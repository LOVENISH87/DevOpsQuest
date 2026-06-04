FROM ubuntu:latest
WORKDIR /project
COPY  . .
# RUN "curl https://www.example.com/" or "apt update && upgrade"
RUN apt-get update && apt install -y curl
# COPY t.txt .
# EXPOSE 8008
RUN echo "hello world" > test.txt
