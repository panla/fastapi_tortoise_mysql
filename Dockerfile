FROM python:3.8-slim-buster

ENV TZ=Asia/Shanghai LANG=C.UTF-8

COPY ./doc/requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

VOLUME ["/home/project", "/home/logs"]

WORKDIR /home/project

EXPOSE 8000

CMD ["sh", "run.sh"]
