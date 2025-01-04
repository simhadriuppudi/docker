# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_bharath():
    return "Hello simha!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Dockerfile
# Use the official Python image from the DockerHub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir Flask

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
