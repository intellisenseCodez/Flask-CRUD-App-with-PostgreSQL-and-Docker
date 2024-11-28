#!/bin/bash

# Set script to exit on any errors
set -e

# Apply Flask deployment and service
echo "Applying Flask deployment..."
kubectl apply -f ../deployments/app-deployment.yml
echo "Flask deployment applied successfully."

echo "Applying Flask service..."
kubectl apply -f ../deployment/app-service.yml
echo "Flask service applied successfully."

# Apply Postgres ConfigMap
echo "Applying Postgres ConfigMap..."
kubectl apply -f ../deployments/postgres-configmap.yml
echo "Postgres ConfigMap applied successfully."

# Apply Postgres deployment and PVC
echo "Applying Postgres deployment..."
kubectl apply -f ../deployments/postgres-deployment.yml
echo "Postgres deployment applied successfully."

echo "Applying Postgres PersistentVolumeClaim..."
kubectl apply -f ../deployments/postgres-pvc.yml
echo "Postgres PVC applied successfully."

# Apply Postgres service
echo "Applying Postgres service..."
kubectl apply -f ../deployments/postgres-service.yml
echo "Postgres service applied successfully."

echo "Deployment complete!"
