FROM python:3.7.3-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

RUN chmod +x /app/gunicorn_starter.sh

ENTRYPOINT ["./gunicorn_starter.sh"]

EXPOSE 8000
