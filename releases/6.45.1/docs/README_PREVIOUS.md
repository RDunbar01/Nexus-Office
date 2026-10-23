# NEXUS Office Suite

## Created with AI-assisted coding

**Developed by Rich Dunbar · Actively developed · Proof of concept**

I am developing NEXUS Office using **AI-assisted coding** as part of my main project, **Nexus OS**. I direct the application's goals and design, using AI to assist with implementation, debugging and refinement.

### Built to make Nexus OS more useful

Nexus OS is built around a **custom bare-metal kernel**. To become a practical workstation, it needs a suite of applications that make everyday work possible.

NEXUS Office is part of that effort: a custom productivity suite for documents, spreadsheets, presentations, visual work and data. Its purpose is to add usability to the wider Nexus OS project and support the development of a self-contained offline workstation.

### Current stage: a working proof of concept

This version demonstrates the concept and provides a foundation for further development. **It is not yet a reliable daily-use office suite.**

I estimate that it is **at least 200 further development iterations away** from the level of reliability I want for everyday office work. That is my development estimate, not a guaranteed completion threshold or release date. Readiness will depend on demonstrated reliability, testing and feedback.

> [!IMPORTANT]
> **NEXUS Office is actively being developed.**
> Use this release for experimentation and evaluation. Keep original documents and independent backups, and verify exported files before relying on them.

### Cross-platform compatibility is the goal

My intent is to support office workflows across **macOS, Windows and Linux**, so documents created on those systems can also be opened and used within Nexus OS.

The long-term destination is a **secure, offline Nexus OS workstation** with useful, interoperable applications. Document compatibility, content preservation, dependable saving and consistent rendering are central to that goal.

| Area | Current position |
| --- | --- |
| **Development** | Active, AI-assisted development |
| **Maturity** | Proof of concept; substantial work remains |
| **Daily-use readiness** | Not yet established |
| **Cross-platform goal** | Work with documents across macOS, Windows, Linux and Nexus OS |
| **Format fidelity** | Limited, feature-specific support; not full Office-suite parity |
| **Security** | Offline-workstation design goal; no security certification claimed |

Browser compatibility and document-format compatibility are separate requirements. The current release does not establish support for every browser, device, file format or advanced document feature.

---

**A browser-native, local-first productivity workspace**  
**Release:** v6.7 · **Build:** GitHub documentation and import-reliability repair · **Maintainer:** NEXUS Emerging Technology

> **Project status — actively developed proof of concept.** NEXUS Office is an independent productivity application, not Microsoft Office, LibreOffice, or a validated drop-in replacement. This repository contains its browser application and technical documentation. No LLM weights or NEXUS Foundry backend are bundled.

![NEXUS Office home screen](assets/nexus-office-home.png)

NEXUS Office combines **Writer, Grid, Present, Paint/Design, Data and Whiteboard** in a single HTML application. It also provides calendar and source-code tools, chart and dashboard design, local saving and recovery, and several office-document interchange formats. Its user interface is written in embedded HTML, CSS and JavaScript, so the core application does not require a Node.js server, Python package, API key or cloud office account.

### At a glance

