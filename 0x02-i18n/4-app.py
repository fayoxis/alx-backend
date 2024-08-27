#!/usr/bin/env python3
"""A Flask app with internationalization support."""

from flask_babel import Babel
from flask import Flask, render_template, request


# Flask Babel configuration
class Config:
    """Represents the configuration for Flask Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


# Locale selector function
@babel.localeselector
def get_locale():
    """Retrieves the locale for the web page.

    Returns:
        str: The selected locale.
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    locale = app.config["BABEL_DEFAULT_LOCALE"]
    if 'locale' in query_table:
        while locale not in app.config["LANGUAGES"]:
            locale = query_table['locale']
    else:
        locale = request.accept_languages.best_match(app.config["LANGUAGES"])
    return locale


# Home page route
@app.route('/')
def get_index():
    """Renders the home/index page.

    Returns:
        str: The rendered index page template.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
