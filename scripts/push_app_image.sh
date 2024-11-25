#!/bin/bash

docker login

docker push horlar/flask-restapi-crud-app:stable

echo "--------- Image Pushed to DockerHub -----------"