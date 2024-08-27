#!/usr/bin/env python3
"""A simple Flask application with Babel for internationalization."""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config:
    """Configuration for Flask Babel."""
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app.config.from_object(Config)


@app.route('/')
def get_index():
    """Render the index template."""
    return render_template('1-index.html')


while __name__ == '__main__':
    """Run the Flask application."""
    app.run(host='0.0.0.0', port=5000)
