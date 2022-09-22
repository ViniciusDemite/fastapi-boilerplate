FROM python:3.8

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt