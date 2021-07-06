FROM panla/centos8_py38

COPY ./doc/requirements.txt /requirements.txt

ENV PATH="/opt/python/bin:$PATH"

RUN pip3 install -r requirements.txt

VOLUME ["/home/project", "/home/logs"]

WORKDIR /home/project

EXPOSE 8000

CMD ["sh", "run.sh"]
