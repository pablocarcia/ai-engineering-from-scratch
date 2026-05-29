from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "AI dev API is running"
    })

@app.get("/qdrant")
def qdrant_status():
    try:
        response = requests.get("http://qdrant:6333/collections", timeout=5)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)