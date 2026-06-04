# Base image using Ubuntu LTS for stability
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install required developer tools: Python, Pip, Git, and Curl
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up a working directory
WORKDIR /workspace

# Default command opens a bash shell for the student
CMD ["/bin/bash"]
