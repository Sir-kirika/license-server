from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)
SALT = "Sri_Jimmy"  # Replace with something private before production

@app.route("/")
def home():
    return "License Server Running"

@app.route("/verify", methods=["GET"])
def verify():
    device_id = request.args.get("device_id", "").strip()
    license_key = request.args.get("license_key", "").strip().upper()

    expected = hashlib.sha256((device_id + SALT).encode()).hexdigest()[:16].upper()

    return jsonify({
        "status": "valid" if license_key == expected else "invalid"
    })
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render will set this
    app.run(host="0.0.0.0", port=port)

