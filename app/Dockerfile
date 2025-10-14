# Use an official lightweight Python image
FROM python:3.12-slim-bullseye

# Upgrade system packages to fix vulnerabilities and remove cache
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install flask prometheus_client
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install prometheus-flask-exporter

# Copy app code
COPY . .

# Expose port 5000 and start app
EXPOSE 5000
CMD ["python", "app.py"]