FROM python:3.6 AS builder

COPY . /app

WORKDIR /app

RUN pip install build \
    && python -m build
