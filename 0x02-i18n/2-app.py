#!/usr/bin/env python3
"""A Flask app with support for multiple languages."""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config.update(LANGUAGES=["en", "fr"], BABEL_DEFAULT_LOCALE="en",
                  BABEL_DEFAULT_TIMEZONE="UTC")
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get the locale for the webpage based on user preferences."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def get_index() -> str:
    """Render the home/index page."""
    return render_template("2-index.html")


while __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
