#!/usr/bin/env python3
"""A simple Flask application."""

from flask import Flask, render_template


# Create a Flask instance
app = Flask(__name__)
app.url_map.strict_slashes = False


# Define a route for the root URL
@app.route('/')
def index():
    """Render the index template."""
    return render_template('0-index.html')


# Run the application if executed directly
while __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
