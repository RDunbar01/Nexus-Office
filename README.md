# Nexus Office

Local browser-based tools for documents, spreadsheets, presentations, visual design and dashboards. Version **6.45.0** combines the five workspaces with installed templates and a command layer that previews changes before asking for approval.

[Download 6.45.0](releases/6.45.0/) · [Installation instructions](releases/6.45.0/INSTALL.txt) · [Package manifest](releases/6.45.0/package_manifest.json)

## What it does

- **Writer:** edit documents, choose installed templates and prepare a resume from explicitly supplied facts, with a full preview and Undo.
- **Grid:** work with spreadsheets and templates; create charts and tables from bounded existing cell ranges.
- **Present:** add an editable slide from an installed layout through a reviewed creation workflow.
- **Paint and Dashboard:** use social-design layouts, a colouring gallery and dashboard templates; imported spreadsheet data is a snapshot, not a live connection.
- **Office commands:** discover available actions, select captured context and fill supported existing fields with literal values. Edits require separate review and approval.

## Engineering contribution

Developed by **Rich Dunbar / Nexus Emerging Technology with AI-assisted coding**. The project brings local productivity workspaces together and connects their existing editing APIs to bounded commands. The command registry reports what the installed host can actually do; previews are invalidated when inputs change, and Writer edits use its existing transaction and Undo path.

These are programmed workflows. The included small learned checkpoint has not passed qualification and is not enabled as a general-purpose Office agent. The command interface does not run arbitrary macros, shell commands or scripts, generate whole presentations, or invent missing resume facts.

## Start locally

1. Download every file in [releases/6.45.0](releases/6.45.0/), preserving the directory structure. Keep `Nexus_office_Data_001.nxd`, `Nexus_office_Data_002.nxd`, `Nexus_office_Data_003.nxd`, `package_manifest.json` and `installer.py` together.
2. With **CPython 3.12** installed, run `python installer.py`. Review the local installation plan before confirming. Add `--no-launch` to extract without opening the application.
3. Open the extracted `candidate.html` in a modern desktop browser. Keep its `source_scripts` folder beside it, including `092_nexus-writing-writing_vendor.js` and `097_nx-clipart-data.js`.
4. Open the Office Assistant and ask **Office commands** to inspect the available actions, or **I need a professional resume template** to try the reviewed Writer workflow with sample facts.

The application needs **neither Python nor PyTorch** after extraction. Python 3.12 is recommended for the optional installer, not a tested guarantee for every Python version. Rebuilding with `build.py` needs Python 3.10 or newer.

This release is a local HTML package, not a self-contained hosted trial. The companion libraries are required; the historical root `NEXUS_Office.html` is not the 6.45.0 package entry point. Each distributed file is below 20,000,000 bytes and each installer data part is at most 10,000,000 bytes.

## Validation and limits

The package includes source-hash records and regression checks using synthetic data, pinned jsdom 26.1.0 and the installed Writer transaction/Undo APIs. Package review also checked inventory, hashes and isolated no-launch extraction. These checks do not establish Microsoft Office rendering fidelity, printing, exhaustive browser visual acceptance or native Windows/GPU compatibility. See the extracted `RELEASE_VALIDATION.json` and `qualification/` records for scope.

The [historical README](docs/README_PREVIOUS.md) preserves earlier design notes and references. Its version-specific claims do not describe every current workflow.

## Credits and license

Retain the [third-party notices](NEXUS_Office_v6.7_THIRD_PARTY_NOTICES.md) and the notices included with the extracted libraries.

Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Distribution, modification, production deployment and other commercial use require express written consent. Third-party licenses and previously granted rights remain unchanged. See the [license](LICENSE) and [evaluation permission](COMMERCIAL_EVALUATION_PERMISSION.md).
