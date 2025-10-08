## 🧩 Kubernetes App Deployment

## 📘 Overview
I created a containerized web application (Flask/Node.js) and deployed it in a Kubernetes cluster using Deployment, Service, and Ingress. The project demonstrates skills in configuring YAML manifests, managing containerized applications, and integrating routing through Ingress Controller.

## ⚙️ Tech Stack
- Python (Flask)
- Docker
- Kubernetes (Minikube)
- NGINX Ingress Controller

## 🚀 Setup Guide
```bash
docker build -t damian/flask-k8s-app:latest app/
docker push damian/flask-k8s-app:latest
minikube start
kubectl apply -f k8s/