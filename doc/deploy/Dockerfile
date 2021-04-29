FROM panla/centos8_py38:v2

COPY ./requirements.txt /requirements.txt

RUN source /etc/profile && source ~/.bashrc && pip3 install -r requirements.txt

VOLUME /home/project

WORKDIR /home/project

EXPOSE 8000

CMD ["sh", "run.sh"]
