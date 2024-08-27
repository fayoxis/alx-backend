#!/usr/bin/env python3
"""
Flask application with internationalization support.
This app demonstrates basic i18n functionality using Flask-Babel.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """
    Configuration class for Flask Babel settings.
    Defines supported languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages.
    
    Checks query parameters for a 'locale' field first.
    Falls back to the best match from the Accept-Language header.
    
    Returns:
        str: The selected locale code.
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = {}
    i = 0
    if queries:
        while True:
            query = queries[i]
            if '=' not in query:
                query = '{}='.format(query)
            key, value = query.split('=')
            query_table[key] = value
            i += 1
            if i >= len(queries):
                break

    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Route handler for the home page.
    
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000)
