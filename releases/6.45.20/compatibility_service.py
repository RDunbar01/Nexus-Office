"""Nexus Office's optional, isolated loopback conversion and PDF signing service."""
from __future__ import annotations
import argparse, base64, hmac, importlib.util, io, json, os, secrets, shutil, subprocess, sys, tempfile, threading, webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

MAX_FILE = 120 * 1024 * 1024
MAX_REQUEST = 180 * 1024 * 1024
WRITER = {'doc','docx','docm','dot','dotx','dotm','odt','ott','fodt','rtf','pages','wps','wpd','html','htm','txt'}
GRID = {'xls','xlsx','xlsm','xlsb','xlt','xltx','xltm','ods','ots','fods','csv','tsv','xml','numbers'}
PRESENT = {'ppt','pptx','pptm','pps','ppsx','ppsm','pot','potx','potm','odp','otp','fodp','key','keynote'}

def office_executable():
    supplied = os.environ.get('NEXUS_OFFICE_CONVERTER')
    candidates = [supplied, shutil.which('soffice'), shutil.which('libreoffice'),
                  r'C:\Program Files\LibreOffice\program\soffice.exe',
                  r'C:\Program Files (x86)\LibreOffice\program\soffice.exe',
                  '/Applications/LibreOffice.app/Contents/MacOS/soffice']
    return next((str(Path(p).resolve()) for p in candidates if p and Path(p).is_file()), None)

def decode_file(value, label='file', maximum=MAX_FILE):
    if not isinstance(value, str) or len(value) > maximum * 4 // 3 + 8:
        raise ValueError(f'{label} exceeds its size limit.')
    try:
        data = base64.b64decode(value, validate=True)
    except Exception as error:
        raise ValueError(f'{label} is not valid base64.') from error
    if not data or len(data) > maximum:
        raise ValueError(f'{label} is empty or too large.')
    return data

def convert_document(data, filename, target=None):
    executable = office_executable()
    if not executable:
        raise ValueError('Install LibreOffice, then restart the Nexus Office launcher to enable legacy and cross-platform conversion.')
    ext = Path(filename).suffix.lower().lstrip('.')
    app = 'writer' if ext in WRITER else 'grid' if ext in GRID else 'present' if ext in PRESENT else None
    if not app:
        raise ValueError('This file type is not supported by the local converter.')
    native = {'writer':'docx','grid':'xlsx','present':'pptx'}[app]
    if target not in {None, 'pdf', native}:
        raise ValueError('Unsupported conversion target.')
    with tempfile.TemporaryDirectory(prefix='nexus-office-convert-') as tmp:
        root = Path(tmp); profile = root/'profile'; profile.mkdir()
        # An isolated profile has no trusted sources; macros and link updates are disabled.
        (profile/'user').mkdir()
        (profile/'user/registrymodifications.xcu').write_text('''<?xml version="1.0" encoding="UTF-8"?>
<oor:items xmlns:oor="http://openoffice.org/2001/registry">
<item oor:path="/org.openoffice.Office.Common/Security/Scripting"><prop oor:name="MacroSecurityLevel" oor:op="fuse"><value>3</value></prop><prop oor:name="DisableMacrosExecution" oor:op="fuse"><value>true</value></prop></item>
<item oor:path="/org.openoffice.Office.Writer/Content/Update"><prop oor:name="Link" oor:op="fuse"><value>0</value></prop></item>
<item oor:path="/org.openoffice.Office.Calc/Content/Update"><prop oor:name="Link" oor:op="fuse"><value>0</value></prop></item>
</oor:items>''')
        incoming = root/('input.'+ext); incoming.write_bytes(data)
        outputs = {}
        for fmt in ([target] if target else [native, 'pdf']):
            if fmt == ext and fmt != 'pdf':
                outputs[fmt] = data; continue
            folder = root/('out-'+fmt); folder.mkdir()
            args = [executable, '-env:UserInstallation='+profile.as_uri(), '--headless', '--nologo', '--nodefault', '--norestore', '--convert-to', fmt, '--outdir', str(folder), str(incoming)]
            result = subprocess.run(args, capture_output=True, timeout=90, check=False)
            output = folder/('input.'+fmt)
            if result.returncode or not output.is_file() or not output.stat().st_size:
                raise ValueError('The local engine could not convert this file. It may be encrypted, damaged, or use an unsupported format version. Open it in its authoring app and export DOCX, XLSX, PPTX or PDF.')
            if output.stat().st_size > MAX_FILE:
                raise ValueError('The converted file exceeds 120 MiB.')
            outputs[fmt] = output.read_bytes()
        return {'app':app, 'nativeFormat':native, 'files':{k:base64.b64encode(v).decode() for k,v in outputs.items()},
                'notes':['Converted by local LibreOffice. Layout, fonts, advanced features and embedded objects may differ from the authoring application.', 'VBA, ActiveX and embedded code are not executed. The original source remains available separately.']}

