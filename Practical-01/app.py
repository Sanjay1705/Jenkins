from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True,
)

@app.route("/health")
def health():
   
    try:
        if r.ping():
            return jsonify(status="ok"), 200
    except Exception as e:
        return jsonify(status="redis-unavailable", error=str(e)), 500

@app.route("/")
def index():
   
    try:
        counter = r.incr("visits")
        return jsonify(message="Hello from Flask + Redis", visits=int(counter))
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000)
