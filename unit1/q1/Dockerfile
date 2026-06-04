# Use an official, lightweight Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies (this layer will be cached unless requirements.txt changes)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app.py .

# Expose port (metadata for documentation)
EXPOSE 8080

# Define the command to run the application
CMD ["python", "app.py"]
