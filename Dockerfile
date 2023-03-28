FROM python:3.10-buster

WORKDIR /app/helloworld

ENV no_proxy=localhost,10.2.28.0/24 \
    https_proxy=http://proxy.vtb.t1cloud:3128 \
    http_proxy=http://proxy.vtb.t1cloud:3128 \
    HTTPS_PROXY=http://proxy.vtb.t1cloud:3128 \
    HTTP_PROXY=http://proxy.vtb.t1cloud:3128

RUN pip --no-cache-dir install -U poetry

ADD pyproject.toml /app/helloworld/pyproject.toml
ADD poetry.lock /app/helloworld/poetry.lock

RUN poetry export -f requirements.txt --output requirements.txt
RUN python -m  pip install -r requirements.txt

ADD helloworld /app/helloworld/helloworld
ADD alembic.ini /app/helloworld/alembic.ini
ADD migrations /app/helloworld/migrations

EXPOSE 8001

ENTRYPOINT [ "sh", "-c", "alembic upgrade head && uvicorn --host 0.0.0.0 --port 8001 helloworld.app:app"]
