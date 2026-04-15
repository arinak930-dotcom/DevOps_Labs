from flask import Flask
import os, socket

app = Flask(__name__)

@app.route("/")
def hello():
    return f"<h1>Hello from Kubernetes! v2 HELM</h1><p>Pod: {socket.gethostname()}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
