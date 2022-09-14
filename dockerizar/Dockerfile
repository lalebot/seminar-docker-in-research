FROM python:3.9.14-slim-bullseye
RUN apt-get update && apt-get install -y --no-install-recommends git sqlite3 wget tar && apt-get clean

RUN pip install urllib3 

COPY conf.ini .
COPY pip_prom_tom.py .