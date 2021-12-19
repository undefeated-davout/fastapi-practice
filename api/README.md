# API README

## 動作確認

- [http://localhost:8000/](http://localhost:8000/)

## Swagger

- [http://localhost:8000/docs](http://localhost:8000/docs)

## デバッグ（VSCode）

[F5]キーで `.vscode/launch.json` 中の `FastAPI Remote Debug` が起動しブレークポイントで停止することができる。

## マイグレーション

### マイグレーションファイル作成

```.bash
alembic revision --autogenerate -m '{マイグレーションファイル名に使用する説明文}'
```

※ `alembic/versions` 配下にマイグレーションファイルが出力されるのでcolumn順を適切に変更（created_at、updated_atを最後尾に移動するなど）

### マイグレーション実行

```.bash
# 全マイグレーションファイル実行
alembic upgrade head

# 1ファイルだけマイグレーション実行
alembic upgrade +1

# 1ファイルだけマイグレーション取り消し
alembic downgrade -1

# マイグレーション全取り消し（全テーブル削除されるので注意！）
alembic downgrade base
```

## 自動テスト

### 実行方法

```.bash
pytest -v
```

### 補足

- テスト用ファイルは `api/tests/` ディレクトリ配下に追記する。
- テスト用DBは開発環境起動時のみ起動する。
- テスト用DBは実行用DBとは完全に分離している。
