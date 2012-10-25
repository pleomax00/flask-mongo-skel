"""
@date Tue Oct  9 23:08:55 IST 2012

Serves the homepage.
"""

from fallenthrone import app
from flask import render_template
from fallenthrone.models import User

@app.route ("/")
def index ():
    name = "yahoo"
    return render_template ('hello.jade', name=name)
