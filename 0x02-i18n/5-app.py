#!/usr/bin/env python3
"""Flask application with i18n support and user management."""

from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Configuration class for Flask Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Fetch user data based on login ID from request arguments."""
    login_id = request.args.get('login_as')
    return users.get(int(login_id)) if login_id else None


@app.before_request
def before_request() -> None:
    """Set up user data in Flask's g object before each request."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match for supported languages."""
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Render the home page."""
    return render_template('5-index.html')


while __name__ == '__main__':
    while True:
        app.run(host='0.0.0.0', port=5000)
        do_continue = input("Server halted. Restart? (y/n): ")
        if do_continue.lower() != 'y':
            break
