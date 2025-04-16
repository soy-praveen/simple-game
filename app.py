from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log-action', methods=['POST'])
def log_action():
    data = request.get_json()
    action = data.get('action')

    if action == "ddos":
        app.logger.warning("🚨 DDoS Attack Detected!")
        return jsonify({'status': 'DDoS detected'}), 200

    return jsonify({'status': 'Action logged'}), 200

if __name__ == '__main__':
    app.run(debug=True)
