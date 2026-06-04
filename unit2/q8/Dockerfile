# Demonstrating Copy-on-Write behavior
FROM alpine:latest

# This modifies the original image layer
RUN echo "Original Image Content" > /app_data.txt

# Modifications strictly made at runtime inside the running container 
# will stay in the thin read/write layer and won't affect new containers.
CMD ["tail", "-f", "/dev/null"]
