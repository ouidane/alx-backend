#!/usr/bin/python3
"""
Flask app with locale and timezone selection
"""
import pytz
from typing import (
    Dict, Union
)

from flask import Flask
from flask import g, request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Babel config with supported languages and defaults
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Retrieve user from mock DB using ?login_as= ID
    """
    return users.get(int(id), {})


@babel.localeselector
def get_locale() -> str:
    """
    Select locale from URL > user > header > default
    """
    options = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale


@babel.timezoneselector
def get_timezone() -> str:
    """
    Select timezone from URL > user > default (UTC)
    """
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        return pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request() -> None:
    """
    Set g.user based on login_as
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render main page
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()