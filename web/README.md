# Web README

## 動作確認

- [http://localhost:3000/](http://localhost:3000/)
  - nginx経由ではなく直接3000番ポートにアクセスする場合、ソース修正するとUIに自動反映される。

## デバッグ方法

1. 開発環境起動後、Chrome で `chrome://inspect` にアクセス
2. Remote Target `inspect` をクリック
3. 表示された[DevTools]の画面下部[Start]ボタンをクリック
4. VSCode[実行とデバッグ] の `full stack debug` を選択し実行
5. Chrome が起動し、 `http://localhost:3000/` にアクセスされる
6. .tsx 上にブレークポイントを置くとその行でストップする

### デバッグ補足

- デバッグ時は `xray-ai/web` ディレクトリを VSCode のルートディレクトリにする。

## 補足

- 保存時コード整形用の常駐コマンドが `scripts/run.sh` に記述されているため、Webディレクトリ配下のVSCodeのformatterは `.vscode/settings.json` でOFFにしている。（VSCodeのPrettierでは細かな設定ができないため）
- 上記formatterは `docker-compose-dev.yml` 起動の際のみ常駐する。
