# Nexus Office 6.45.4

A local-first productivity application for documents, spreadsheets, presentations, visual work and dashboards.

[Open Nexus Office in your browser](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_4_Browser.html) · [Download the single HTML](Nexus_Office_v6_45_4_Browser.html) · [Full local package](releases/6.45.4/)

## Current release

Version 6.45.4 introduces a redesigned Home workspace with six cards: Writer, Grid, Dashboard Studio, NexusPoint, Paint and Compatibility. Native text, CSS and SVG graphics adapt the layout from narrow windows to 4K desktops. Home retains command search and the existing Open action.

The Assistant dock, Home card and launch button are no longer shown, and automatic Assistant opening is disabled. Recent document names are also removed from Home. Documents, stored history, existing launch actions and the 6.45.3 Writer ribbon remain intact; hiding these panels does not delete their underlying data or modules.

## Try it now

The Pages link opens the actual single-file application, not a mock-up. Acknowledge its application notice to continue. No Python, PyTorch backend, server or CDN is needed to start the browser edition.

Use a current desktop Chromium browser with `DecompressionStream('gzip')`, TextEncoder/TextDecoder and Web Crypto. The loader checks its embedded data before execution and reports unsupported APIs or corrupt data. Startup time depends on the device and connection; a fixed ten-second launch is not guaranteed.

The monolithic HTML makes online trials straightforward: one link opens the application, and one saved file contains its code and assets. Lossless dictionary/gzip/Base85 packaging keeps the delivered HTML at **16,572,073 bytes**, below 20 MB. The expanded application is about 29 MB, and runtime memory use is higher. The loader does not upload user documents.

## Workspaces

- **Writer:** document editing, templates, formatting and existing import/export workflows. All 223 Writer ribbon controls are retained in this release.
- **Grid:** workbooks, formulas, charts and tables.
- **NexusPoint:** presentation editing and existing slide layouts.
- **Paint and Dashboard Studio:** visual work, colouring assets and dashboard templates. Imported spreadsheet data is a snapshot, not a live connection.
- **Compatibility:** access the existing compatibility information and workflows.

Developed by **Rich Dunbar / Nexus Emerging Technology with AI-assisted coding**. The engineering contribution is a locally usable productivity suite with a self-contained, integrity-checked browser distribution. The included learned checkpoint remains unqualified; this release does not claim a general-purpose autonomous Office agent or new inference performance.

## Full local package

The [6.45.4 package directory](releases/6.45.4/) contains the exact delivered installer, manifest and three numbered data files. Download all of them together and follow [INSTALL.txt](releases/6.45.4/INSTALL.txt). Each data file is at most 10,000,000 bytes, and every individual distributed component is below 20,000,000 bytes.

The complete Library download is named `Nexus_office_6.45.4_Full.zip`. Its SHA-256 is `19aa2a783e4b8a6096ad9d67f2d15fb19b7be00a3ec85fde82d5eb4b1df1e238`. The complete ZIP is larger than 20 MB; Git supplies its components separately. Do not mix releases.

**Standard CPython 3.12** is recommended for the optional installer. It creates a version-isolated folder and verifies checksums without global dependency changes or downloads. Python and PyTorch are not required after extraction. Keep the installed `candidate.html` with its `source_scripts` directory; the standalone browser HTML already embeds its companion libraries.

Existing browser state is not automatically migrated. Export documents from the old edition and import them into the new one when needed, keeping the originals. Published [6.45.2](releases/6.45.2/), [6.45.1](releases/6.45.1/) and [6.45.0](releases/6.45.0/) files remain unchanged for rollback and historical comparison.

## Evidence and limits

See [release changes](releases/6.45.4/docs/CHANGELOG_6.45.4.md), [delivered validation records](releases/6.45.4/RELEASE_VALIDATION.json) and [browser artifact details](docs/BROWSER_TRIAL.md). The delivered records report Home and Writer integration checks on both editions in headless Chromium on Linux, including an actual 3840 × 2160 capture. These are scoped checks, not a guarantee of every document or device.

Physical Windows/Radeon behavior, OS clipboard, printing and other browser engines were not tested by those records. Microsoft Office fidelity and hardware performance are not guaranteed. The prior Writer implementation guide remains included for the ribbon; its Assistant-layout guidance is superseded by 6.45.4.

## License and credits

Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Distribution, modification, production deployment and other commercial use require express written consent. Third-party licenses and previously granted rights remain unchanged. See [LICENSE](LICENSE), the [current repository evaluation permission covering 6.45.4](COMMERCIAL_EVALUATION_PERMISSION.md), and [scope](NEXUS_LICENSE_SCOPE.md) and [third-party notices](NEXUS_Office_v6.7_THIRD_PARTY_NOTICES.md). Retain the notices embedded in the application.

The delivered package is preserved byte-for-byte. Its enclosed supplemental version list predates 6.45.4; the current repository permission explicitly covers this release. This publication does not rewrite the package license files.
