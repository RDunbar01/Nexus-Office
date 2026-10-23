# Nexus Office browser trial 6.45.1

[Open the current trial](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_1_Browser.html) · [Build manifest](OFFICE_BROWSER_BUILD.json) · [UI changes](CHANGELOG_6.45.1.md)

## Current delivery and application changes

Version 6.45.1 updates the assistant dock, header and composer, and the responsive Writer ribbon and ruler. These presentation changes are included in both the rebuilt local package and the browser edition. Commands, document formats, model assets and editing capabilities are unchanged.

Writer’s ribbon wraps and grows across the available width. On short screens, a bounded, scrollable tool area preserves document space. All controls remain accessible, but are not necessarily visible at the same time.

The browser builder uses the same reversible dictionary, gzip and ASCII Base85 envelope as the previous edition. It restores the two companion JavaScript libraries inline in their original order, restores the expanded application bytes and verifies their SHA-256 before execution. No application-code download, CDN or companion file is required by the single-file edition. Original libraries, model assets and attribution notices are retained.

Both current editions carry the current evaluation-permission notice. Unlike the previous browser packaging revision, the permission notice is no longer a browser-only difference. The expanded browser edition includes its 6.45.1 end-of-body readiness marker. That marker means parsing reached the end, not that every browser action or model is qualified. The existing application notice still requires acknowledgment.

## Artifact, requirements and checks

The file is `Nexus_Office_v6_45_1_Browser.html`. The stable `NEXUS_Office.html` entry uses the exact same reviewed 6.45.1 browser blob, not a redirect; the versioned 6.45.0 file remains unchanged for rollback. The [current build manifest](OFFICE_BROWSER_BUILD.json) is the authority for this artifact's exact size, hashes, reconstructed byte count, source and vendor hashes. Historical 6.45.0 hashes below do not describe the new file. The distributed HTML must remain below 20,000,000 bytes. Expanded bytes and peak memory are larger; startup retains intermediate decoding buffers.

Use a current desktop browser with `DecompressionStream('gzip')`, TextEncoder/TextDecoder and Web Crypto. Decoding and integrity checks run locally. Missing APIs, invalid data, incorrect lengths, corrupt compression or a reconstruction hash mismatch produce a startup error rather than executing unverified output. Retry handling and concurrent-job protection remain in the loader. Startup time depends on the device.

The application's content security policy and script order are retained. Offline startup does not make remote media or optional connected services available offline. The command interface remains bounded and the included learned checkpoint is not enabled as a qualified general-purpose Office agent.

Validation must identify the exact 6.45.1 artifact. Historical regression counts below are prior-release evidence, not proof that this patch passed. See the current release's validation records for executed reconstruction, UI, format, command and layout checks. Synthetic DOM checks do not establish physical Windows/Radeon performance, browser-native clipboard or printing behavior, or Microsoft Office fidelity.

## Rebuild the current browser edition

Extract the complete 6.45.1 local package. Keep its source `candidate.html` with `source_scripts/092_nexus-writing-writing_vendor.js` and `source_scripts/097_nx-clipart-data.js`. Set `NEXUS_OFFICE_SOURCE` to that source directory and use the matching [browser builder and loader](../tools/office-browser/) with CPython 3.12. Run `python tools/office-browser/build_trial.py`, then its `test_loader.cjs` and `test_base85.cjs` checks with a compatible Node.js runtime. The manifest must match the actual source and output; compression bytes may differ across Python/zlib versions. Do not publish expanded verification copies above the distribution file-size limit.

Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Distribution, modification, production deployment and other commercial use require express written consent. Third-party licenses and previously granted rights remain unchanged. See [evaluation permission](../COMMERCIAL_EVALUATION_PERMISSION.md).

## Historical 6.45.0 packaging-revision-1 record

The record below is preserved unchanged. Its versions, byte counts, hashes, test counts, environment limitations and relative manifest references describe that prior release, not 6.45.1.

# Nexus Office browser trial

Application version: **6.45.0**. Browser packaging revision: **1**.

## What changed

The installed 6.45.0 application is delivered as one HTML file. Its two previously separate JavaScript libraries are restored inline in their original order. A reversible dictionary removes duplicate embedded strings, including strings inside base64 JSON, before gzip compression. An ASCII base85 envelope keeps delivery compact without changing the compressed or reconstructed bytes. The local loader restores every application byte and validates SHA-256 before executing it. No application-code download, CDN or companion file is needed.

The original embedded libraries, models, images, fonts and attribution notices are preserved. The only changes to the expanded application are one current evaluation-permission sentence/link and an end-of-body browser-package marker. The marker indicates parsing reached the end, not that every browser-specific operation or model has been qualified.

