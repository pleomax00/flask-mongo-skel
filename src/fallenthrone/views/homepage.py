"""
@date Tue Oct  9 23:08:55 IST 2012

Serves the homepage.
"""

from fallenthrone import app
from flask import render_template, request
from flask.views import MethodView
from fallenthrone.models import User
from flask_login import *
import sys

class Index (MethodView):

    @login_required
    def get (self):
        """ Serves GET method """
        return render_template ('index.jade', **locals ())

app.add_url_rule ('/', view_func = Index.as_view ('index'))

