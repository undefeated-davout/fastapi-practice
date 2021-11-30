# README

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
