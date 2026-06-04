FROM nginx:alpine

# EXPOSE acts as documentation indicating which port the application listens on
EXPOSE 80

# Note: The port must still be published at runtime (e.g., docker run -p 8080:80)
CMD ["nginx", "-g", "daemon off;"]
