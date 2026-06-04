# The .dockerignore file prevents sensitive files mentioned above from entering the context
FROM python:3.9-slim

WORKDIR /app

# Even with COPY ., .env and credentials.json are protected
COPY . .

CMD ["python", "app.py"]
