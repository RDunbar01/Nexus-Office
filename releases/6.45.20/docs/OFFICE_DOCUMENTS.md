# Nexus Office 6.45.20 revision 6 — documents and sheets

## Using tabs

Writer and Paint now have a tab strip at the bottom of the application. The Office navigation remains in place. Click **+** to add a document or sheet. Click a tab to switch, or double-click its name to rename it. F2 also starts renaming; Enter accepts and Escape cancels. Arrow keys move between tabs. Each tab retains its own document content and session Undo history.

In Paint, **Clear** clears only the active sheet and can be undone. Other sheets retain their pixels, objects, layers and canvas dimensions. **Save project** downloads a `.nxpaint` containing every sheet. **Export** downloads only the active sheet, using that sheet's name. Older one-sheet `.nxpaint` projects open as an additional sheet. Closing a tab asks for confirmation; save the collective project first if you want to keep it.

In Writer, **Open** accepts multiple files and opens each supported document in its own tab. **Save project** downloads all Writer tabs in a `.nxwriter` file. Regular document and PDF exports use the active tab. A collective project stores editing data, retained originals and compatibility previews; it is not a combined Word document. Opening a collective project replaces that application's current collection after confirmation. Native `.nxo` snapshots also include both tab collections. Projects support up to 25 tabs and 120 MiB; Undo history is session-only.

In Sheets, double-click a worksheet tab to rename it inline. The existing worksheet rename backend updates sheet references. Existing sheet-name validation still applies.

## Compatibility and preserved originals

Compatibility follows the document format, not the operating system on which the document was made. **Compatibility view** shows the retained source PDF, embedded preview, or locally converted PDF. It does not reflect later edits in Nexus. **Download original** retrieves the exact imported file. Editable imports reconstruct supported content; they do not guarantee every feature of the authoring application.

| Application | Browser import | Optional local conversion |
| --- | --- | --- |
| Writer | DOCX, DOCM, DOTX, DOTM; ODT; RTF; TXT; Markdown; HTML; NWD; PDF text and original PDF preview | Legacy DOC/DOT, Pages, additional OpenDocument variants and word processor formats supported by the installed converter |
| Sheets | XLSX, XLSM, XLTX, XLTM; ODS; CSV and TSV | XLS, XLSB, XLT, Numbers and additional supported spreadsheet formats |
| Present | PPTX, PPTM, PPSX, PPSM, POTX, POTM; ODP | PPT, PPS, POT, Keynote and additional supported presentation formats |

Apple Pages files with an embedded PDF can supply a preview and editable PDF text without local conversion. A file containing only an embedded image can show that first-page preview, explicitly labelled as incomplete. Other Pages versions require conversion or export from Pages. PDF text import is an editable reconstruction, while Compatibility view retains the original page appearance. Scanned PDFs can be viewed; OCR is not included. PDF import supports up to 300 pages.

For DOCX or PPTX structures rejected by the richer native reader, a compatibility reader imports supported text, tables/images for Writer, and text/images for Present. The interface identifies this fallback and retains the original. Advanced drawing effects, animations, charts, embedded objects, fonts and pagination can differ. Encrypted, damaged or unsupported files can still require the original application. This release does not claim universal or pixel-identical compatibility with every historical format version.

Macro-enabled files can be opened for supported document content. VBA, ActiveX and embedded code are **not executed**. The exact original, including its code, remains available separately. Edited exports do not promise preservation or execution of unsupported program features. Formula results and layout may differ when a workbook relies on macros, external links or unsupported functions.

## Local conversion and PKI setup

Extract the complete browser ZIP and keep `document_assets`, `theme_assets` and `comparison_assets` beside the HTML. The HTML can be opened directly for tabs, browser imports, PDF preview, signature appearances and browser printing.

For legacy conversion and direct paginated PDF downloads:

1. Install Python 3.10 or later and [LibreOffice](https://www.libreoffice.org/download/download-libreoffice/).
2. Run `python Start_Nexus_Office.py` from the extracted folder (`python3` on systems using that command).
3. Keep the launcher window open while using the Office window it opens. Close it to stop the local helper.

The helper binds only to `127.0.0.1`, uses a per-launch authorization token and an isolated temporary LibreOffice profile. Conversion runs locally. Macros and automatic link updates are disabled. A nonstandard LibreOffice installation can be selected with `NEXUS_OFFICE_CONVERTER` set to its executable path. The helper belongs only to this Office package and does not modify a shared Nexus launcher.

For certificate signing, run `python Start_Nexus_Office.py --setup-signing` once. This installs pinned pyHanko 0.31.0 into this package's private `.nexus-office-python` environment, then opens Office. Initial setup needs an internet connection. Normal signing and conversion use local files.

## Signatures and PDF

Open Writer's **Signature** control. Draw a signature, upload a signature image, or reuse a signature saved on this device. Enter a name and choose **Insert signature and date**. The current local date is inserted with the signature and is retained in the document. Saving a signature is optional; the same dialog can remove it. A signature image is an appearance, not a certificate signature.

For a cryptographic signature, choose a `.p12` or `.pfx` containing your certificate and private key, enter its password, and select **Sign and download PDF**. Nexus converts the active Writer document to PDF and signs that PDF with SHA-256 CMS. The signature includes the certificate identity and signing time. The password and identity are not stored in the project or browser storage, and temporary signing files are cleaned up. Recipient trust depends on the certificate chain. No online revocation check or trusted timestamp is added.

**Save as PDF** offers browser **Print / Save as PDF** and a direct **Download PDF** through the local conversion engine. Both operate on the current Writer tab. Browser printing uses a simplified print layout; the local route exports supported DOCX content and paginates it with LibreOffice. Review the resulting PDF when exact pagination matters.

## Implementation and validation

The release adds three modules: document tabs, compatibility routing and signatures. The existing Paint project API delegates to the tab collection; image export retains active-sheet semantics. Theme tokens style the tab strip. Existing template catalogues, aviation heat maps and ten Office themes remain in place.

`document_assets/pdf-runtime.js` bundles Mozilla PDF.js 5.6.205 under its included Apache 2.0 license. It renders locally without a CDN. Existing fonts and PDF features can still impose rendering limits.

Validation uses Chromium on Linux at phone, desktop and 3840×2160 viewports; real LibreOffice conversions of DOC, XLS and PPT; source/project round trips; a self-signed test PKCS#12 identity with cryptographic PDF validation; original-byte preservation; and local service authorization checks. The Pages test uses a synthetic package with a genuine embedded PDF; the macro fixture contains inert test VBA bytes. These tests do not establish compatibility with every real-world Apple file, VBA program, or Office version. Windows and macOS hardware were not exercised.

See `RELEASE_VALIDATION.json` for the exact completed checks. The older Word implementation guide remains the revision 3 guide; this document describes the revision 6 additions.
