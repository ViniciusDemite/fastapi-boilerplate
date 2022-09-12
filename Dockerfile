FROM python:3.8

WORKDIR /app

RUN apt-get update -y && \
  apt-get install -y python3-pip python3.8-dev

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000