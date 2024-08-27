#!/usr/bin/env python3
"""A Flask app with internationalization support."""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
app.config.from_object('config.Config')
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """this will Retrieve the locale for a web page."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index():
    """The home/index page will be read."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


class Config:
    """Flask Babel configuration are always needed ."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
