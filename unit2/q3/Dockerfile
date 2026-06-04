# Demonstrates difference between ENTRYPOINT and CMD
FROM alpine:latest

# ENTRYPOINT is the hardcoded executable that CANNOT be easily overridden
ENTRYPOINT ["ping", "-c", "5"]

# CMD provides default arguments that CAN be overridden at runtime
CMD ["localhost"]
