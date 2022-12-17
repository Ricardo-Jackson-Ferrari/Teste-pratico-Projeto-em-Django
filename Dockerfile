FROM python:3.11-slim

RUN useradd -ms /bin/bash python

RUN apt-get update

RUN pip install pipenv

USER python

WORKDIR /home/python/app

ENV PIPENV_VENV_IN_PROJECT=True

COPY . .

RUN pipenv install

CMD [ "pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]