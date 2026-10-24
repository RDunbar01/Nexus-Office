# Nexus Office 6.45.20 · revision 6

## [▶ Open Nexus Office now](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/Nexus_Office_v6_45_20_Browser.html)

The link opens the application directly. No installation or Python is needed for the browser edition. Use a current desktop Chromium browser, read the application notice and choose whether to continue. Loading time depends on your device and connection.

[Français](https://github.com/RDunbar01/Nexus-Office/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ko) · [Release files](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.20)

## Documents, sheets and signatures

Revision 6 adds bottom tabs in Writer and Paint. Use **+** to add a tab; double-click a tab or press F2 to rename it. Each tab retains its own content and session Undo history. Paint Clear and image export affect only the active sheet. Writer saves all tabs as `.nxwriter`; Paint saves all sheets as `.nxpaint`. Collective projects support up to 25 tabs and 120 MiB; Undo history is not saved. Opening one replaces the application's collection after confirmation. Sheets tabs also rename inline using the existing reference-aware backend.

PDF import reconstructs editable text while retaining the original page layout for Compatibility view. That view does not reflect later Nexus edits. Original files remain available to download. PDF import/preview is limited to 300 pages, and scanned PDFs have no OCR. Macro-enabled originals are retained, but VBA, ActiveX and embedded code do not execute.

Writer can insert a drawn, uploaded or saved signature image with the current local date. **A signature image is not a cryptographic signature. Legacy conversion, direct paginated PDF download and PKI signing require the optional local helper, not just the hosted browser page.** The helper needs Python 3.10+ and LibreOffice; certificate signing requires additional package-specific setup. Read the [documents and signatures guide](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/OFFICE_DOCUMENTS.md) before using those features.

## Themes and retained workspaces

All ten themes remain available through **Settings → Office themes**. Porcelain is the default without a saved choice. Themes change the interface, not authored content. The preference is saved for this browser and origin; blocked storage keeps it for the session. Keep the theme artwork alongside the HTML. [Office themes guide](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/OFFICE_THEMES.md).

- **Dashboard Studio → Aviation example → Use template:** 14 editable tables, 101 fictional records, six pages, 15 measures and 23 visuals. Fleet overview and Safety & risks contain a live 5 × 5 risk matrix. Editing Impact or Likelihood moves the risk; selecting a cell filters the page. [Open the independent editable example](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/examples/NEXUS_General_Aviation_Dashboard.html).
- **Paint → Design Studio:** 629 templates, 2,720 elements and 19 fonts retained from revision 2. **Photos → Before & after collections** provides 100 generated comparison pairs in two collections of 100 editable layouts. Photos and text remain separate layers. The images illustrate eyebrow designs, not actual treatment outcomes.

The included Word implementation guide still describes revision 3's functional features; OFFICE_DOCUMENTS.md describes revision 6. [Read the changelog](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/CHANGELOG_6.45.20.md).

## Offline use and installation

The browser HTML is 19,976,619 bytes, but **the PDF runtime, theme artwork and complete photo collection are not contained in the HTML alone**. Keep `document_assets`, `theme_assets` and `comparison_assets` beside it. The complete `document_assets` folder supplies the PDF runtime, manifest and vendor license for local PDF import and preview. The 12 PNGs in `theme_assets` provide theme artwork; missing pictures fall back to built-in vector previews without disabling theme controls or launch actions. Keep `comparison_assets/photos-01.js` through `photos-10.js` beside it in the `comparison_assets` folder. Those ten companions provide all 100 generated pairs. If they are missing, use **Load comparison photos** to import the matching `.nxcomparisons` packs. Saved `.nxpaint` projects embed the photos they use.

For a complete download, choose **Code → Download ZIP** in the repository, extract it and open `releases/6.45.20/Nexus_Office_v6_45_20_Browser.html`. Keep the folder structure intact. No local server is needed. The browser must support DecompressionStream, TextEncoder/TextDecoder and Web Crypto. Expanded application data and runtime memory are larger than the HTML download.

The full release contains 482 files totaling 500,273,126 extracted bytes. Every distributed file is below 20,000,000 bytes. The large original ZIPs are not committed; their extracted components are supplied. For optional source installation, keep the installer, manifest and **all 23 `.nxd` parts** together. Each part is at most 10,000,000 bytes. Follow [INSTALL.txt](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/INSTALL.txt) with standard CPython 3.12. Keep extracted `candidate.html`, `source_scripts`, `document_assets`, `theme_assets` and `comparison_assets` together.

Back up existing documents and projects before moving between versions. This release does not rewrite saved projects. [Earlier releases](https://github.com/RDunbar01/Nexus-Office/tree/main/releases) remain available.

## Validation and limits

[Supplied revision-6 results](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/RELEASE_VALIDATION.json) record 25 browser-document checks, 14 theme checks, 21 Design Studio checks and 9 risk checks, plus 6 service checks, 6 source checks and 5 loader cases in Chromium on Linux. They include real LibreOffice conversion and a self-signed test certificate. The Pages embedded-preview and macro fixtures are synthetic, not proof of compatibility with every real-world file. Older receipts remain historical evidence, not new revision-6 runs.

The [separate package review](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/PUBLICATION_VERIFICATION_6.45.20.json) checks bytes, hashes, inventories, reconstruction and companion paths without running the supplied application or functional tests. It is not cross-platform qualification. Windows and macOS hardware were not exercised; Radeon performance and physical 4K monitors are not qualified by these records. Startup speed and document-format fidelity are not guaranteed. [Exact hashes and browser details](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/BROWSER_TRIAL.md).

## Permissions

Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Redistribution, modification, production deployment and other commercial use require express written consent. Third-party licenses and previously granted rights remain unchanged. Read the [license](https://github.com/RDunbar01/Nexus-Office/blob/main/LICENSE), [evaluation permission](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md) and bundled notices.
