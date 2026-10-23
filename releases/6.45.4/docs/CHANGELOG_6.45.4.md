# Nexus Office 6.45.4 — Modern Home workspace

Home now fills the available screen with a clean navy sidebar, a white header and six balanced cards: Writer, Grid, Dashboard Studio, NexusPoint, Paint and Compatibility. A clear heading, consistent typography and restrained app colors replace the previous nested panels. Document editing controls appear in their respective apps; Home keeps command search and the existing Open action.

The Assistant dock, Home card and launch button are removed from the visible GUI. Its automatic opening is disabled, and explicit calls to its UI opener respect the hidden configuration. The underlying model and command modules remain intact. Recent document names are removed from the Home layout. The hidden legacy save target remains inert so existing save code continues to work; documents and stored history are not deleted.

## Display behavior

The interface uses native text, CSS and vector SVG artwork. It was rendered and checked at a native 3840 × 2160 viewport; the accompanying PNG is an actual capture of the working standalone HTML at that resolution. No enlarged screenshot or bitmap UI is used inside the app.

Three columns and two rows fill standard large desktop screens. Two columns support smaller windows, and one column supports narrow mobile widths. The sidebar becomes a horizontally scrollable navigation strip below 760 pixels. Narrow or short screens scroll vertically without clipping actions. At 1600 × 900, 1920 × 1080, 2560 × 1440 and 3840 × 2160 all six cards fit without vertical scrolling.

## Implementation

- `tools/office-layout/home.js` builds the Home presentation around the six original buttons, retaining their existing handlers. Decorative previews are hidden from assistive technology; launch buttons retain descriptive accessible labels.
- `home.css` scopes the redesigned shell to Home and hides the Assistant controls. Existing editor layouts retain their own sizing rules.
- `apply_home.py` applies the change to a separate copy of the validated 6.45.3 source, adds module 184, updates product labels, and guards Assistant opening in modules 127 and 142.
- `test_home.cjs` exercises card bounds, text clipping, launch routing, compatibility, file selection, keyboard navigation and Assistant suppression. The existing ribbon integration suite covers all original Writer controls and selection-aware editing.

Rebuild with `python tools/office-layout/apply_home.py BASELINE OUTPUT`, where BASELINE is the extracted 6.45.3 source. Set `NEXUS_OFFICE_SOURCE=OUTPUT` and run the existing browser builder. See `tools/office-layout/README.md` for test environment variables.

## Validation

Nine Home checks and thirteen Writer checks passed on each edition: 44 real-browser integration checks in total. Six source/build checks passed, including syntax for all executable modules, exact preservation of the two companion libraries, and an isolated reproducible build. The standalone loader passed exact reconstruction, failure, retry and Base85 tests. Detailed results identify the exact application hashes.

Screenshots of the desktop, 4K and mobile layouts were visually inspected. Tests use synthetic content in headless Chromium 153 on Linux. Physical Windows display behavior, OS clipboard, printing and Radeon performance were not tested. Historical receipts retained in the source package describe their original builds.

The 6.45.3 Writer implementation guide remains included for that ribbon. This changelog describes the new Home screen and supersedes its earlier Assistant-layout guidance. Repository publication is separate from creation of these local release artifacts.
