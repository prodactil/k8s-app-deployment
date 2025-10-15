## 🧩 Kubernetes App Deployment
---

## 📘 Overview
I created a containerized web application (Flask) and deployed it in a Kubernetes cluster using Deployment, Service, and Ingress. The project demonstrates skills in configuring YAML manifests, managing containerized applications, and integrating routing through Ingress Controller.

---

## 🧱 Project Structure
```bash
k8s-monitoring/  
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
├── app
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── k8s
│   ├── deployment.yaml
│   ├── ingress.yaml
│   └── service.yaml
└── README.md
```
---

## ⚙️ Tech Stack
- Python (Flask-App)
- Docker
- Kubernetes (Docker Desktop)
- NGINX Ingress Controller

---

## 🌐 Access
- http://flask.local

---

## 🚀 Setup Guide
--> Add in /etc/hosts this line <--

--> 127.0.0.1 flask.local <-- 

---
