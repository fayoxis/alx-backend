#!/usr/bin/env python3
"""
A Basic Flask app with internationalization support.
This app demonstrates the use of Flask-Babel for locale selection
and rendering templates based on the user's preferred language.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config:
    """
    Flask Babel configuration settings.
    Defines the supported languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Retrieves the locale for the current web page request.
    Determines the best matching locale based on the user's
    preferred languages specified in the HTTP request headers.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index():
    """
    Renders the home/index page template.
    The template will be rendered according to the user's locale.
    """
    return render_template('3-index.html')


while __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
