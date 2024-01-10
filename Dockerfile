FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /articles-service

COPY Pipfile Pipfile.lock /articles-service/

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY . /articles-service
