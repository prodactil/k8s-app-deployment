from flask import Flask
from prometheus_client import generate_latest, Counter

app = Flask(__name__)
REQUEST_COUNT = Counter('flask_request_count', 'Number of requests received')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return {"message": "Hello from Kubernetes!"}

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}