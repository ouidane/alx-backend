#!/usr/bin/python3
"""
Flask app with Babel configuration
"""

import babel
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration for Babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Route for the index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
