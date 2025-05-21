FROM python:3.12.5

WORKDIR /usr/src/app

ADD requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ADD . ./

WORKDIR /usr/src/app/myproject

