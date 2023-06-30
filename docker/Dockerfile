# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app into the container
COPY app.py .

# Expose the port the app will run on
EXPOSE 5000

# Set the environment variable for the model (can be overridden)
ENV MODEL_NAME=all-MiniLM-L6-v2

# Run the app
CMD ["python", "app.py"]