# Nexus Office themes

Nexus Office 6.45.20 revision 5 includes ten visual themes. **01 — Porcelain** is the default for a browser without a saved theme choice.

## Choose a theme

1. Open **Settings** in the shared left navigation.
2. Find **Office themes** at the top of Settings.
3. Select a theme card or use **Applied theme**. The appearance changes immediately.
4. Select **Home** to view the full composition. Use **Reset to Porcelain** to restore the default.

| Theme | Character | Home composition |
| --- | --- | --- |
| 01 — Porcelain | White, teal, sculptural app artwork | Three columns, two rows |
| 02 — Architect | Cool blue, precise edges | Two columns of horizontal panels |
| 03 — Chromatic Gallery | Rich, distinct app colours | Three columns of artwork cards |
| 04 — Editorial | Ivory, fine rules, serif headings | Open editorial grid |
| 05 — Crystal | Pale glass, cyan and lavender | Luminous translucent cards |
| 06 — Midnight Atelier | Deep navy and jewel tones | Dark gallery with lit artwork |
| 07 — Swiss | Strong typography and vermilion accents | Minimal horizontal modules |
| 08 — Soft Modern | Warm stone and muted natural colours | Soft rounded gallery |
| 09 — Panorama | Airy, tall app galleries | Six columns on wide screens |
| 10 — Aurora | Pearl gradients and translucent artwork | Asymmetric bento grid |

Layouts adapt to narrower windows. The shared navigation stays in place across applications. All title bars remain white, including the embedded Dashboard title bar. Dashboard navigation uses a separate secondary palette.

## What changes

Themes style Home, shared navigation, ribbons and control accents, editing workspace backgrounds, Settings, and the supported application panels. The Home pictures are decorative; app labels, launch actions and theme controls remain real HTML elements with keyboard access.

Theme selection does not change Writer formatting, spreadsheet data, authored slide colours, Paint objects, dashboard data or risk-map bands. Document and presentation design themes remain separate authoring features.

The choice is saved in this browser and origin, and synchronizes with other tabs at that origin. A different browser, profile or file location may use a separate preference. If browser storage is blocked, themes still work for the session and Settings explains that the choice could not be saved. Unknown saved theme IDs revert to Porcelain.

## Open offline

Extract the complete browser ZIP and open `Nexus_Office_v6_45_20_Browser.html`. Keep `theme_assets` and `comparison_assets` beside it. No server is required. Missing theme pictures fall back to built-in vector previews; themes and launch actions still work. The source installer includes the same assets.

The artwork uses the ten approved image concepts. Crystal and Aurora include clean illustration atlases derived from their concepts. The PNGs remain at their original generated resolution; interface typography, controls and layout scale independently through 4K.

## Implementation

- `themes.js`: theme catalog, scoped CSS tokens, Settings gallery, local preference persistence, artwork viewports, and same-origin Dashboard bridge.
- `themes.css`: first cascade layer, screen-only chrome selectors, responsive Home compositions and accessibility rules.
- `themes-dashboard.css`: embedded Dashboard chrome; authored chart surfaces and risk colours remain separate.
- `apply_themes.py`: adds source module 191 to a revision 4 source tree and includes the companion artwork.
- Preference key: `nexus.office.visualTheme.v1`. No document-state or undo-history writes are made by the theme API.
- Public API: `NXOfficeThemes.list()`, `NXOfficeThemes.status()`, and `NXOfficeThemes.apply(id)`.

Validation covers every theme from 320-pixel mobile layouts through 3840 × 2160, native and packaged browser builds, persistence, keyboard selection, fallback behaviour, app routing and authoring invariants in Chromium on Linux. Windows and physical display qualification are outside this validation.
