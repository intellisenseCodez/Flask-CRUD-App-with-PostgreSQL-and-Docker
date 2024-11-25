#!/bin/bash

echo "Deleting existing containers..."

docker container rm -f flask-restapi-crud-app-container

echo ""

docker run \
    -p 5000:5000 \
    -d \
    --name flask-restapi-crud-app-container \
    horlar/flask-restapi-crud-app:${IMAGE_TAG}