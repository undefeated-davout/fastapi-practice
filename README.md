# README

[![CI](https://github.com/undefeated-davout/fastapi-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/undefeated-davout/fastapi-practice/actions/workflows/ci.yml)

## 開発環境構築

### nginxあり

```.bash
# 開始
docker-compose up -d
# 終了
docker-compose down
```

### nginxなし

```.bash
# 開始
docker-compose -f docker-compose.yml -f docker-compose-dev.yml up -d
# 終了
docker-compose -f docker-compose.yml -f docker-compose-dev.yml down
```

## 動作確認

- API
  - [http://localhost:23450/](http://localhost:23450/)
- API Swagger
  - [http://localhost:23450/docs](http://localhost:23450/docs)

## API構築

### JWT用SECRET KEY生成

```.bash
openssl rand -hex 32
```

上記コマンドで生成されたキーを.envのJWT_SECRET_KEYにセット
