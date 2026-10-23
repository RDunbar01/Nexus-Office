"""Build an offline, single-file Office browser trial without dropping app assets."""
from pathlib import Path
import base64,gzip,hashlib,json,re,os
ROOT=Path(__file__).resolve().parent
SOURCE=Path(os.environ.get('NEXUS_OFFICE_SOURCE',str(ROOT/'baseline-source')))
OUT=ROOT/'dist';OUT.mkdir(exist_ok=True)
def sha(b):return hashlib.sha256(b).hexdigest()
original_bytes=(SOURCE/'candidate.html').read_bytes()
assert sha(original_bytes)=='963417585f38be4223f9caf47b66f1f2d184718a414c2f8d736821a715d295e5', 'Baseline candidate differs from reviewed 6.45.0 source'
original=original_bytes.decode('utf-8')
canonical=original
vendors={}
EXPECTED_VENDORS={'092_nexus-writing-writing_vendor.js': 'b020ab03cde13f3989d4c6d3bf6d661fef2d3a6201ace620578466270529e2f0', '097_nx-clipart-data.js': 'd4475f684d11d69b173fcba7ae9e91c5474c3a08ebb73c0993df8dbc0dd2a3e9'}
for name in ['092_nexus-writing-writing_vendor.js','097_nx-clipart-data.js']:
 data=(SOURCE/'source_scripts'/name).read_bytes();vendors[name]=sha(data)
 assert vendors[name]==EXPECTED_VENDORS[name], 'Baseline vendor differs: '+name
 pattern=r'(<script\b[^>]*?) src="source_scripts/'+re.escape(name)+r'"(></script>)'
 canonical,n=re.subn(pattern,lambda m:m[1]+'>'+data.decode('utf-8')+'</script>',canonical)
 assert n==1
assert not re.search(r'<script\b[^>]*\bsrc=',canonical)
old='Commercial use of Nexus-owned software requires express written consent from the rights holder.'
new='Personal use and internal commercial testing and evaluation of Nexus-owned software are permitted. Distribution, modification, production deployment and other commercial use require express written consent. See the <a href="https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md" target="_blank" rel="noopener noreferrer">current evaluation permission</a>.'
assert canonical.count(old)==1
app=canonical.replace(old,new)
ready='''<script id="nx-office-browser-pack-ready">window.NXOfficeBrowserPackage=Object.freeze({schema:1,engineVersion:'6.45.0',packagingRevision:1,standalone:true});document.documentElement.dataset.nxOfficeBrowserReady='true';</script>'''
body_end=app.rfind('</body>');assert body_end>len(app)-100
app=app[:body_end]+ready+'\n'+app[body_end:]
# Long base64-wrapped JSON contains tensors also embedded elsewhere. Decode only
# canonical UTF-8 JSON-shaped base64, recursively store its text, and deduplicate
# exact long strings in a dictionary. No model values or app expressions change.
pattern=re.compile(r'[A-Za-z0-9+/=]{1000,}')
chunks=[];lookup={};duplicate_refs=0;json_wrappers=0

def pack(text,depth=0):
 global duplicate_refs,json_wrappers
 if depth>4:raise ValueError('Unexpected nesting')
 parts=[];pos=0
 for m in pattern.finditer(text):
  parts.append(text[pos:m.start()]);value=m.group()
  try:
   decoded=base64.b64decode(value,validate=True).decode('utf-8')
   if base64.b64encode(decoded.encode()).decode()!=value or not decoded.startswith(('{','[')):raise ValueError()
   json.loads(decoded)
   node={'b':pack(decoded,depth+1)};json_wrappers+=1
  except (ValueError,UnicodeDecodeError):
   if value not in lookup:lookup[value]=len(chunks);chunks.append(value)
   else:duplicate_refs+=1
   node={'r':lookup[value]}
  parts.append(node);pos=m.end()
 parts.append(text[pos:]);return parts
parts=pack(app)
packed=json.dumps({'schema':1,'chunks':chunks,'parts':parts},ensure_ascii=False,separators=(',',':')).encode('utf-8')

def unpack(nodes):
 return ''.join(n if isinstance(n,str) else chunks[n['r']] if 'r' in n else base64.b64encode(unpack(n['b']).encode()).decode() for n in nodes)
