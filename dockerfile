FROM python:3.9.5-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update

RUN apt-get upgrade -y

COPY . /app

RUN pip install -r requirements.txt
