FROM python:3.9.2-slim

RUN apt-get update && apt-get install

RUN apt-get install -y \
  libpq-dev \
  gcc \
  && apt-get clean

COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["./gunicorn.sh"]