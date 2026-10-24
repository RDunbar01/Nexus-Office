# Nexus Office 6.45.20 · 리비전 6

## [▶ Nexus Office 열기](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/Nexus_Office_v6_45_20_Browser.html)

이 링크는 애플리케이션을 바로 엽니다. 브라우저 버전에는 설치나 Python이 필요하지 않습니다. 최신 데스크톱 Chromium 계열 브라우저를 사용하고, 애플리케이션 안내문을 읽은 뒤 계속할지 결정하세요. 로딩 시간은 기기와 연결 환경에 따라 달라집니다.

[English](https://github.com/RDunbar01/Nexus-Office/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Office/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ja) · [릴리스 파일](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.20)

## 문서, 시트 및 서명

리비전 6는 Writer와 Paint 하단에 탭을 추가합니다. **+**로 탭을 추가하고, 탭을 두 번 클릭하거나 F2를 눌러 이름을 변경하세요. 각 탭은 독립적인 내용과 세션 중 실행 취소 기록을 유지합니다. Paint의 Clear와 이미지 내보내기는 활성 시트에만 적용됩니다. Writer는 모든 탭을 `.nxwriter`로, Paint는 모든 시트를 `.nxpaint`로 저장합니다. 통합 프로젝트는 최대 탭 25개와 120 MiB를 지원하며 실행 취소 기록은 저장하지 않습니다. 프로젝트를 열면 확인 후 해당 앱의 탭 모음을 교체합니다. Sheets 탭도 직접 이름을 변경할 수 있으며 기존 기능이 시트 참조를 업데이트합니다.

PDF 가져오기는 편집 가능한 텍스트를 재구성하고 Compatibility view에 원본 페이지 배치를 보존합니다. 이 보기에는 이후 Nexus에서 편집한 내용이 반영되지 않습니다. 원본 파일은 계속 다운로드할 수 있습니다. PDF 가져오기와 미리 보기는 최대 300페이지이며 스캔 PDF의 OCR은 포함하지 않습니다. 매크로가 포함된 원본은 보존하지만 VBA, ActiveX 및 포함된 코드는 실행하지 않습니다.

Writer는 직접 그리거나 업로드하거나 저장한 서명 이미지와 현재 현지 날짜를 삽입할 수 있습니다. **서명 이미지는 암호학적 전자서명이 아닙니다. 이전 형식 변환, 페이지가 구분된 PDF 직접 다운로드 및 PKI 서명에는 선택 사항인 로컬 도우미가 필요하며, 호스팅된 브라우저 페이지만으로는 제공되지 않습니다.** 도우미에는 Python 3.10 이상과 LibreOffice가 필요합니다. 인증서 서명에는 이 패키지 전용 추가 설정이 필요합니다. [문서 및 서명 가이드](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/OFFICE_DOCUMENTS.md)를 확인하세요.

## 테마와 유지된 작업 공간

테마 10개는 계속 **Settings → Office themes**에서 선택할 수 있습니다. 저장된 선택이 없으면 Porcelain이 기본값입니다. 테마는 인터페이스만 변경하며 작성한 내용은 바꾸지 않습니다. 설정은 현재 브라우저와 출처에 저장되며 저장소가 차단되면 세션 동안만 유지됩니다. 테마 이미지는 HTML 옆에 보관하세요. [Office 테마 가이드](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/OFFICE_THEMES.md).

- **Dashboard Studio → Aviation example → Use template**: 편집 가능한 표 14개, 가상 레코드 101개, 페이지 6개, 측정값 15개, 시각화 23개가 포함되어 있습니다. Fleet overview와 Safety & risks에는 데이터와 연동되는 5 × 5 위험 매트릭스가 있습니다. Impact 또는 Likelihood를 편집하면 위험의 위치가 바뀌고, 셀을 선택하면 페이지가 필터링됩니다. [독립적으로 편집 가능한 예제 열기](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/examples/NEXUS_General_Aviation_Dashboard.html).
- **Paint → Design Studio**: 리비전 2부터 유지된 템플릿 629개, 요소 2,720개, 글꼴 19개를 제공합니다. **Photos → Before & after collections**에서는 생성된 비교 이미지 100쌍을 각각 편집 가능한 레이아웃 100개로 구성된 두 컬렉션에서 사용할 수 있습니다. 사진과 텍스트는 별도 레이어로 유지됩니다. 이미지는 눈썹 디자인을 보여 주는 예시이며, 실제 시술 결과가 아닙니다.

포함된 Word 구현 가이드는 여전히 리비전 3의 기능을 설명합니다. 리비전 6의 설명은 OFFICE_DOCUMENTS.md를 확인하세요. [변경 기록](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/CHANGELOG_6.45.20.md).

## 오프라인 사용과 설치

브라우저 HTML은 19,976,619바이트이지만, **PDF 런타임, 테마 이미지 및 전체 사진 컬렉션이 HTML 파일 하나에 모두 포함되어 있지는 않습니다**. HTML 옆에 `document_assets`, `theme_assets`, `comparison_assets`를 보관하세요. 전체 `document_assets` 폴더에는 로컬 PDF 가져오기와 미리 보기에 필요한 런타임, 매니페스트 및 타사 라이선스가 있습니다. `theme_assets`의 PNG 12개가 테마 이미지를 제공합니다. 이미지가 없으면 기본 벡터 미리 보기를 사용하며, 테마 선택과 앱 실행 기능은 계속 작동합니다. HTML 옆에 `comparison_assets` 폴더를 두고 그 안에 `photos-01.js`부터 `photos-10.js`까지 보관하세요. 이 파일 10개가 생성된 이미지 100쌍을 제공합니다. 파일이 없으면 **Load comparison photos**에서 해당 `.nxcomparisons` 팩을 가져오세요. 저장된 `.nxpaint` 프로젝트에는 사용한 사진이 포함됩니다.

전체를 다운로드하려면 저장소에서 **Code → Download ZIP**을 선택하고 압축을 푼 뒤 `releases/6.45.20/Nexus_Office_v6_45_20_Browser.html`을 여세요. 폴더 구조를 유지하세요. 로컬 서버는 필요하지 않습니다. 브라우저는 DecompressionStream, TextEncoder/TextDecoder, Web Crypto를 지원해야 합니다. 압축 해제된 애플리케이션 데이터와 실행 중 메모리 사용량은 HTML 다운로드 크기보다 큽니다.

전체 릴리스는 파일 482개이며, 압축 해제 후 총 500,273,126바이트입니다. 배포 파일은 각각 20,000,000바이트 미만입니다. 원본 대용량 ZIP은 커밋하지 않고, 압축을 푼 구성 파일을 제공합니다. 선택적으로 소스를 설치하려면 설치 프로그램, 매니페스트, **`.nxd` 분할 파일 23개 모두**를 같은 위치에 두세요. 각 분할 파일은 최대 10,000,000바이트입니다. 표준 CPython 3.12를 사용하여 [INSTALL.txt](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/INSTALL.txt)를 따르세요. 압축 해제 후에도 `candidate.html`, `source_scripts`, `document_assets`, `theme_assets`, `comparison_assets`를 함께 보관하세요.

버전을 전환하기 전에 기존 문서와 프로젝트를 백업하세요. 이 릴리스는 저장된 프로젝트를 다시 작성하지 않습니다. [이전 릴리스](https://github.com/RDunbar01/Nexus-Office/tree/main/releases)도 계속 이용할 수 있습니다.

## 검증 범위와 한계

[제공된 리비전 6 결과](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/RELEASE_VALIDATION.json)에는 Linux의 Chromium에서 수행한 브라우저 문서 검사 25개, 테마 검사 14개, Design Studio 검사 21개, 위험 검사 9개와 함께 서비스 검사 6개, 소스 검사 6개, 로더 사례 5개가 기록되어 있습니다. 실제 LibreOffice 변환과 자체 서명 테스트 인증서를 사용했습니다. 내장 미리 보기가 있는 Pages 파일과 매크로 테스트 파일은 합성 자료이며, 모든 실제 파일과의 호환성을 입증하지는 않습니다. 이전 결과는 과거 검증 기록이지 리비전 6에서 새로 실행한 테스트가 아닙니다.

[별도로 수행한 패키지 검증](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/PUBLICATION_VERIFICATION_6.45.20.json)은 제공된 애플리케이션이나 기능 테스트를 실행하지 않고 바이트, 해시, 파일 목록, 복원 데이터, 보조 파일 경로를 확인합니다. 이는 여러 플랫폼에서의 동작 검증이 아닙니다. Windows와 macOS 실물 하드웨어에서는 테스트하지 않았습니다. 이 기록은 Radeon 성능이나 실제 4K 모니터에서의 동작을 검증하지 않습니다. 시작 속도와 문서 형식의 완전한 재현성은 보장하지 않습니다. [정확한 해시와 브라우저 세부 정보](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/BROWSER_TRIAL.md).

## 사용 허가

Nexus가 권리를 소유한 자료는 개인 용도와 조직 내부의 상업적 테스트 및 평가에 사용할 수 있습니다. 재배포, 수정, 운영 환경 배포 및 기타 상업적 사용에는 명시적인 서면 동의가 필요합니다. 타사 라이선스와 이전에 부여된 권리는 변경되지 않습니다. [라이선스](https://github.com/RDunbar01/Nexus-Office/blob/main/LICENSE), [평가 허가](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md), 포함된 고지 사항을 확인하세요.
