メモリ最低でも2GBはほしいです。

```
docker build -t cat-detect .
docker run -p 80:8000 --name cat-detect-img cat-detect
```