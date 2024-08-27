#!/usr/bin/env python3
"""
A Basic Flask app with internationalization support.
app demonstrates use of Flask-Babel for localization and
handling different user locales and timezones.
"""
import pytz
from typing import Union, Dict
from flask_babel import Babel, format_datetime
from flask import Flask, render_template, request, g

class Config:
    """Represents a Flask Babel configuration.
    """
    # List of supported languages
    LANGUAGES = ["en", "fr"]
    # Default locale for the app
    BABEL_DEFAULT_LOCALE = "en"
    # Default timezone for the app
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

# Sample user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id from the query string.
    """
    login_id = request.args.get('login_as', '')
    if login_id:
        user_id = int(login_id)
        user_found = False
        user_key = 1
        # Loop through the users dictionary to find the user
        while not user_found:
            if user_key in users:
                if user_key == user_id:
                    user_found = True
                    return users[user_key]
            else:
                return None
            user_key += 1
    return None

@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    Stores the user details in the flask.g object for later use.
    """
    user = get_user()
    g.user = user

@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    The locale is determined by the following order:
    1. Query string parameter 'locale'
    2. User's locale (if logged in)
    3. Request header 'locale'
    4. Default locale from the app configuration
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = {}
    i = 0
    # Parse the query string into a dictionary
    while i < len(queries):
        query = queries[i]
        if '=' in query:
            key, value = query.split('=')
            query_table[key] = value
        else:
            query_table[query] = ''
        i += 1
    locale = query_table.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    user_details = getattr(g, 'user', None)
    if user_details and user_details['locale'] in app.config["LANGUAGES"]:
        return user_details['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']

@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves the timezone for a web page.
    The timezone is determined by the following order:
    1. Query string parameter 'timezone'
    2. User's timezone (if logged in)
    3. Default timezone from the app configuration
    """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def get_index() -> str:
    """The home/index page.
    Formats current time using user's locale and timezone.
    """
    g.time = format_datetime()
    return render_template('index.html')

while __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