The full native package, previous releases and source history remain unchanged. This is a delivery revision, not a new inference engine or a new Office model.

## Artifact and provenance

- File: `Nexus_Office_v6_45_0_Browser.html`
- Distributed HTML: **16,555,013 bytes**, below 20,000,000 bytes.
- SHA-256: `c21e46b99e32c9032f4eacf276441f173e5794347171a659ff2dc4c4cafe999f`
- Baseline repository main: `50c4332214395bc883a98fd5e589a84d927529ee`.
- Fully inlined, unchanged baseline: 28,912,935 bytes; SHA-256 `d0d96baa606f83fef094756482d10de5229d7c178bc4526a1d09b60f9cd290e6`.
- Expanded trial: 28,913,457 bytes; SHA-256 `ab0ddb8912018b2660408b8b256812791b01dbe01ec7efd8adbf6e8206c40049`.

[Machine-readable manifest](OFFICE_BROWSER_BUILD.json) records exact vendor hashes, size limits and presentation deltas. Expanded size is not peak memory usage; startup holds several intermediate buffers and uses more memory than the download size.

## Runtime requirements and failure behavior

Use a current desktop browser providing `DecompressionStream('gzip')`, TextEncoder/TextDecoder and Web Crypto. All decoding is local. Missing APIs, incorrect lengths, invalid reconstruction nodes, corrupt compressed data or a final hash mismatch produce a visible startup error and a retry button instead of executing unverified output. Concurrent retry clicks cannot launch duplicate reconstruction jobs.

The existing application's content security policy and script order are retained. Remote media or explicitly connected local services remain subject to that policy and browser restrictions. Offline startup does not imply that a remote video or an optional connected service works offline. The application notice remains visible until acknowledged; the package does not bypass it.

## Validation scope

The complete production loader was executed against the distributed embedded payload. Tests cover byte-exact reconstruction, unsupported decompression APIs, corrupt data, expansion bounds, successful retry after API restoration and concurrent-click suppression.

The actual compact HTML was also loaded into a DOM test harness, which runs its loader and `document.open/write/close` path rather than substituting the expanded application. All 23 UI smoke checks passed with external resources disabled, including all workspaces, settings, cancellation safety, unavailable controls and Writer content preservation. Ten format round-trip and failure/cancellation checks passed, including DOCX, XLSX, PPTX and NWD. Thirteen integrated command/Writer transaction checks passed, including preview invalidation and exact Undo. These checks ran through the prior base64 envelope; its expanded application is byte-identical to this base85 edition. Five additional full-host lifecycle checks passed, covering stale approvals, cancellation, session limits and disabled learned qualification. Clipboard, canvas and other native browser facilities are mocked in these DOM tests; they do not establish visual fidelity or hardware performance.

Local Chromium could not launch in the test container because its process-singleton socket was denied before any page loaded. That run is **not run**, not a browser pass. Browser-native testing, Windows/Radeon qualification, clipboard, printing and rendering need separate verification. Microsoft Office fidelity is not guaranteed.

## Rebuild

Use the unchanged full 6.45.0 package to obtain its source directory containing `candidate.html` and `source_scripts/092_nexus-writing-writing_vendor.js` and `source_scripts/097_nx-clipart-data.js`. Keep that directory outside the published browser output. The source candidate's SHA-256 must match the manifest before rebuilding.

The builder and loader are in [tools/office-browser](../tools/office-browser/). Set the `NEXUS_OFFICE_SOURCE` environment variable to the extracted source directory, then run `python tools/office-browser/build_trial.py` with CPython 3.12. The builder uses standard-library modules only. After rebuilding, run `node tools/office-browser/test_loader.cjs` with a current Node.js version supporting the same decompression and Web Crypto APIs. Run `node tools/office-browser/test_base85.cjs` for the independent codec edge cases. It writes its output under that tool directory's `dist`, plus local verification copies and a manifest. Do not publish those expanded verification copies: each exceeds the distribution file-size limit.

Compression output can differ across Python/zlib versions, so always record the generated manifest. Restored application bytes and their integrity hashes must remain exact. The existing full-package installer is separate from this browser packaging step.

## Permission

Personal use and internal commercial testing and evaluation of Nexus-owned material are permitted. Distribution, modification, production deployment and other commercial use require express written consent. Third-party licenses and earlier grants remain unchanged. See the root [evaluation permission](../COMMERCIAL_EVALUATION_PERMISSION.md) and retained third-party notices.
