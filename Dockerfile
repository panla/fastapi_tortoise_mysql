FROM python:3.8-slim-buster

ENV TZ=Asia/Shanghai LANG=C.UTF-8

COPY ./mirrors /mirrors

RUN cp /mirrors/sources.list /etc/apt/sources.list && apt update \ 
&& python -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/ \ 
&& pip3 install -r /mirrors/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

VOLUME ["/home/project", "/home/logs"]

WORKDIR /home/project

EXPOSE 8000

CMD ["sh", "run.sh"]
