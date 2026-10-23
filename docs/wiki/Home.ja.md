# 現行リリース 6.45.4

[ブラウザーで試す](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_4_Browser.html) · [完全版パッケージ](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.4)

ホーム画面には Writer、Grid、Dashboard Studio、NexusPoint、Paint、Compatibility の6つのカードがあります。アシスタントと最近の項目のパネルは非表示になり、自動表示は無効になっています。文書と履歴は保持されます。6.45.3 のリボンは維持されています。この更新は現行の画面構成を説明するもので、モデルや編集機能の追加を示すものではありません。

Nexus 所有の素材は個人利用および社内の商用テスト・評価に利用できます。配布、改変、本番導入、その他の商用利用には明示的な書面による同意が必要です。第三者のライセンスと既に付与された権利は変更されません。 [評価許可](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).

## 旧版の説明（変更せず保存）

# 現行の修正版 6.45.2

[ブラウザーで試す](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_2_Browser.html) · [完全版パッケージ](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.2)

6.45.2 では Writer リボンのオーバーフロー規則を修正し、高さを制限したツール領域を実際にスクロールできるようにしました。ルーラーの数値入力欄をコンパクトな横一列にまとめ、必要に応じてスクロールすることで文書の表示領域を確保します。すべての操作項目にアクセスできますが、常に同時に表示されるわけではありません。6.45.1 のアシスタント改善は変更していません。公開済みの 6.45.1 のレイアウトは、この表示修正によって置き換えられます。

Nexus 所有の素材は個人利用および社内の商用テスト・評価に利用できます。配布、改変、本番導入、その他の商用利用には明示的な書面による同意が必要です。第三者のライセンスと既に付与された権利は変更されません。 [評価許可](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).

[6.45.2](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/CHANGELOG_6.45.2.md) · [LICENSE](https://github.com/RDunbar01/Nexus-Office/blob/main/LICENSE) · [COMMERCIAL_EVALUATION_PERMISSION](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md)

## 旧版の説明（レイアウトは更新済み・本文は変更せず保存）

# 現行リリース 6.45.1

[ブラウザーで試す](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_1_Browser.html) · [完全版インストーラーの構成ファイル](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.1) · [リリースノート](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/CHANGELOG_6.45.1.md)

インストール版とブラウザー版のアシスタントパネル、ヘッダー、入力欄を改善しました。Writer はリボンの各グループを利用可能な幅に配置し、アシスタントを固定した場合を含め、狭いウィンドウでも操作項目とルーラーが収まるようにしました。コマンド、文書形式、モデル、編集機能は変更していません。

現行のブラウザー版とインストール版には同じ UI 変更が含まれます。完全版 ZIP にはインストーラーと全データファイルが含まれるため、一緒に保管してください。各データファイルは 10,000,000 バイト以下、各配布コンポーネントは 20,000,000 バイト未満です。この UI 更新は対応モデルを追加せず、実機の Windows/Radeon 検証を示すものではありません。

Nexus 所有の素材は個人利用および社内の商用テスト・評価に利用できます。配布、改変、本番導入、その他の商用利用には明示的な書面による同意が必要です。第三者のライセンスと既に付与された権利は変更されません。 [評価許可](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).

## 旧版の説明（変更せず保存）

# Nexus Office

[ブラウザーで試す](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_0_Browser.html) · [リポジトリ](https://github.com/RDunbar01/Nexus-Office)

Nexus Office 6.45.0 は Writer、Grid、Present、Paint、Dashboard をまとめたアプリです。ブラウザー試用版（パッケージ改訂 1）は、既存アプリのコードと素材を単一 HTML に格納します。オンライン評価を始めやすくし、ダウンロード後は一つのファイルで利用できるようにするための形式です。

## 機能と制限

文書とワークブックの編集、プレゼンテーションのレイアウト、画像素材、ダッシュボードを利用できます。Office コマンドは定義済み操作に限定され、入力値、プレビュー、承認に基づいて変更します。Writer の変更は既存の取り消し機能を使います。同梱の小規模モデルは汎用 Office エージェントとして認定されておらず、有効化もされていません。

インポートとエクスポートの対応範囲は形式によって異なります。Microsoft Office との完全な互換性は保証しません。クリップボード、印刷、表示はブラウザーに依存します。取り込んだダッシュボードデータはスナップショットであり、ライブ接続ではありません。

## 起動

DecompressionStream、TextEncoder/TextDecoder、Web Crypto に対応した最新のデスクトップブラウザーを使ってください。同梱データをローカルで検証・展開してからアプリの通知を表示します。起動にはサーバー、Python、PyTorch、CDN は不要です。配布 HTML は 20,000,000 バイト未満ですが、展開後のアプリと必要メモリはより大きくなります。起動時間は端末によって異なります。

完全版 6.45.0 のパッケージは変更せずに残しています。任意のインストーラーには CPython 3.12 を推奨します。旧パッケージの candidate.html には二つの付属スクリプトが必要ですが、新しい単一ファイル試用版には不要です。

## 検証と許可

[ビルドとテストの詳細](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/BROWSER_TRIAL.md)を参照してください。Nexus 所有部分の個人利用と社内での商用テスト・評価は許可されています。配布、変更、本番導入、その他の商用利用には明示的な書面による同意が必要です。第三者ライセンスと以前に付与された権利は変わりません。[評価許可](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md)をご確認ください。

[English](https://github.com/RDunbar01/Nexus-Office/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Office/wiki/Home.fr) · [한국어](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ko)
