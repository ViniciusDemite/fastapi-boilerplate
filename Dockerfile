FROM python:3.8

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

# RUN apt-get update -y && \
#   apt-get install -y python3-pip python3.8-dev

COPY . .

RUN pip install -r requirements.txt


# CMD uvicorn --host=0.0.0.0 app.main:app