def sign_pdf(data, p12, password, name='', reason='Signed in Nexus Writer'):
    if not data.startswith(b'%PDF-'):
        raise ValueError('Choose a PDF to sign.')
    try:
        from pyhanko.sign import signers, fields
        from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
        from cryptography.hazmat.primitives.serialization import pkcs12
        from cryptography.x509.oid import NameOID
    except ImportError as error:
        raise ValueError('PKI support is not installed. Run Start_Nexus_Office.py --setup-signing once.') from error
    import datetime
    password_bytes = password.encode('utf-8') if password else None
    try:
        private_key, certificate, _ = pkcs12.load_key_and_certificates(p12, password_bytes)
    except Exception as error:
        raise ValueError('Cannot unlock this PKCS#12 file. Check the password and choose a .p12 or .pfx containing a private key.') from error
    if private_key is None or certificate is None:
        raise ValueError('This certificate file does not contain a signing private key.')
    now = datetime.datetime.now(datetime.timezone.utc)
    if not certificate.not_valid_before_utc <= now <= certificate.not_valid_after_utc:
        raise ValueError('The signing certificate is not currently within its validity period.')
    subject = certificate.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    signer_name = subject[0].value if subject else name or certificate.subject.rfc4514_string()
    with tempfile.TemporaryDirectory(prefix='nexus-office-sign-') as tmp:
        path = Path(tmp)/'identity.p12'
        path.write_bytes(p12)
        try:
            path.chmod(0o600)
        except OSError:
            pass
        signer = signers.SimpleSigner.load_pkcs12(str(path), passphrase=password_bytes)
        if signer is None:
            raise ValueError('The signing identity could not be loaded.')
        writer = IncrementalPdfFileWriter(io.BytesIO(data))
        field_name = 'NexusSignature_'+secrets.token_hex(6)
        # Standard CMS signature in the PDF. An unsigned appearance is never labelled PKI-signed.
        metadata = signers.PdfSignatureMetadata(field_name=field_name, name=signer_name, reason=reason[:300], md_algorithm='sha256')
        output = signers.PdfSigner(metadata, signer=signer, new_field_spec=fields.SigFieldSpec(field_name, on_page=-1, box=(36,30,330,88))).sign_pdf(writer)
        return {'pdf':base64.b64encode(output.getvalue()).decode(), 'signer':signer_name, 'signedAt':now.isoformat(),
                'note':'The PDF contains a cryptographic signature. Recipient trust depends on the certificate chain; no online revocation check or trusted timestamp was requested.'}

class OfficeServer(ThreadingHTTPServer):
    daemon_threads = True
    def __init__(self, root, port=0):
        self.root = Path(root).resolve(); self.token = secrets.token_urlsafe(32); self.jobs = threading.BoundedSemaphore(2)
        super().__init__(('127.0.0.1', port), Handler)