| Attribute | Implementation |
| --- | --- |
| Application | Single standalone `NEXUS_Office_v6.7.html` |
| Primary runtime | Modern desktop browser; Chromium / Microsoft Edge recommended |
| Processing | Browser JavaScript, DOM, Canvas, storage, file APIs |
| Persistence | Downloaded files; browser IndexedDB autosave; optional File System Access binding where supported |
| Office interchange | DOCX, XLSX, PPTX, and bounded ODT/ODS/ODP support |
| Optional integration | NEXUS Foundry via a separately operated loopback service or native bridge |
| Bundled third-party JavaScript packages | None identified in the audited single-file source |
| Software license | **Not supplied for NEXUS-owned code**; see [Licensing](#licensing-and-third-party-attribution) |

## Contents

- [Created with AI-assisted coding](#created-with-ai-assisted-coding)
- [Built to make Nexus OS more useful](#built-to-make-nexus-os-more-useful)
- [Current stage: a working proof of concept](#current-stage-a-working-proof-of-concept)
- [Cross-platform compatibility is the goal](#cross-platform-compatibility-is-the-goal)
- [Quick start](#quick-start)
- [Applications](#applications)
- [Supported file formats](#supported-file-formats)
- [Saving and recovery](#saving-and-recovery)
- [Optional NEXUS Foundry integration](#optional-nexus-foundry-integration)
- [Debugged release and tests](#debugged-release-and-tests)
- [Security and privacy](#security-and-privacy)
- [Known limitations](#known-limitations)
- [Project files](#project-files)
- [Licensing and third-party attribution](#licensing-and-third-party-attribution)

## Quick start

1. Download or clone this repository.
2. Open **`NEXUS_Office_v6.7.html`** in an up-to-date Microsoft Edge or Chromium browser.
3. Select **Writer**, **Grid**, **Present**, **Paint**, **Data**, or **Whiteboard** from the navigation rail. Calendar and Code tools are available within the appropriate Writer/Grid ribbons.
4. Use **Open** to import a supported local file. Use **Save** for the active application's primary format, or **Export** to choose another format.
5. Save a native **`.nxo`** workspace copy if you need to preserve NEXUS-specific multi-tool data and features that external formats cannot reproduce.

A local static server may improve browser-origin handling, especially for IndexedDB or file-system features. From the repository directory, if Python is already installed:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/NEXUS_Office_v6.7.html>. This command serves the static HTML file **only**; it is not an office-processing backend and is not the optional Foundry service. Avoid hosting the application or documents on untrusted public servers.

## Applications

| Workspace | Features in this release |
| --- | --- |
| **NEXUS Writer** | Rich-text editing; headings, lists, tables, images, layout and print controls; review/comments and track-changes tools; DOCX, PDF, RTF, HTML, Markdown and text exports |
| **NEXUS Grid** | Multi-sheet workbooks, formulas, common analytic functions, cell styling, charts, conditional formatting, filters, data validation, calendar tools and XLSX/CSV/ODS workflows |
| **NEXUS Present** | Editable slide objects, text, images, tables, shapes, themes, presentation mode and PPTX/ODP/HTML/PDF/image outputs |
| **NEXUS Paint / Design** | Raster drawing, image editing, crop/resize/rotation, effects, local images, design templates and common image exports |
| **NEXUS Data** | Local tables and records, typed fields, schema/validation tools, CSV/TSV/JSON interoperability and reporting |
| **NEXUS Whiteboard** | Moveable notes and objects, connectors, freehand annotations, embedded visuals and PNG export |
| **Calendar / Code** | Date insertion and linked calendar tools; source-code open, inspection and editing inside Writer's Code workspace |
| **Visual tools** | Chart Studio, templates, dashboards, layout elements, clip art, presentation design and constrained NEXUS automation commands |

**AI status:** An optional Foundry launch/bridge is present, but this HTML does not itself bundle a trainable LLM, a model-inference engine or a Foundry backend. In particular, opening this HTML alone does not start an AI model.

## Supported file formats

Support is **feature-specific**, not full binary or visual parity with commercial office suites. Complex layout, formulas and imported objects can be simplified or omitted.

| Workspace | Principal imports | Principal exports |
| --- | --- | --- |
| Writer | DOCX, ODT, TXT, RTF, HTML, Markdown | DOCX, ODT, PDF, RTF, HTML, Markdown, TXT |
| Grid | XLSX, ODS, CSV, TSV and compatible structured data | XLSX, ODS, CSV, TSV, JSON, PDF |
| Present | PPTX, ODP | PPTX, ODP, HTML slideshow, PDF, PNG/JPEG/SVG, notes |
| Paint | Common raster image files | PNG, JPEG, WebP, BMP, TIFF, SVG/PDF representations |
| Data | CSV, JSON and common tabular text | CSV, TSV, JSON, HTML, PDF |
| Workspace | Native `.nxo` state | Native `.nxo` state |

A native NEXUS workspace preserves more application-specific state than an external interchange document. **Always retain an original copy** of an important DOCX, XLSX or PPTX and check the exported result in its destination application before relying on it. XML package validity and successful re-import do not prove perfect formatting fidelity.

Some PDF and SVG exports are image-based or contain embedded raster images; do not assume exported text is selectable or that all SVG contents remain vector-editable. Office macros, ActiveX, SmartArt, advanced animations, external connections and other unsupported proprietary features are not executed or faithfully reproduced.

## Saving and recovery

- **Save** downloads the current workspace's primary format (for example, Writer → DOCX and Grid → XLSX); the browser may choose a download filename and location.
- **Export** provides alternate interoperable formats and the native `.nxo` format.
- **Autosave** uses browser storage, including IndexedDB. An autosave can be restored through the recovery controls when available in the same origin/browser profile.
- **Optional direct-to-file saving** relies on a compatible browser's File System Access API and user-granted file permissions. It is not supported uniformly in every browser or direct-file context.
- Autosave is **not** a substitute for independent saved copies. Clearing site data, private-browsing limits, changing browsers/origins or storage quota failures can remove recovery state.

## Optional NEXUS Foundry integration

The NEXUS Wheelhouse section provides a launcher and status probe for a separately operated Foundry runtime. Its fallback endpoint is `http://127.0.0.1:8765`, including an `/api/health` check. The corresponding Foundry server, dependencies, and any model weights are **not included** here.

The Office application is local-first, **not a blanket guarantee of zero network connections**: its content security policy permits selected YouTube/Vimeo media frames and local loopback connections for integrations. If absolute offline operation is required, do not activate external media or optional services, and audit the deployment/browser configuration.

## Debugged release and tests

This repository includes the **repaired** v6.7 HTML file and an unchanged source snapshot under [`archive/`](archive/). The repair was limited to file interoperability and import safety; it does not claim to solve every user-interface or compatibility issue.

### Changes in the repaired HTML

1. **Deflated ZIP import deadlock fixed:** the ZIP decompressor now drains output concurrently with compressed input, resolving the observed hang when importing DEFLATE-compressed Office archives.
2. **Archive integrity checks:** import rejects invalid uncompressed lengths, CRC-32 mismatches, duplicate ZIP entries and unsupported encrypted ZIP entries.
3. **OOXML relationship targets:** normalized absolute and relative package-part paths for DOCX media, XLSX worksheets and PPTX images.
4. **Native workspace Writer HTML:** `.nxo`/compatible JSON restoration now removes active script/event-handler markup and untrusted embeds from imported Writer content, while allowing selected local embedded images and trusted video frames. This is **not** a comprehensive security sandbox for every possible NEXUS object field.
5. **Open-dialog routing:** native Office/data/workspace formats take priority over automatic source-code viewing even if the operating system reports a text/JSON MIME type. Use **Open source code** explicitly for code inspection.

### Executed checks

| Check | Result |
| --- | --- |
| JavaScript syntax, all 19 embedded scripts | Passed |
| Chromium application startup | Passed; no uncaught startup exceptions |
| Grid SUM/IF/arithmetic, cycle detection and cross-sheet reference samples | Passed |
| DOCX, XLSX and PPTX sample archive/XML generation | Passed |
| Import of DEFLATE-compressed DOCX, XLSX and PPTX samples | Passed |
| XLSX relationship with absolute `/xl/...` target | Passed |
| ODT, ODS and ODP sample exports and compressed imports | Passed |
| Deliberately invalid ZIP CRC and declared length | Rejected as expected |
| Malicious Writer HTML inside a native `.nxo` import | Script/event payload removed in test |
| Writer PDF generation and PDF rendering | Passed on sample document |

These are **software-level smoke and regression tests on synthetic/sample content**, not certification of real-world Microsoft Office fidelity, accessibility, large files, sustained performance or hardware-specific File System Access behavior. See [TESTING.md](TESTING.md) for methods and coverage gaps.

## Security and privacy

The file import layer applies size and path checks to ZIP packages and sanitizes supported Writer HTML content. Spreadsheet formulas use an allowlisted parser rather than arbitrary JavaScript evaluation. Some suite automation syntax resembles JavaScript, Basic or Java, but these are **limited NEXUS command subsets**, not execution of arbitrary Office VBA or Java programs.

The HTML is a local application and has **no built-in authentication, central audit service, malware scanner or enterprise security certification**. Treat imported files, macros and media as untrusted. Do not publish `.nxo` documents or autosave data containing sensitive material. Review [TESTING.md](TESTING.md) before production use.

## Known limitations

- Not at feature, format, accessibility or performance parity with Microsoft Office/LibreOffice.
- Complex Office format constructs and real-world compatibility matrices remain unverified.
- Certain UI controls and modern browser APIs depend on the chosen browser, origin and user permissions.
- Imported Office macros and unsupported embedded code are not executed.
- The built-in PDF generator may rasterize page content; export is not a substitute for specialist print production.
- Auto recovery depends on browser-local storage; full disaster recovery is not guaranteed.
- The Foundry integration requires a separate runtime; no AI model is embedded.
- This release was not subjected to a comprehensive independent security audit.

## Project files

```text
NEXUS_Office_v6.7.html             # Repaired standalone browser app; open this
README.md                          # GitHub home page and usage guide
THIRD_PARTY_NOTICES.md             # Attribution, standards and provenance scope
CHANGELOG.md                       # Specific fixes and retained limitations
TESTING.md                         # Tests and gaps
assets/nexus-office-home.png       # Actual Chromium-rendered application image
archive/Nexus_Office_v6.7_Original.html  # Unmodified uploaded source snapshot
```

## Licensing and third-party attribution

The single HTML source contains **no identifiable bundled third-party JavaScript framework, library or CDN package**. NEXUS uses browser-provided HTML/JavaScript APIs and independently packaged document-format handling. The source scan cannot prove the historical origin of every algorithm or fragment; any confirmed external contribution must be documented with its own copyright and license.

See [**THIRD_PARTY_NOTICES.md**](THIRD_PARTY_NOTICES.md) for specific credit to document-format standards, browser specifications, external platforms and optional font fallbacks, clearly distinguished from third-party code distributed in this repository.

**No license for NEXUS-owned source code was included in the supplied file.** Publishing source on GitHub does not itself make it Apache-2.0, MIT or public domain. Add an explicit `LICENSE` only after the repository owner selects its terms and clears any additional third-party provenance obligations.

---

**NEXUS Emerging Technology** · Experimental research and software engineering · 2026
