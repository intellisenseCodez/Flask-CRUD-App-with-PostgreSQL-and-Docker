#!/bin/bash

docker build  -t horlar/flask-restapi-crud-app:stable .

echo "------------- Docker Image Created Successfully ------------------"
docker images | grep horlar

