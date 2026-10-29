# Log Output Application

University of Helsinki - DevOps with Kubernetes 2026

## Exercise 1.1

This Python application generates a UUID on startup
and prints the same UUID with a UTC timestamp every
5 seconds.

## Run locally

python3 main.py

## Build and run with Docker

docker build -t log-output:1.1 .
docker run --rm log-output:1.1

## Deploy to Kubernetes with k3d

First import the image into your existing k3d cluster:

k3d image import log-output:1.1 -c mycluster

Then deploy:

kubectl create deployment log-output --image=log-output:1.1

## Verify

kubectl get pods
kubectl logs -f deployment/log-output

## Note

Replace mycluster with your actual k3d cluster name.
