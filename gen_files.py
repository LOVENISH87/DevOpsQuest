import os

base_dir = "/home/batman/DevQuest"
structure = {
    "1": ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"],
    "2": ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"],
    "unit3": ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"]
}

files = {}

# Unit 1
files["1/q1/Dockerfile"] = """FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
CMD ["python", "app.py"]"""
files["1/q1/app.py"] = """from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello"
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)"""

files["1/q2/Dockerfile"] = """FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip git curl
WORKDIR /workspace
CMD ["/bin/bash"]"""

files["1/q3/docker-compose.yml"] = """version: '3.8'
services:
  team_a_python:
    image: python:3.12-slim
    command: tail -f /dev/null
  team_b_node:
    image: node:18-slim
    command: tail -f /dev/null"""

files["1/q4/docker-compose.yml"] = """version: '3.8'
services:
  analytics:
    image: python:3.9-slim
    command: python -c "x = 'a' * 10**8; import time; time.sleep(3600)"
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 200M"""

files["1/q5/Dockerfile"] = """FROM alpine:latest
CMD ["sh", "-c", "echo Hostname: $HOSTNAME && ps aux && sleep 3600"]"""

files["1/q6/docker-compose.yml"] = """version: '3.8'
services:
  webapp:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - app_data:/usr/share/nginx/html
volumes:
  app_data:"""

files["1/q7/docker-compose.yml"] = """version: '3.8'
services:
  frontend:
    image: nginx:alpine
    ports:
      - "8080:80"
    networks:
      - app_network
  backend:
    image: node:18-slim
    command: sh -c "echo 'Backend running' && tail -f /dev/null"
    networks:
      - app_network
networks:
  app_network:
    driver: bridge"""

files["1/q8/Dockerfile"] = """FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]"""
files["1/q8/requirements.txt"] = "flask"
files["1/q8/app.py"] = ""

files["1/q9/Dockerfile"] = """FROM ubuntu:22.04
RUN apt-get update && apt-get install -y iputils-ping curl vim
CMD ["/bin/bash"]"""

files["1/q10/Dockerfile"] = """FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80"""
files["1/q10/index.html"] = """<h1>Event</h1>"""

# Unit 2
files["2/q1/Dockerfile"] = """FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
CMD ["node", "server.js"]"""
files["2/q1/package.json"] = """{"name":"app","version":"1.0.0"}"""
files["2/q1/server.js"] = """console.log("Running");"""

files["2/q2/.dockerignore"] = """.env
credentials.json
.git
node_modules"""
files["2/q2/Dockerfile"] = """FROM python:3.9-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]"""

files["2/q3/Dockerfile"] = """FROM alpine:latest
ENTRYPOINT ["echo"]
CMD ["Started"]"""

files["2/q4/Dockerfile"] = """FROM node:18-alpine
ENV APP_ENV=production
ENV DB_URL=URl
WORKDIR /app
COPY server.js .
CMD ["node", "server.js"]"""
files["2/q4/server.js"] = """console.log(process.env.APP_ENV);"""

files["2/q5/Dockerfile"] = """FROM nginx:alpine
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]"""

files["2/q6/docker-compose.yml"] = """version: '3.8'
services:
  frontend:
    image: nginx:alpine
    networks:
      - micro-net
  backend:
    image: alpine
    command: tail -f /dev/null
    networks:
      - micro-net
networks:
  micro-net:
    driver: bridge"""

files["2/q7/docker-compose.yml"] = """version: '3.8'
services:
  app:
    image: alpine
    command: tail -f /dev/null
    volumes:
      - appdata:/data
volumes:
  appdata:"""

files["2/q8/Dockerfile"] = """FROM alpine:latest
RUN echo "Initial" > /test.txt
CMD ["tail", "-f", "/dev/null"]"""

files["2/q9/Dockerfile"] = """FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html"""
files["2/q9/index.html"] = """<h1>V1</h1>"""

files["2/q10/Dockerfile"] = """FROM alpine:latest
CMD ["echo", "Private image"]"""

# Unit 3
files["unit3/q1/docker-compose.yml"] = """version: '3.8'
services:
  frontend:
    image: nginx:alpine
    ports:
      - "80:80"
  backend:
    image: node:18-alpine
    command: tail -f /dev/null
  database:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root"""

files["unit3/q2/docker-compose.yml"] = """version: '3.8'
services:
  database:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
  backend:
    image: node:18-alpine
    command: tail -f /dev/null
    depends_on:
      - database"""

files["unit3/q3/docker-compose.yml"] = """version: '3.8'
services:
  backend:
    image: node:18-alpine
    environment:
      - DB_HOST=mongodb
      - DB_URL=URl
    command: tail -f /dev/null
  mongodb:
    image: mongo:latest"""

files["unit3/q4/docker-compose.yml"] = """version: '3.8'
services:
  app:
    image: alpine
    command: tail -f /dev/null
    secrets:
      - db_password
secrets:
  db_password:
    file: ./db_password.txt"""
files["unit3/q4/db_password.txt"] = """secretpassword"""

files["unit3/q5/docker-compose.yml"] = """version: '3.8'
services:
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: wordpress
  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_USER: root
      WORDPRESS_DB_PASSWORD: password
      WORDPRESS_DB_NAME: wordpress"""

files["unit3/q6/docker-compose.yml"] = """version: '3.8'
services:
  nodeapp:
    build: .
    ports:
      - "3000:3000"
  mongodb:
    image: mongo:latest"""
files["unit3/q6/Dockerfile"] = """FROM node:18-alpine
WORKDIR /app
COPY index.js .
CMD ["node", "index.js"]"""
files["unit3/q6/index.js"] = """console.log('App running');"""

files["unit3/q7/docker-compose.yml"] = """version: '3.8'
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: appdb
  springboot:
    image: openjdk:17-oracle
    command: tail -f /dev/null
    environment:
      - SPRING_DATASOURCE_URL=URl
      - SPRING_DATASOURCE_USERNAME=postgres
      - SPRING_DATASOURCE_PASSWORD=pass"""

files["unit3/q8/docker-compose.yml"] = """version: '3.8'
services:
  backend:
    image: node:18-alpine
    command: tail -f /dev/null"""

files["unit3/q9/docker-compose.yml"] = """version: '3.8'
services:
  gateway:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
  userservice:
    image: node:18-alpine
    command: tail -f /dev/null
  orderservice:
    image: node:18-alpine
    command: tail -f /dev/null"""
files["unit3/q9/nginx.conf"] = """events {}
http {
    server {
        listen 80;
        location /user/ {
            proxy_pass URl;
        }
        location /order/ {
            proxy_pass URl;
        }
    }
}"""

files["unit3/q10/docker-compose.yml"] = """version: '3.8'
services:
  database:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: password
    volumes:
      - dbdata:/var/lib/mysql
volumes:
  dbdata:"""

for folder in structure.keys():
    for sub in structure[folder]:
        os.makedirs(os.path.join(base_dir, folder, sub), exist_ok=True)

for path, content in files.items():
    full_path = os.path.join(base_dir, path)
    with open(full_path, "w") as f:
        f.write(content)
