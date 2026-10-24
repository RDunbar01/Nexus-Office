# Nexus Office 6.45.20 · revision 6

## [▶ Open Nexus Office in your browser](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/Nexus_Office_v6_45_20_Browser.html)

**Go straight to the application. No installation or Python is needed for the browser edition.** Use a current desktop Chromium browser, read the application notice and choose whether to continue. Initial loading depends on your device and connection.

[Release files](releases/6.45.20/) · [Offline instructions](docs/BROWSER_TRIAL.md) · [English](https://github.com/RDunbar01/Nexus-Office/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Office/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ko)

Nexus Office brings Writer, Grid, Dashboard Studio, NexusPoint and Paint into one workspace. Home also provides Compatibility, Open and Settings.

## What changed in revision 6

- **Writer and Paint tabs:** add and switch documents at the bottom, then double-click a tab or press F2 to rename it. Each tab has its own content and session Undo history. Paint Clear and image export affect only the active sheet.
- **Collective projects:** Writer saves all tabs as `.nxwriter`; Paint saves all sheets as `.nxpaint`. Regular document and image exports use the active tab. Projects support up to 25 tabs and 120 MiB; Undo history is not saved. Opening a collective project replaces that application's collection after confirmation.
- **Sheets renaming:** double-click a worksheet tab to rename it through the existing reference-aware backend.
- **PDF and compatibility:** the bundled local PDF runtime imports editable text and displays the retained original page layout. Compatibility view does not reflect later edits. Original files remain available to download. PDF import/preview supports up to 300 pages; scanned PDFs have no OCR.
- **Signature appearances:** Writer can insert a drawn, uploaded or saved signature image with the current local date. An image of a signature is not a cryptographic signature.

**Legacy format conversion, direct paginated PDF download and certificate-based PDF signing require the optional local helper. They are not provided by the GitHub Pages launch alone.** The helper uses Python 3.10+ and LibreOffice; PKI signing needs additional package-specific setup. Macro-enabled files can expose supported content and retain their originals, but VBA, ActiveX and embedded code do not run. Compatibility is format-specific, not a guarantee of perfect Office or Apple fidelity. See the [documents and signatures guide](releases/6.45.20/docs/OFFICE_DOCUMENTS.md) and [local setup](docs/BROWSER_TRIAL.md#optional-local-conversion-and-certificate-signing).

## Office themes

The ten themes from revision 5 remain available through **Settings → Office themes**. Porcelain is the default without a saved choice. Themes change Home, navigation and editing-panel appearance, not authored content. The choice is stored for this browser and origin; blocked storage keeps it for the session. [Office themes guide](releases/6.45.20/docs/OFFICE_THEMES.md).

## Try the included workspaces

- **Aviation dashboard:** open Dashboard Studio → Aviation example → Use template. It contains 14 editable source tables, 101 fictional records, six pages, 15 measures and 23 visuals. Fleet overview and Safety & risks include a live 5 × 5 impact/likelihood matrix. Source edits update the matrix; selecting a cell filters the page.
- **Paint and Design Studio:** 629 templates, 2,720 elements and 19 fonts are retained from revision 2. Open Paint → Design Studio → Photos → Before & after collections for 100 generated comparison pairs in two sets of 100 editable layouts. Photos, text and other objects remain separate layers. Generated examples illustrate eyebrow designs; they are not records of real treatment outcomes.
- **Independent dashboard example:** [open the editable aviation example](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/examples/NEXUS_General_Aviation_Dashboard.html).

See the [release changelog](releases/6.45.20/docs/CHANGELOG_6.45.20.md) and [installation notes](releases/6.45.20/INSTALL.txt) for the exact scope.

## Use it offline

The browser HTML is **19,976,619 bytes**. It is not fully self-contained. Keep all three asset folders beside it:

- **`document_assets/`** contains the PDF runtime, its manifest and Mozilla PDF.js license. Keep these files for local PDF import and preview.
- **`theme_assets/`** contains 12 PNGs for theme artwork. If they are missing, built-in vector previews remain available and theme controls still work.
- **`comparison_assets/`** contains `photos-01.js` through `photos-10.js` for all 100 generated comparison-photo pairs, plus the matching manual-import packs.

Download the repository with **Code → Download ZIP**, extract it, and open `releases/6.45.20/Nexus_Office_v6_45_20_Browser.html`. Keep that release folder's structure intact. If selecting individual files, download the HTML and all three asset folders while preserving their names and relative paths. No local server is needed for this browser edition.

If comparison photos are missing, use **Load comparison photos** and select the matching `.nxcomparisons` packs from the same release. Saved `.nxpaint` projects embed the photos they use. Back up existing documents and projects before opening another version; this release does not rewrite saved projects.

The browser needs DecompressionStream, TextEncoder/TextDecoder and Web Crypto. Expanded application data is about 33.0 MB; runtime memory use is higher than the download size.

## Full package and optional source installation

The [6.45.20 release directory](releases/6.45.20/) contains the **482 delivered files**, totaling **500,273,126 extracted bytes**. Every distributed file is below **20,000,000 bytes**. The large full and browser ZIP containers are not committed; their extracted components are supplied instead.

For source installation, keep `installer.py`, `package_manifest.json` and **all 23** `Nexus_office_Data_001.nxd` through `Nexus_office_Data_023.nxd` files together. Each data part is at most 10,000,000 bytes. Use standard CPython 3.12 and follow [INSTALL.txt](releases/6.45.20/INSTALL.txt); `python installer.py --no-launch` extracts without launching. Do not mix parts from different releases. Keep extracted `candidate.html`, `source_scripts`, `document_assets`, `theme_assets` and `comparison_assets` together.

[Earlier releases](releases/) remain available. The delivered 6.45.20 application and package components are preserved unchanged, rather than rebuilt for publication.

## Validation and limits

The [supplied revision-6 validation](releases/6.45.20/RELEASE_VALIDATION.json) records **25 browser-document checks, 14 theme checks, 21 Design Studio checks and 9 risk checks**, plus **6 service checks, 6 source checks and 5 loader cases**, in Chromium on Linux. It includes real LibreOffice conversions and a self-signed test certificate, but the Pages embedded-preview and macro fixtures are synthetic. Older receipts are retained as historical evidence, not counted as new revision-6 runs.

[Separate read-only package checks](docs/PUBLICATION_VERIFICATION_6.45.20.json) cover archive contents, sizes, hashes, data parts, source inventories, browser reconstruction and companion-asset paths. They are integrity checks, not a new functional or cross-platform test. Windows and macOS hardware were not exercised; physical display and Radeon performance qualification are not established by these records. Startup speed and document-format fidelity are not guaranteed. [Artifact hashes and technical details](docs/BROWSER_TRIAL.md). The included Word implementation guide remains the revision 3 guide; use OFFICE_DOCUMENTS.md for revision 6.

## License and attribution

Rich Dunbar / Nexus Emerging Technology. Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Redistribution, modification, production deployment and other commercial use require express written consent. Third-party licenses and previously granted rights remain unchanged.

Read the [repository license](LICENSE), [commercial-evaluation permission](COMMERCIAL_EVALUATION_PERMISSION.md), [license scope](NEXUS_LICENSE_SCOPE.md) and the release's bundled notices. Source availability does not grant additional rights.
