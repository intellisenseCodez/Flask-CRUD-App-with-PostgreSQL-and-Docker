# pull official base image
FROM python:3.11-alpine3.18

LABEL NAME=flask-crud-restapi-image
LABEL VERSION=latest

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ /app/

EXPOSE 5000

CMD [ "python3", "-m", "flask", "run",  "--host=0.0.0.0", "--port=5000"]