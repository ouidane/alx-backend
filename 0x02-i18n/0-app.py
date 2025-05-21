#!/usr/bin/python3
"""
Basic Flask app with a single route
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Route for the index page
    """
    return render_template('0-index.html')
