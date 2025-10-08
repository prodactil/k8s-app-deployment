# Use an official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port 5000 and start app
EXPOSE 5000
CMD ["python", "app.py"]