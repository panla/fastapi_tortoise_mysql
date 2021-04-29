# README

Dockerfile 和 `docker-compose.yaml` 中的路径要根据实际情况来设置

网络 ftm 需要提前建立

```bash
docker network create --driver bridge --subnet 172.21.0.1/16 --gateway 172.21.0.1 ftm
```

```bash
docker-compose up -d --build
```
