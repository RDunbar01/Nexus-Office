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