class Handler(BaseHTTPRequestHandler):
    server_version = 'NexusOffice/6.45.20'
    def log_message(self, *args):
        pass  # Never log keys, passwords, document bodies or authentication URLs.
    def reply(self, code, body, content_type='application/json'):
        data = json.dumps(body).encode() if isinstance(body, dict) else body
        self.send_response(code); self.send_header('Content-Type', content_type); self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control','no-store'); self.send_header('X-Content-Type-Options','nosniff'); self.send_header('Referrer-Policy','no-referrer'); self.end_headers(); self.wfile.write(data)
    def valid_host(self):
        return self.headers.get('Host') == '127.0.0.1:'+str(self.server.server_port)
    def do_GET(self):
        if not self.valid_host(): return self.reply(403, {'error':'Invalid host.'})
        path = unquote(urlsplit(self.path).path)
        if path == '/api/office/health':
            return self.reply(200, {'service':'Nexus Office compatibility', 'version':1, 'conversion':bool(office_executable()), 'signing':bool(importlib.util.find_spec('pyhanko'))})
        relative = path.lstrip('/') or 'Nexus_Office_v6_45_20_Browser.html'
        file = (self.server.root/relative).resolve()
        permitted = relative in {'Nexus_Office_v6_45_20_Browser.html','candidate.html'} or relative.startswith(('theme_assets/','comparison_assets/','document_assets/','source_scripts/'))
        if not permitted or not file.is_relative_to(self.server.root) or not file.is_file(): return self.reply(404, {'error':'File not found.'})
        content_type = {'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.png':'image/png','.json':'application/json'}.get(file.suffix,'application/octet-stream')
        return self.reply(200,file.read_bytes(),content_type)
    def do_POST(self):
        if not self.valid_host() or not hmac.compare_digest(self.headers.get('X-Nexus-Office-Token',''), self.server.token): return self.reply(403, {'error':'Start Nexus Office from its launcher to authorize this local request.'})
        origin = self.headers.get('Origin')
        if origin and origin != 'http://127.0.0.1:'+str(self.server.server_port): return self.reply(403, {'error':'This request is not from the Nexus Office window.'})
        path = urlsplit(self.path).path
        if path not in {'/api/office/convert','/api/office/sign'}: return self.reply(404, {'error':'Unknown operation.'})
        try:
            size = int(self.headers.get('Content-Length','0'))
            if size < 1 or size > MAX_REQUEST: raise ValueError('Request exceeds its size limit.')
            if self.headers.get('Content-Type','').split(';')[0] != 'application/json': raise ValueError('JSON content required.')
            if not self.server.jobs.acquire(blocking=False): return self.reply(429, {'error':'Wait for another conversion to finish.'})
            try:
                request = json.loads(self.rfile.read(size))
                data = decode_file(request.get('data'))
                if path.endswith('/convert'):
                    result = convert_document(data, str(request.get('name','')), request.get('target'))
                else:
                    result = sign_pdf(data, decode_file(request.get('identity'), 'Signing identity', 4*1024*1024), str(request.get('password','')), str(request.get('name','')), str(request.get('reason','Signed in Nexus Writer')))
                self.reply(200,result)
            finally:
                self.server.jobs.release()
        except (ValueError, TimeoutError, subprocess.TimeoutExpired) as error:
            self.reply(400, {'error':str(error)[:800]})
        except Exception:
            self.reply(500, {'error':'The local operation failed. No document was replaced. Check that the file and signing identity are supported.'})

def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--root',type=Path,default=Path(__file__).parent); parser.add_argument('--port',type=int,default=0); parser.add_argument('--no-launch',action='store_true'); args=parser.parse_args()
    server = OfficeServer(args.root,args.port)
    entry = 'Nexus_Office_v6_45_20_Browser.html' if (args.root/'Nexus_Office_v6_45_20_Browser.html').is_file() else 'candidate.html'
    url='http://127.0.0.1:'+str(server.server_port)+'/'+entry+'?nexusOfficeToken='+server.token
    print('Nexus Office local compatibility service is running. Close this window to stop it.',flush=True)
    print('LibreOffice conversion: '+('available' if office_executable() else 'install LibreOffice to enable'),flush=True)
    if not args.no_launch: webbrowser.open(url)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()

if __name__ == '__main__': main()
