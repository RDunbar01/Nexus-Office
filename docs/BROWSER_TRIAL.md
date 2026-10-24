# Nexus Office 6.45.20 browser edition · revision 6

## [▶ Open Nexus Office](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/Nexus_Office_v6_45_20_Browser.html)

[Release files](../releases/6.45.20/) · [Install notes](../releases/6.45.20/INSTALL.txt) · [Changelog](../releases/6.45.20/docs/CHANGELOG_6.45.20.md) · [README](../README.md)

## Start in the browser

The link opens the application directly. Use a current desktop Chromium browser with DecompressionStream, TextEncoder/TextDecoder and Web Crypto. No Python or local server is needed. Read the existing application notice and choose whether to continue; publication does not bypass it. The startup screen reports loading stages and offers Retry on failure. Loading time depends on the connection and device.

Revision 6 adds bottom tabs and collective projects in Writer and Paint, inline worksheet renaming, retained-original compatibility views, local PDF import/preview and signature appearances. Paint Clear and image export affect only the active sheet. Writer `.nxwriter` and Paint `.nxpaint` projects save their entire tab collections; regular exports use the active tab. Projects support up to 25 tabs and 120 MiB, with session-only Undo history. Opening a collective project replaces the current application collection after confirmation.

The ten Office themes remain available through **Settings → Office themes**, with Porcelain as the default without a saved preference. Theme selection changes the interface rather than authored content. Keep theme artwork alongside the HTML. See the [themes guide](../releases/6.45.20/docs/OFFICE_THEMES.md).

**The hosted browser launch does not by itself provide legacy conversion, direct paginated PDF download or PKI signing.** Those features use the optional local helper described below. Browser-only features include tabs, supported imports, PDF preview, signature images and browser printing. The [documents guide](../releases/6.45.20/docs/OFFICE_DOCUMENTS.md) describes current formats and limitations; the Word implementation guide remains the revision 3 guide.

## Offline layout and required companion folders

Keep this structure when copying or downloading the browser edition:

```text
releases/6.45.20/
├── Nexus_Office_v6_45_20_Browser.html
├── Start_Nexus_Office.py
├── compatibility_service.py
├── document_assets/
│   ├── pdf-runtime.js
│   ├── manifest.json
│   └── PDFJS-LICENSE.txt
├── theme_assets/
│   ├── porcelain.png
│   ├── …
│   └── aurora-artwork.png
└── comparison_assets/
    ├── photos-01.js
    ├── photos-02.js
    ├── …
    ├── photos-10.js
    ├── Nexus_Comparison_Photos_01.nxcomparisons
    ├── …
    └── Nexus_Comparison_Photos_10.nxcomparisons
```

The HTML contains the core browser application, but **the PDF runtime, theme artwork and complete comparison-photo collection are not embedded in that one file**. Keep all three companion folders beside it.

`document_assets/` contains `pdf-runtime.js`, `manifest.json` and `PDFJS-LICENSE.txt`. The runtime bundles Mozilla PDF.js 5.6.205 and renders PDFs locally without a CDN. Its Apache 2.0 license applies to that separately licensed component, not to the whole Nexus application. The supplied runtime and license SHA-256 values match the [document-asset manifest](../releases/6.45.20/document_assets/manifest.json).

The `theme_assets/` folder contains 12 PNGs. Missing theme artwork falls back to built-in vector previews; theme selection and launch controls still work. Keep the complete folder beside the HTML.

The comparison-photo collection loads 100 generated pairs from ten adjacent JavaScript companions. Preserve the exact `comparison_assets/` directory name and file names. The `.nxcomparisons` files provide a manual-import alternative through **Load comparison photos**.

For a complete local copy, choose **Code → Download ZIP** in the repository, extract it, then open the HTML inside `releases/6.45.20/`. If downloading individual files, save the actual file contents rather than GitHub's HTML preview. Keep the complete `document_assets` folder, all 12 theme PNGs and all ten photo JavaScript companions in their respective folders. The two Python files in the layout above are for optional helper features, not ordinary browser startup. Opening a comparison template without the photos may prompt for the matching packs; import them and reopen the template.

Paint saves the photos used inside `.nxpaint` projects so those projects can reopen independently of the photo packs. Existing projects and original user imports are not rewritten. Retain backups when moving work between versions. A local copy does not make optional remote media or services available offline.

## Exact artifacts

The delivered HTML and release components are preserved unchanged. The [browser manifest](../releases/6.45.20/BROWSER_BUILD_MANIFEST.json) records the browser packaging details; [BUILD_PROVENANCE.json](../releases/6.45.20/BUILD_PROVENANCE.json) identifies application revision 6. The browser manifest's `packaging_revision: 1` is a packaging field, not the application revision number. Its `source_main` value describes the producer's build source, not the repository publication commit.

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| Browser HTML | 19,976,619 | `6d811bf537c9021cf4b567e64960dcbec2b58fe09c5c6d6856dd9ad390bcdb56` |
| Original full ZIP | 462,846,303 | `6cdf1a0f3d147076a65a58d35e166ab6aecdef10d9886ea09511e23e5c1d1bc0` |
| Original complete-browser ZIP | 116,805,005 | `f72f0cd011627dad1c0580178fd0b1563fc5d46905620fab2378bf281c59229b` |

