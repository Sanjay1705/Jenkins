from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

counter = 0

@app.route("/health")
def health():
    return "OK", 200

@app.route("/counter")
def counter_increment():
    global counter
    counter += 1
    r.set("counter", counter)
    return str(counter)
