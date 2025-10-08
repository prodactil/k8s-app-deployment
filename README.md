## 🧩 Kubernetes App Deployment

## 📘 Overview
I created a containerized web application (Flask/Node.js) and deployed it in a Kubernetes cluster using Deployment, Service, and Ingress. The project demonstrates skills in configuring YAML manifests, managing containerized applications, and integrating routing through Ingress Controller.

## ⚙️ Tech Stack
- Python (Flask)
- Docker
- Kubernetes (Minikube)
- NGINX Ingress Controller

## 🌐 Access
- http://flask.local
- http://flask.local/health

## 🚀 Setup Guide
--> Add in /etc/hosts this line <--
--> 127.0.0.1 flask.local <-- 
```bash
docker build -t prodactil/flask-k8s-app:latest app/
docker push prodactil/flask-k8s-app:latest
minikube start
minikube addons enable ingress
kubectl apply -f k8s/