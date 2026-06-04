# Demonstrates proper Layering for Build Cache Optimization
FROM python:3.9-slim

WORKDIR /app

# Step 1: Copy ONLY dependency list initially. 
# This prevents rebuilding the pip install layer when application code changes.
COPY requirements.txt .

# Step 2: Install dependencies. (Cached if requirements.txt doesn't change)
RUN pip install --no-cache-dir -r requirements.txt

# Step 3: Copy source code AFTER dependencies.
# Changes in app.py will only rebuild this layer downwards.
COPY . .

CMD ["python", "app.py"]
