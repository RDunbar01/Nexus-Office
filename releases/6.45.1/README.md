# Nexus Office 6.45.1

The complete download is `Nexus_office_6.45.1_Full.zip`. Extract the entire ZIP together. Keep `installer.py`, `package_manifest.json` and all numbered `.nxd` parts in their supplied layout. Do not mix releases.

Run `python installer.py` with standard 64-bit CPython 3.12. Review the installation plan before confirming. The manifest supplies the package checksums and installation layout. Data parts are at most 10,000,000 bytes and individual distributed components are below 20,000,000 bytes; the complete ZIP and reconstructed application may be larger.

After extraction, the local application does not require Python or PyTorch. Keep candidate.html with its two companion libraries. The separate single-file browser edition embeds those assets.

[Current overview and browser trial](https://github.com/RDunbar01/Nexus-Office#readme) · [UI changes](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/CHANGELOG_6.45.1.md)

Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Distribution, modification, production deployment and other commercial use require express written consent. See LICENSE and COMMERCIAL_EVALUATION_PERMISSION.md. Third-party licenses and previously granted rights remain unchanged.

This UI patch does not change the engine, add model compatibility or establish physical Windows/Radeon qualification. See the matching release validation evidence for checks actually performed.
