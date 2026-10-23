# Nexus Office

Documents, spreadsheets, presentations, visual design and dashboards in a local browser application. The **6.45.0 browser trial, packaging revision 1**, carries the same application and assets as the installed 6.45.0 package in one HTML file.

[Open the browser trial](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_0_Browser.html) · [Download the single HTML](Nexus_Office_v6_45_0_Browser.html) · [Full package](releases/6.45.0/) · [Wiki](https://github.com/RDunbar01/Nexus-Office/wiki)

## What it does

- **Writer:** edit documents, use installed templates and prepare a resume from facts you supply, with preview and Undo.
- **Grid:** edit workbooks, use templates, and create charts and tables from bounded cell ranges.
- **Present:** add editable slides from installed layouts using a reviewed creation workflow.
- **Paint and Dashboard:** work with visual layouts, colouring assets and dashboard templates. Imported spreadsheet data is a snapshot, not a live connection.
- **Office commands:** discover supported actions, capture context and fill supported fields with literal values. Review and approval precede edits.

## Try it in your browser

Open the trial link above. The file expands its bundled code and assets locally, then shows the application notice. It needs no server, Python installation, PyTorch backend or CDN to start. You can also save the HTML and open it locally in a supported browser.

Use a current desktop browser with `DecompressionStream('gzip')`, TextEncoder/TextDecoder and Web Crypto. Startup checks these APIs and the embedded data, and reports an error rather than pretending the application loaded. The trial does not guarantee a fixed startup time on every device.

The monolithic HTML is intended to make online evaluation easy: one Pages link opens the application, and one downloaded file contains its code and assets. A reversible dictionary/gzip package keeps the distributed HTML below 20,000,000 bytes without dropping the writing library, clipart or model assets. The expanded application is about 28.9 MB; memory use is higher than the file size. No user document is sent through the application loader.

## Engineering contribution

Developed by **Rich Dunbar / Nexus Emerging Technology with AI-assisted coding**. Office brings five productivity workspaces together and connects their existing editing APIs to bounded commands. The command registry reports available host actions; previews become invalid when inputs change, and Writer edits use the application's transaction and Undo path.

The single-file edition adds a reproducible, integrity-checked delivery format around the existing application rather than a mock interface. Imported documents are handled by the application's existing format code. These are programmed workflows: the included small learned checkpoint remains unqualified and is not enabled as a general-purpose Office agent. The command interface does not run arbitrary macros or shell scripts, generate whole presentations, or invent missing resume facts.

## Full local package

The [6.45.0 package](releases/6.45.0/) remains available unchanged. Keep all installer data files together and follow [INSTALL.txt](releases/6.45.0/INSTALL.txt). **CPython 3.12** is recommended for its optional installer; Python and PyTorch are not required after extraction. The original package's `candidate.html` still needs its two companion libraries. That requirement does not apply to the new single-file browser trial.

## Validation and limits

See [browser build and test details](docs/BROWSER_TRIAL.md) for exact hashes, reconstruction checks and test scope. Existing regressions cover document/workbook operations, format round trips, cancelled imports, command previews and Undo with synthetic data. Browser-native clipboard, drawing, printing and rendering fidelity need testing on the intended device. Microsoft Office fidelity and Windows/Radeon performance are not guaranteed.

[English Wiki](https://github.com/RDunbar01/Nexus-Office/wiki) · [Français](https://github.com/RDunbar01/Nexus-Office/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ko)

## Credits and license

Retain the [third-party notices](NEXUS_Office_v6.7_THIRD_PARTY_NOTICES.md) and library notices embedded in the application. Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Distribution, modification, production deployment and other commercial use require express written consent. Third-party licenses and previously granted rights remain unchanged. See [LICENSE](LICENSE) and the [evaluation permission](COMMERCIAL_EVALUATION_PERMISSION.md).
