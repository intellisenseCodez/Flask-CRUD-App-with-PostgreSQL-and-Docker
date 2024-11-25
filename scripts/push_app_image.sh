#!/bin/bash

# Docker login
echo "Logging into DockerHub..."
docker login || { echo "Docker login failed!"; exit 1; }

# Push the image to DockerHub
IMAGE_NAME="horlar/flask-restapi-crud-app:$IMAGE_TAG"
echo "Pushing image: $IMAGE_NAME"
docker push "$IMAGE_NAME" || { echo "Docker push failed!"; exit 1; }

echo "--------- Image Pushed to DockerHub -----------"
