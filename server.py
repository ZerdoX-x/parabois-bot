"""
Simple http server that will keep bot alive
"""

from flask import Flask

app = Flask('')

@app.route('/')
def index():
    """Get response"""
    return "Parabois bot is alive."
