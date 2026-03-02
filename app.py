from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h2>Kubernetes Web App</h2>
    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Environment:</b> {os.getenv('ENV','dev')}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
