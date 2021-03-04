FROM python:3.6 AS builder

COPY . /source

WORKDIR /source

RUN pip install build \
    && python -m build

FROM python:3.6-alpine

COPY --from=builder /source/dist/* /app/
