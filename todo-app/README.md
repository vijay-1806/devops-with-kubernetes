# Todo App

University of Helsinki - DevOps with Kubernetes 2026

## Exercise 1.2

A simple Python HTTP server that reads its listening
port from the PORT environment variable.

## Run locally

PORT=3000 python3 main.py

## Docker

docker build -t todo-app:1.2 .
docker run --rm -p 3000:3000 -e PORT=3000 todo-app:1.2

## Kubernetes

k3d image import todo-app:1.2 -c k3s-default
kubectl create deployment todo-app --image=todo-app:1.2

Configure the Deployment's imagePullPolicy to IfNotPresent
and set PORT=3000.

## Verify

kubectl get pods
kubectl logs deployment/todo-app
