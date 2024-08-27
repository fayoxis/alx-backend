#!/usr/bin/env python3
"""A Flask app with internationalization support using Babel.
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
    """Retrieve user data based on login_id from request args.
    """
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """Set user data in the global context before each request.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Determine the best locale for the current request.
    """
    locale_choices = [
        request.args.get('locale', ''),
        g.user and g.user['locale'],
        request.headers.get('locale', ''),
    ]
    while locale_choices:
        locale = locale_choices.pop(0)
        if locale in app.config["LANGUAGES"]:
            return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Render the index page.
    """
    return render_template('6-index.html')


while __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
