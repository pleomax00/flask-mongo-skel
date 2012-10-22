"""
@date Tue Oct  9 23:08:55 IST 2012

Serves the homepage.
"""

from fallenthrone import app
from fallenthrone.models import User

@app.route ("/")
def index ():
    return "Home Page Goes Here.."
