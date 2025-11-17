from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from flask + DevOps Lab!"

@app.route("/health")
def health():
	#In real world, you'd check DB, Redis, etc.
	return jsonify(status="ok", version="1.0.0"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
