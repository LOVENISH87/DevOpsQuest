# Simple Flask application to demonstrate consistent environment execution
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the isolated Python container! Environment is consistent."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
