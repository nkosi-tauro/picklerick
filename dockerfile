FROM python:3.7-slim


RUN python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt

COPY . /app/