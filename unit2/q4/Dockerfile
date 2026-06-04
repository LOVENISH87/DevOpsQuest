# Environment configuration via ENV variables
FROM node:18-alpine

# Set default Environment variables (can be overridden via docker run -e)
ENV APP_ENV=production
ENV DB_URL=URl

WORKDIR /app

COPY server.js .

CMD ["node", "server.js"]
