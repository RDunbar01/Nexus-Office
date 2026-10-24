# Nexus Office 6.45.20 · リビジョン 6

## [▶ Nexus Office を開く](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/Nexus_Office_v6_45_20_Browser.html)

このリンクからアプリケーションを直接開けます。ブラウザー版にはインストールや Python は不要です。最新のデスクトップ向け Chromium 系ブラウザーを使用し、アプリケーションの注意事項を読んでから続行するか判断してください。読み込み時間は端末と接続環境によって異なります。

[English](https://github.com/RDunbar01/Nexus-Office/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Office/wiki/Home.fr) · [한국어](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ko) · [リリースファイル](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.20)

## 文書、シート、署名

リビジョン 6 では Writer と Paint の下部にタブを追加しました。**+** でタブを追加し、ダブルクリックまたは F2 で名前を変更できます。各タブは独立した内容とセッション中の Undo 履歴を保持します。Paint の Clear と画像エクスポートは現在のシートだけに作用します。Writer は全タブを `.nxwriter` に、Paint は全シートを `.nxpaint` に保存します。集合プロジェクトは最大 25 タブ、120 MiB に対応し、Undo 履歴は保存しません。開く際には確認後にそのアプリのタブ集合を置き換えます。Sheets のタブも直接名前を変更でき、既存の仕組みでシート参照を更新します。

PDF の読み込みでは編集可能なテキストを再構成し、Compatibility view には元のページレイアウトを保持します。この表示には、その後の Nexus での編集は反映されません。元のファイルは引き続きダウンロードできます。PDF の読み込みとプレビューは最大 300 ページで、スキャンした PDF の OCR は含まれません。マクロを含む元ファイルは保持しますが、VBA、ActiveX、埋め込みコードは実行しません。

Writer では描画、アップロード、保存済みの署名画像と現在のローカル日付を挿入できます。**署名画像は暗号学的な電子署名ではありません。旧形式の変換、ページ分割された PDF の直接ダウンロード、PKI 署名には任意のローカルヘルパーが必要で、公開ブラウザーページだけでは利用できません。** ヘルパーには Python 3.10 以降と LibreOffice が必要です。証明書による署名には、さらにこのパッケージ専用の設定が必要です。[文書と署名のガイド](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/OFFICE_DOCUMENTS.md)を確認してください。

## テーマと引き継がれた機能

10 種類のテーマは引き続き **Settings → Office themes** から選べます。保存済みの設定がなければ Porcelain が既定です。テーマはインターフェースを変更し、作成した内容は変更しません。設定はこのブラウザーとオリジンに保存され、ストレージが使えない場合はセッション中のみ保持されます。テーマ画像は HTML の隣に保持してください。[Office テーマガイド](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/OFFICE_THEMES.md)。

- **Dashboard Studio → Aviation example → Use template**：編集可能な表 14 個、架空のレコード 101 件、6 ページ、15 個のメジャー、23 個のビジュアルを収録しています。Fleet overview と Safety & risks には、データに連動する 5 × 5 のリスクマトリックスがあります。Impact または Likelihood を編集するとリスクの位置が変わり、セルを選択するとページを絞り込めます。[独立した編集可能なサンプルを開く](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/examples/NEXUS_General_Aviation_Dashboard.html)。
- **Paint → Design Studio**：リビジョン 2 から引き継いだ 629 個のテンプレート、2,720 個の要素、19 種類のフォントを収録しています。**Photos → Before & after collections** では、生成された比較画像 100 組を、各 100 種類の編集可能なレイアウトからなる 2 つのコレクションで利用できます。写真と文字は別々のレイヤーです。画像は眉のデザインを示すもので、実際の施術結果ではありません。

同梱の Word 実装ガイドは引き続きリビジョン 3 の機能を説明しています。リビジョン 6 の説明は OFFICE_DOCUMENTS.md を参照してください。[変更履歴](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/CHANGELOG_6.45.20.md)。

## オフライン利用とインストール

ブラウザー版 HTML は 19,976,619 バイトですが、**PDF ランタイム、テーマ画像、写真コレクション全体が HTML 単体に含まれているわけではありません**。HTML の隣に `document_assets`、`theme_assets`、`comparison_assets` を保持してください。`document_assets` フォルダー全体には、ローカルでの PDF 読み込みとプレビューに使うランタイム、マニフェスト、第三者ライセンスが含まれます。`theme_assets` 内の 12 個の PNG がテーマ画像を提供します。画像がない場合は組み込みのベクタープレビューに切り替わり、テーマの選択やアプリの起動は引き続き利用できます。HTML と同じ場所に `comparison_assets` フォルダーを置き、その中に `photos-01.js` から `photos-10.js` までを保持してください。この 10 個のファイルが、生成された画像 100 組を提供します。ファイルがない場合は、**Load comparison photos** で対応する `.nxcomparisons` パックを読み込めます。保存した `.nxpaint` プロジェクトには、使用した写真が埋め込まれます。

一式をダウンロードするには、リポジトリの **Code → Download ZIP** を選び、展開してから `releases/6.45.20/Nexus_Office_v6_45_20_Browser.html` を開いてください。フォルダー構成を変更しないでください。ローカルサーバーは不要です。ブラウザーは DecompressionStream、TextEncoder/TextDecoder、Web Crypto に対応している必要があります。展開後のアプリケーションデータと実行時メモリー使用量は、HTML のダウンロードサイズより大きくなります。

完全版には 482 個のファイルがあり、展開後の合計は 500,273,126 バイトです。配布ファイルはそれぞれ 20,000,000 バイト未満です。元の大きな ZIP アーカイブはコミットされず、展開済みの構成ファイルが提供されています。任意のソースインストールを行う場合は、インストーラー、マニフェスト、**23 個すべての `.nxd` 分割ファイル**を同じ場所に置いてください。各分割ファイルは最大 10,000,000 バイトです。標準の CPython 3.12 を使い、[INSTALL.txt](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/INSTALL.txt) に従ってください。展開後も `candidate.html`、`source_scripts`、`document_assets`、`theme_assets`、`comparison_assets` を同じ場所に保持してください。

バージョンを切り替える前に、既存の文書とプロジェクトをバックアップしてください。このリリースは保存済みプロジェクトを書き換えません。[以前のリリース](https://github.com/RDunbar01/Nexus-Office/tree/main/releases)も引き続き利用できます。

## 検証範囲と制限

[提供されたリビジョン 6 の結果](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/RELEASE_VALIDATION.json)には、Linux 上の Chromium におけるブラウザー文書機能 25 項目、テーマ 14 項目、Design Studio 21 項目、リスク 9 項目に加え、サービス 6 項目、ソース 6 項目、ローダー 5 ケースの検証が記録されています。実際の LibreOffice 変換と自己署名のテスト証明書を使用しています。埋め込みプレビュー付き Pages とマクロのテストファイルは合成されたもので、実在するすべてのファイルとの互換性を証明するものではありません。古い結果は過去の検証記録であり、リビジョン 6 で新たに実行されたテストではありません。

[別途行われたパッケージ検証](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/PUBLICATION_VERIFICATION_6.45.20.json)は、提供されたアプリケーションや機能テストを実行せず、バイト列、ハッシュ、ファイル一覧、復元データ、補助ファイルのパスを確認しています。これは複数プラットフォームでの動作保証ではありません。Windows と macOS の実機ではテストしていません。これらの記録は Radeon の性能や物理的な 4K モニターを検証したものではありません。起動速度や文書形式の完全な再現性は保証されません。[正確なハッシュとブラウザー版の詳細](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/BROWSER_TRIAL.md)。

## 利用許諾

Nexus が権利を保有する部分については、個人利用、および組織内での商用テストと評価が認められています。再配布、改変、本番環境への導入、その他の商用利用には、明示的な書面による同意が必要です。第三者のライセンスおよび過去に付与された権利は変更されません。[ライセンス](https://github.com/RDunbar01/Nexus-Office/blob/main/LICENSE)、[評価許諾](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md)、同梱の注意事項を確認してください。
