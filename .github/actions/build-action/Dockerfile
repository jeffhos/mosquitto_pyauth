FROM ubuntu:20.04

ENV PYTHON_VERSION=3.8

RUN apt update
RUN apt full-upgrade -y
RUN apt install -y build-essential python3.8-dev libmosquitto-dev mosquitto-dev

CMD make
