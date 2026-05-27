
import os
from flask import Flask, jsonify

app = Flask(__name__)


def get_api_key():
    key = os.environ.get("API_KEY")
    if not key:
        return None
    return key


@app.route("/")
def hello():
    return "Hello, DevOps World!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/secret-status")
def secret_status():
  
    key = get_api_key()
    if key:
        return jsonify({
            "secret_loaded": True,
            "secret_length": len(key),
            "message": "API key successfully loaded from Vault"
        })
    return jsonify({"secret_loaded": False}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
