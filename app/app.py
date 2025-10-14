from flask import Flask, Response
from prometheus_client import generate_latest, Counter
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
REQUEST_COUNT = Counter('requests_total', 'Total HTTP Requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return {"message": "Hello from Kubernetes!"}

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    # 0.0.0.0 permite acces din alte pod-uri / servicii
    app.run(host="0.0.0.0", port=5000)