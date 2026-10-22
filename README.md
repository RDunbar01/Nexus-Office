# Nexus Office

## Current release licensing

This Nexus release is not offered under Apache License 2.0. Nexus-owned software may be used only for personal, non-commercial purposes. Any other use, including commercial use, modification or redistribution, requires express written consent from the rights holder. Third-party code, models, datasets and separately licensed components retain their own licenses and notices. Previously granted rights and rights that cannot lawfully be restricted remain unchanged.


> Draft next-release staging: the reviewed installer and complete data-part set are included below. This branch is not a published release or live deployment; the pull request remains draft.

**6.45.0 · next-release package staging · not a published application update**

Experimental local productivity suite for documents, spreadsheets, presentations, visual work and data.

## Current baseline and release status

The staged package advances to **6.45.0**, with active application and package version labels normalized. Historical documentation is retained separately.

The latest audited source retains 183 original script blocks/assets and includes reviewed, bounded command workflows. It does not turn the failed small learned checkpoint into a qualified language model. Document writes require the application review/approval controls. Native Microsoft Office rendering, printing and Windows hardware are not validated by CPU round-trip tests.

## Install the staged package

Download all files in [releases/6.45.0](releases/6.45.0), retaining the directory structure. Keep Nexus_office_Data_001.nxd, Nexus_office_Data_002.nxd and Nexus_office_Data_003.nxd together with package_manifest.json and [installer.py](releases/6.45.0/installer.py). Each data part is at most 10,000,000 bytes. With Python already installed, run python installer.py and review its local-only installation plan before confirming. Use --no-launch to extract without opening the app. The installer extracts the application HTML and local libraries into a new version-isolated directory; keep those files together. See [INSTALL.txt](releases/6.45.0/INSTALL.txt). No live browser deployment is created.

Independent package review verified the complete inventory, hashes, licensing notices and isolated no-launch installation/extraction. This does not qualify native Windows execution, physical hardware or Microsoft Office rendering.

## Start and inspect the original project

Use the exact launch instructions accompanying the matching release package. The [preserved previous README](docs/README_PREVIOUS.md) contains the original workflow, research citations, credits, downloads and limitations. Treat its release-specific statements as historical; this staged update does not silently replace its software or relicense dependencies.

## Evidence and licensing

Developed by Rich Dunbar / Nexus Emerging Technology with AI-assisted coding. Retain existing licenses, attribution and third-party notices. No additional Windows, physical GPU, device-write or model-quality qualification is claimed by this documentation refresh. No live browser-trial deployment is created by this README.
