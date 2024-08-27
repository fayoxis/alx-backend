#!/usr/bin/env python3
"""A Flask app with internationalization support."""
import pytz
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Flask Babel configuration class."""
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
    """Retrieves a user based on a user id."""
    login_id = request.args.get('login_as', '')
    while login_id:
        user = users.get(int(login_id), None)
        if user:
            return user
    return None


@app.before_request
def before_request() -> None:
    """Retrieves the user before each request."""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    locale = ''
    while locale not in app.config["LANGUAGES"]:
        locale = request.args.get('locale', '')
        if locale in app.config["LANGUAGES"]:
            return locale
        if g.user and g.user['locale'] in app.config["LANGUAGES"]:
            return g.user['locale']
        header_locale = request.headers.get('locale', '')
        if header_locale in app.config["LANGUAGES"]:
            return header_locale
        return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves the timezone for a web page."""
    timezone = request.args.get('timezone', '').strip()
    while not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def get_index() -> str:
    """This is home/index page."""
    return render_template('7-index.html')


while __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
