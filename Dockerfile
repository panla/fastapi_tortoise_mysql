FROM python:3.8-slim-buster

ENV TZ=Asia/Shanghai LANG=C.UTF-8

COPY ./mirrors /mirrors

RUN cp /mirrors/sources.list /etc/apt/sources.list && apt update && cd /mirrors \ 
&& pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

VOLUME ["/home/project", "/home/logs"]

WORKDIR /home/project

EXPOSE 8000

CMD ["sh", "run.sh"]
