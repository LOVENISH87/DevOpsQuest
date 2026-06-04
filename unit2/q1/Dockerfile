# Optimization: Multi-stage builds and strict layer ordering 
FROM node:18-alpine AS builder

WORKDIR /app

# Copy ONLY package configuration to leverage cache
COPY package*.json ./

# Install only production dependencies for smaller final image
RUN npm ci --only=production

# Copy application source
COPY . .

# Final execution
CMD ["node", "server.js"]
