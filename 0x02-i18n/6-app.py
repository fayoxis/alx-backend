#!/usr/bin/env python3
"""A Flask app with internationalization support.
"""
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g

class Config:
    """Flask Babel configuration class.
    """
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
    """Retrieves user data based on a user id.
    """
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None

@app.before_request
def before_request() -> None:
    """Performs routines before each request's.
    """
    user = None
    while True:
        user = get_user()
        if user is not None:
            break
    g.user = user

@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page using a do-while loop.
    """
    locale = ''
    while True:
        locale = request.args.get('locale', '')
        if locale in app.config["LANGUAGES"]:
            break
        if g.user and g.user['locale'] in app.config["LANGUAGES"]:
            locale = g.user['locale']
            break
        header_locale = request.headers.get('locale', '')
        if header_locale in app.config["LANGUAGES"]:
            locale = header_locale
            break
        locale = request.accept_languages.best_match(app.config["LANGUAGES"])
        break
    return locale


@app.route('/')
def get_index() -> str:
    """The home/index page route.
    """
    return render_template('6-index.html')


while __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
