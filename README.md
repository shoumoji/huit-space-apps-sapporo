# huit-space-sapporo

## ディレクトリについて

- [api](/api/)
  - API関連のコード
- [database](/database/)
  - データベース(MySQL)関連のコード
- [frontend](/frontend/)
  - フロントエンド関連のコード
- [nginx](/nginx/)
  - ローカル実行時のみ使用するリバースプロキシ(ALBの代替)
- [.circleci](/.circleci/)
  - AWSへのデプロイ
- [.github](/.github/)
  - ドキュメントやコードの自動生成

## 起動方法

docker compose で全体を起動できます。

### 起動

```bash
git clone git@github.com:shoumoji/huit-space-apps-sapporo.git
cd huit-space-apps-sapporo
docker compose up --build -d
```

### 終了

```bash
docker compose down
```
