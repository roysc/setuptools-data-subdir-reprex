from ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3-pip

ARG PIP_VERSION
RUN python3 -m pip install --upgrade "pip==$PIP_VERSION"
