# Alpine Linux is ideal for process isolation demonstrations
FROM alpine:latest

# The command keeps the container alive and prints its isolated hostname
# Run 'docker exec <container> ps aux' vs 'ps aux' on host to verify PID 1 isolation
CMD ["sh", "-c", "echo 'Container started with Hostname: '$HOSTNAME; echo 'Run "docker exec -it <container> ps aux" to see PID isolation.'; sleep 3600"]
