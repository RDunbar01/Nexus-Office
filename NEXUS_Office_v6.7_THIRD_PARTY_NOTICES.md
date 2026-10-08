# Third-Party Notices and Attribution

**Project:** NEXUS Office Suite v6.7  
**Document date:** 8 October 2026  
**Prepared for:** NEXUS Emerging Technology

This document records dependencies, standards, integration points and provenance **as evidenced by inspection of the user-supplied single-file HTML application**. A reference to a format or API is **not** an assertion that the NEXUS source copied or embeds code from its maintainers.

## 1. Findings from the supplied source

- **No external JavaScript bundles or runtime CDN imports were identified.** The inspected page contains 19 embedded JavaScript blocks and inline styles, without externally linked `<script src>` or bundled JS frameworks such as JSZip, SheetJS, pdf-lib, Fabric.js or Quill.
- ZIP container creation and extraction, OOXML/ODF file conversion, PDF construction, charting, image handling and the NEXUS formula parser are implemented in the supplied JavaScript rather than calling a named third-party package. Similarity to standards or familiar algorithms does not establish the origin of individual source statements.
- **No upstream copyright headers or explicit software-license file** were present in the supplied HTML. A code audit alone cannot certify that no source fragment was adapted from an unrecorded repository or published example.
- The document-format and standards acknowledgements below **do not impose the standards bodies' copyright terms on the NEXUS code** merely because the formats are supported.

## 2. Standards and community acknowledgements (not bundled software)

| Technology | Credit / governing organization | How NEXUS uses it | Licensing or attribution note |
| --- | --- | --- | --- |
| Office Open XML (DOCX/XLSX/PPTX) | **Ecma International / ECMA-376; ISO/IEC 29500**. Original format technologies developed by Microsoft and others | NEXUS writes/reads a subset of OOXML XML parts and ZIP packages | Specification interoperability, **not** use or redistribution of Microsoft Office application code. [Official ECMA-376 standard](https://ecma-international.org/publications-and-standards/standards/ecma-376/) |
| OpenDocument (ODT/ODS/ODP) | **OASIS OpenDocument Technical Committee** | NEXUS writes/reads bounded OpenDocument documents and ZIP-based packages | Format standard, **not** use or redistribution of LibreOffice/OpenOffice source. [ODF 1.3](https://www.oasis-open.org/standard/open-document-format-for-office-applications-opendocument-version-1-3/) |
| Web platform and JavaScript APIs | **WHATWG, ECMA TC39 and browser-engine contributors** | HTML/CSS/JavaScript, Canvas, IndexedDB, Blob, DOMParser, File APIs, compression streams | Browser-provided capabilities; no Chromium or Firefox engine binary is bundled. [WHATWG HTML](https://html.spec.whatwg.org/multipage/), [ECMAScript](https://tc39.es/ecma262/) |
| Browser File System Access API | **Browser-platform contributors** | Optional user-granted local file binding where supported | API access; no third-party file-picker library is bundled. [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API) |
| ZIP / DEFLATE and CRC-32 | **ZIP format and Deflate interoperability specifications**, including the historical work of Phil Katz and other contributors | Custom JavaScript ZIP writer/reader, decompression, CRC checks | Use of publicly documented data formats and algorithms, **not** inclusion of JSZip/pako source; no upstream ZIP library was identified |
| PDF format | **Adobe (format origin); ISO 32000 standardization** | JavaScript-created PDF byte streams for selected exports | Support for PDF files does **not** mean Adobe libraries or Adobe software are distributed |
| Image/media formats | Format communities and specifications for PNG, JPEG, GIF, TIFF, BMP, WebP and SVG | Browser Canvas output and custom interchange routines | Format usage is not evidence that reference implementations or codecs were copied |

## 3. Optional platform integrations and trademarks

**Microsoft Office.** DOCX/XLSX/PPTX names denote compatibility targets. Microsoft, Word, Excel and PowerPoint are trademarks of their respective owner(s). This project is not claimed to be endorsed or developed by Microsoft.

**OpenDocument and LibreOffice.** The ODF format is governed by the OASIS standard; no LibreOffice software package was identified in this HTML. The project does not assert official compatibility certification.

**YouTube / Vimeo.** NEXUS permits optional media embeds from specified services. The service players are provided by their platform when selected and are not packaged source code or NEXUS assets. Embedded media may create network traffic and is subject to its service's terms.

**NEXUS Foundry / Wheelhouse.** These are optional NEXUS project integrations. The HTML contains bridge/launcher code referencing a local runtime endpoint. That endpoint and the backend are not included in this repository and their dependencies should be documented **separately** if distributed.

**Fonts.** The source names local/system font faces, including Inter, Calibri, Segoe UI and others, as rendering choices or fallbacks. **No font binaries are packaged or sublicensed.** Any externally installed font remains subject to its own license; naming a font family in CSS does not distribute it.

## 4. Provenance and source ownership

| Item | Audit outcome |
| --- | --- |
| Source of application HTML and JS | Supplied by NEXUS Emerging Technology for repository packaging |
| Bundled third-party JS packages | **None identified** in the inspected HTML |
| Copied/adapted source snippets | **Cannot be determined conclusively** from a static scan alone |
| Original uploaded HTML | Preserved under `archive/Nexus_Office_v6.7_Original.html` |
| Debugging changes | ZIP/OOXML import, archive integrity, workspace Writer HTML sanitization and file-routing fixes; see `CHANGELOG.md` |
| License for NEXUS-owned code | **Not specified**; do not infer Apache-2.0 or another open-source license |

The preserved original source can be compared directly against the repaired file. No outside library was inserted to implement the repair.

## 5. Maintaining notices for future contributions

When external source code, icons, fonts, datasets or libraries are added:

1. Record the component name, upstream author(s), repository URL, exact version or commit, files used and any modifications.
2. Preserve upstream copyright and license notices; include any mandatory full license text.
3. Review code provenance and compatibility **before** publishing a downstream license for the NEXUS-owned work.
4. Keep format/standards acknowledgements separate from notices required for actual redistributed code.

**Attribution correction policy:** If an original author identifies a copied or adapted fragment in this repository, the project maintainer should verify its provenance and update the notices and licensing before the next release.

---

*This inventory documents observable content, not a legal opinion or a complete historical code-origin investigation.*

## 6. Optional developer test tooling

The repository's optional `tests/smoke_test.py` uses **Microsoft Playwright for Python** when installed by the person running the tests. Playwright is distributed under the **Apache License 2.0**; its own distribution is **not** included with NEXUS Office. [Source and license](https://github.com/microsoft/playwright). The test harness also uses Python standard-library utilities; **no Python runtime is bundled** with the application. These are *development/test dependencies*, not requirements to open the HTML application.
