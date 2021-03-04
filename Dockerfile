FROM python:3.9 AS builder

COPY . /source

WORKDIR /source

RUN pip install build \
    && python -m build

FROM python:3.9-alpine

COPY --from=builder /source/dist /dist

RUN pip install /dist/*.whl \
    && rm -rf /dist

ENTRYPOINT ["python", "-m", "bump"]
