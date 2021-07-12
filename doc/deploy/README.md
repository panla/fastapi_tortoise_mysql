# README

Dockerfile 和 `docker-compose.yaml` 中的路径要根据实际情况来设置

网络 fastapi_tm_net 需要提前建立

example

```bash
docker network create --driver bridge --subnet 172.22.0.1/16 --gateway 172.22.0.1 fastapi_tm_net
```

run

```bash
docker-compose up -d --build
```
