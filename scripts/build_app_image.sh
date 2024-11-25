#!/bin/bash

docker build  -t horlar/flask-restapi-crud-app:"$IMAGE_TAG" .

echo "------------- Docker Image Created Successfully ------------------"
docker images | grep horlar

