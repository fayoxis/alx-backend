#!/usr/bin/env python3
"""
Flask application with internationalization support.
This app demonstrates locale selection and user management.
"""

from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Configuration class for Flask Babel settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Fetch user details based on login_as parameter.
    Returns user dict if found, None otherwise.
    """
    login_id = request.args.get('login_as', '')
    return users.get(int(login_id), None) if login_id else None


@app.before_request
def before_request() -> None:
    """Middleware to set global user for each request."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match locale using a do-while loop structure.
    Checks URL parameters, user preferences, and request headers.
    """
    locale = None
    while True:
        # Check URL parameters
        locale = request.args.get('locale', '')
        if locale in app.config["LANGUAGES"]:
            break
        
        # Check user settings
        if g.user and g.user['locale'] in app.config["LANGUAGES"]:
            locale = g.user['locale']
            break
        
        # Check request headers
        header_locale = request.headers.get('locale', '')
        if header_locale in app.config["LANGUAGES"]:
            locale = header_locale
            break
        
        # Fall back to best match from accepted languages
        locale = request.accept_languages.best_match(app.config["LANGUAGES"])
        break
    
    return locale


@app.route('/')
def get_index() -> str:
    """Render the home page."""
    return render_template('6-index.html')


while __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