assert unpack(parts)==app
compressed=gzip.compress(packed,compresslevel=9,mtime=0)
payload=base64.b85encode(compressed).decode()
assert base64.b85decode(payload)==compressed
assert "</script" not in payload.lower()
assert "<!--" not in payload and "<script" not in payload.lower(), "Base85 payload contains a script parser state marker"
config={'schema':1,'compressedBytes':len(compressed),'packedBytes':len(packed),'htmlBytes':len(app.encode()),'compressedSha256':sha(compressed),'htmlSha256':sha(app.encode())}
loader=(ROOT/'loader.js').read_text(encoding='utf-8')
wrapper='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Nexus Office 6.45.0 · Browser Trial</title><style>body{margin:0;background:#101628;color:#eff4ff;font:16px/1.5 system-ui,sans-serif}main{max-width:700px;margin:10vh auto;padding:32px;border:1px solid #3b5370;border-radius:18px;background:#19233b}a{color:#7cddff}progress{width:100%;height:14px}#nxBootError{color:#ffb8af;white-space:pre-wrap}button{padding:10px 20px;font:inherit}</style></head><body><main id="nxOfficeBoot"><h1>Nexus Office</h1><p>Version 6.45.0 · Single-file browser trial · Packaging revision 1</p><p id="nxBootStatus" role="status" aria-live="polite">Preparing the embedded application locally…</p><progress id="nxBootProgress" max="5" value="0" aria-label="Startup progress"></progress><p id="nxBootError" role="alert" hidden></p><button id="nxBootRetry" type="button" hidden>Retry startup</button><p>No server, Python installation or application-code download is needed. This file expands its bundled assets in memory. Startup time depends on your device.</p><p>Personal use and internal commercial testing are permitted. Distribution and other uses require written consent. <a href="https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md" target="_blank" rel="noopener noreferrer">Evaluation permission</a> · <a href="https://github.com/RDunbar01/Nexus-Office" target="_blank" rel="noopener noreferrer">Source and full package</a></p><noscript>JavaScript is required to open this trial.</noscript></main><script id="nxOfficePackConfig" type="application/json">CONFIG</script><script id="nxOfficePackedApp" type="application/octet-stream">PAYLOAD</script><script id="nxOfficeBootLoader">LOADER</script></body></html>'''
wrapper=wrapper.replace('CONFIG',json.dumps(config,separators=(',',':'))).replace('PAYLOAD',payload).replace('LOADER',loader)
output=wrapper.encode();assert len(output)<20_000_000
(OUT/'Nexus_Office_v6_45_0_Browser.html').write_bytes(output)
# Expanded artifacts are local verification inputs, not distribution components.
(ROOT/'canonical_full.html').write_text(canonical,encoding='utf-8',newline='\n')
(ROOT/'expanded_trial.html').write_text(app,encoding='utf-8',newline='\n')
manifest={'source_main':'50c4332214395bc883a98fd5e589a84d927529ee','engine_version':'6.45.0','packaging_revision':1,'filename':'Nexus_Office_v6_45_0_Browser.html','html_bytes':len(output),'html_sha256':sha(output),'git_blob_sha1':hashlib.sha1(b'blob '+str(len(output)).encode()+b'\0'+output).hexdigest(),'source_candidate_sha256':sha(original.encode()),'canonical_full_html_sha256':sha(canonical.encode()),'canonical_full_html_bytes':len(canonical.encode()),'expanded_trial_sha256':sha(app.encode()),'expanded_trial_bytes':len(app.encode()),'config':config,'vendors':vendors,'deduplicated_references':duplicate_refs,'decoded_json_wrappers':json_wrappers,'dictionary_entries':len(chunks),'presentation_deltas':['One current evaluation-permission sentence and link','One end-of-body browser-package readiness marker'],'limits':['Distributed HTML below 20,000,000 bytes; expanded app is larger and runtime memory use is higher','Modern browser with DecompressionStream, TextEncoder/TextDecoder and Web Crypto required','No Windows/Radeon performance qualification','Existing application legal notice is retained; no automatic acceptance']}
(ROOT/'BUILD_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:manifest[k]for k in ['html_bytes','html_sha256','expanded_trial_bytes','deduplicated_references']}))
