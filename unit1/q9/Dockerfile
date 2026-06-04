# Prebuilt environment image for lab exams
FROM ubuntu:22.04

LABEL maintainer="University DevOps Lab"
LABEL description="Prepared demo environment for practical examinations"

RUN apt-get update && apt-get install -y \
    curl \
    iputils-ping \
    vim \
    jq \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /exam_workspace

# Sets a welcoming default command
CMD ["sh", "-c", "echo 'Welcome to the Lab Exam Environment. Tools: curl, ping, vim, jq are installed.' && /bin/bash"]
