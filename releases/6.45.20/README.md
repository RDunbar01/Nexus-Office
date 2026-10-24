# Nexus Office 6.45.20 revision 6

Writer and Paint now include bottom document tabs, double-click renaming and collective project save. Paint Clear affects only the active sheet; image export uses only that sheet. Writer supports multiple opened documents and `.nxwriter` projects. Sheets tabs now rename inline on double-click through the existing reference-aware rename backend.

PDF import and original-layout viewing use a bundled local PDF runtime. Imported originals are retained for download and compatibility previews. The optional Office-only local helper adds legacy/cross-platform conversion through LibreOffice and direct paginated PDF export. Macro-enabled files can expose supported content while retaining their originals; VBA and ActiveX do not run. Format and fidelity limits are explained in `OFFICE_DOCUMENTS.md`.

Writer can insert drawn, uploaded or saved signatures with the current date, and export a cryptographically signed PDF using a PKCS#12 identity through the local helper. Signature appearances are clearly distinguished from PKI signing. Certificate passwords are not stored in documents.

All ten themes, the Paint template catalogue and aviation heat maps remain available. See `OFFICE_DOCUMENTS.md` for setup, file formats and usage. The older Word guide is still the revision 3 guide.

# Nexus Office 6.45.20 revision 5

Ten complete Office themes are now integrated, with **01 — Porcelain** applied by default: Porcelain, Architect, Chromatic Gallery, Editorial, Crystal, Midnight Atelier, Swiss, Soft Modern, Panorama and Aurora.

Open **Settings → Office themes** to choose from the visual gallery or accessible selector. The choice applies immediately, persists in local browser storage, and synchronizes with other open tabs at the same origin. Reset to Porcelain is available. Invalid stored choices fall back to Porcelain; blocked storage keeps the choice for the current session.

Each theme includes its Home composition, app artwork, palette, navigation treatment, control accents and editing-panel styling. The white top bars remain consistent, including Dashboard Studio. The Dashboard secondary rail remains distinct from the Office rail. Writer pages, spreadsheet cells, slide contents, Paint layers and dashboard data are not changed by theme selection.

The new theme module and screen-only styles are isolated from the existing authoring engines. Twelve PNG artwork assets ship in `theme_assets`; keep that folder beside the HTML. Missing artwork falls back to the built-in vector previews. All text and launch controls remain native HTML. See `OFFICE_THEMES.md` for use, implementation and validation scope. The included Word guide remains the revision 3 functional guide.

# Nexus Office 6.45.20 revision 4

Home now uses six horizontal app panels in a balanced two-column layout. The Local workspace badge and One workspace. Endless possibilities. slogan are removed. A compact Your workspace heading, short descriptions, slim line icons and muted accents give the main page a quieter appearance. All existing app launch actions, Open, Compatibility, keyboard access and Settings navigation remain available.

The layout adapts from 320-pixel screens to 3840 by 2160. Only Home JavaScript and CSS changed. The aviation dashboard, live heat maps, Paint templates, photos and editing backends are byte-identical to revision 3. The included Word implementation guide remains the revision 3 functional guide; this revision changes Home presentation only.

# Nexus Office 6.45.20 revision 3

Home now has larger vector app previews, a compact heading and balanced spacing. All six original launch actions and the shared Office navigation remain in use. A white startup screen matches Home, shows actual loading stages and retains startup error handling and Retry.

The General Aviation example restores the original 5×5 impact-and-likelihood risk matrix on Fleet overview and Safety & risks, plus an editable risk-register table. The example retains 14 tables and 101 records across six pages, with 15 measures and 23 visuals. Risk counts and IDs are computed from filtered source rows. Colours use impact × likelihood and the original Low 1–7, Medium 8–14, High 15–19 and Extreme 20–25 bands. Editing coordinates moves risks immediately; cell selection filters the page. Invalid coordinates are reported and empty data retains all 25 cells. Risk mode, bindings, title and width are editable through the native chart editor. Ordinary sum heat maps are retained.

The generated comparison photography, 74-percent image coverage, 629 templates, 2720 elements and 19 fonts from revision 2 are retained. This revision does not rewrite saved user projects. Current release assets exclude supplied reference photographs.

Validation covers responsive Home navigation, native and standalone-browser heat-map behaviour, source edits, filters, Undo/Redo, independent authoring exports, existing dashboard engines and loader integrity checks. Chromium on Linux was used; Windows hardware performance was not measured.
