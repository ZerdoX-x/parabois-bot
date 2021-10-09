"""
Simple http server that will keep bot alive
"""

from threading import Thread
from flask import Flask
from waitress import serve

app = Flask('')

@app.route('/')
def home():
    """Get response"""
    return "Parabois bot is alive."

def run():
    """Start server"""
    serve(app, host="0.0.0.0", port=8080)

def keep_alive():
    """Create new thread"""
    thread = Thread(target=run)
    thread.start()