The two original ZIPs exceed the 20,000,000-byte distribution-file limit and are not committed as archives. The repository carries their extracted components. The full package contains 482 files totaling 500,273,126 bytes; the original complete-browser archive contains 50 files. Every distributed component is below 20,000,000 bytes; the browser HTML is the largest. Expanded browser application data is 32,954,461 bytes, and runtime memory is higher.

## Optional source extraction

Keep `installer.py`, `package_manifest.json` and all 23 numbered `.nxd` data parts from this release in one directory. Each part is at most 10,000,000 bytes. Use standard CPython 3.12:

```text
python installer.py --no-launch
```

Omit `--no-launch` to let the installer launch the extracted entry point. It uses a version- and checksum-isolated directory. Keep `candidate.html`, `source_scripts`, `document_assets`, `theme_assets` and `comparison_assets` together after extraction. The supplied installation notes identify `build.py` for rebuilding expanded source; this publication does not claim an independently reproduced build. Do not use earlier release parts or assume historical repository builders reproduce this release.

## Optional local conversion and certificate signing

Open the extracted release folder containing `Start_Nexus_Office.py`, `compatibility_service.py`, the HTML and all three asset folders. For legacy format conversion and direct paginated PDF downloads, install Python 3.10+ and LibreOffice, then run:

```text
python Start_Nexus_Office.py
```

Use `python3` if that is your system's command. Use the Office window the launcher opens and keep the launcher window open; closing it stops the helper. The documented helper listens on `127.0.0.1`, uses a per-launch authorization token and an isolated temporary LibreOffice profile, and disables macros and automatic link updates. It belongs to this Office package, not a shared Nexus launcher.

Certificate-based PDF signing requires one-time setup:

```text
python Start_Nexus_Office.py --setup-signing
```

Initial setup needs internet access and installs the pinned signing dependency in this package's private Python environment. Ordinary conversion and signing use local files. The setup is separate from the CPython 3.12 source-package extraction above.

In Writer, **Signature** can insert a drawn, uploaded or optionally saved image and the current local date. This is a visible signature appearance. **Sign and download PDF** instead uses a `.p12` or `.pfx` certificate and private key through the helper to cryptographically sign the current document's PDF. Recipient trust depends on the certificate chain; no trusted timestamp or online revocation check is added. These are different operations. Follow the [documents guide](../releases/6.45.20/docs/OFFICE_DOCUMENTS.md) for setup and handling.

## Compatibility boundaries

- **Originals and edits:** Download original retrieves the imported file. Compatibility view shows the retained PDF, embedded preview or locally converted PDF, not later Nexus edits. Editable import reconstructs supported content and can differ in layout or features.
- **Legacy and Apple files:** conversion depends on the installed local converter. Some Pages files contain an embedded PDF that the browser can preview and use for text import; an image-only preview is incomplete. Other Pages versions need conversion or export from Pages. The hosted site does not supply LibreOffice.
- **Macros:** supported content from macro-enabled files can be imported while retaining the original file separately. VBA, ActiveX and embedded code are not executed. Edited exports do not promise preservation of unsupported program features.
- **PDF limits:** import and preview support up to 300 pages. Scanned PDFs can be viewed, but no OCR is included. Browser printing uses a simplified layout; direct helper PDF export paginates supported DOCX content with LibreOffice. Review output when pagination matters.

## What the evidence establishes

- **Current supplied functional evidence:** 25 browser-document checks, 14 theme checks, 21 Design Studio checks and 9 risk checks, plus 6 successful service checks, 6 source checks and 5 loader cases for revision 6 in Chromium on Linux. The record covers tab isolation and project round trips, retained originals, PDF import/preview, signature appearances, real LibreOffice conversions, current-tab PDF export, PKI signing and service authorization.
- **Test fixtures and limits:** the PKI test uses a self-signed test identity; the Pages fixture is synthetic with a genuine embedded PDF, and the macro fixture contains inert test VBA bytes. These do not establish compatibility with every real-world Apple file, macro program or historical Office format.
- **Retained supplied evidence:** revision-5 theme, Home, Design Studio and risk results, with older aviation, Paint and comparison receipts nested below them. These historical sections are not newly rerun revision-6 results; current suites are listed separately above.
- **[Separate read-only integrity review](PUBLICATION_VERIFICATION_6.45.20.json):** original ZIP/member equality and CRCs, file sizes and SHA-256 hashes, all data parts, payload/source inventories, browser reconstruction and companion-asset paths. No supplied application code or bundled functional suite was executed by that review.

See [RELEASE_VALIDATION.json](../releases/6.45.20/RELEASE_VALIDATION.json) for the supplied test descriptions. Integrity checks do not establish authorship, licensing, complete build reproducibility, real-world document fidelity or cross-platform behavior. Windows and macOS hardware were not exercised. No Radeon performance or physical 4K-monitor qualification is claimed. The aviation records and dates are fictional; generated comparison images are illustrations.

## Permissions and earlier releases

Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Redistribution, modification, production deployment and other commercial use require express written consent. Read the [repository license](../LICENSE), [evaluation permission](../COMMERCIAL_EVALUATION_PERMISSION.md) and [scope](../NEXUS_LICENSE_SCOPE.md). Bundled notices, third-party licenses and previously granted rights remain unchanged.

[Earlier releases](../releases/) remain available with their version-specific files and notices. Their historical hashes and test results should not be used as validation for 6.45.20.
