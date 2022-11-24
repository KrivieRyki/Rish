FROM python:3.11.0rc2-slim-buster

COPY . /myRishat

WORKDIR /myRishat

COPY requirements.txt ./

RUN apt-get update &&\
    apt-get install -y libpq-dev gcc


RUN pip install --no-cache-dir -r requirements.txt




CMD [ "python", "manage.py", "runserver" ]