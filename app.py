from flask import Flask, request, render_template, jsonify
import logging
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Simple in-memory store to simulate rate monitoring
request_times = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log-action', methods=['POST'])
def log_action():
    global request_times
    now = time.time()
    request_times = [t for t in request_times if now - t < 1.0]  # Keep only last 1 second
    request_times.append(now)

    if len(request_times) > 50:
        app.logger.warning("🚨 DDoS Attack Detected! Rate exceeded: %d req/sec", len(request_times))
        return jsonify({'status': 'DDoS detected'}), 429

    return jsonify({'status': 'Request logged'}), 200

if __name__ == '__main__':
    app.run(debug=True)
