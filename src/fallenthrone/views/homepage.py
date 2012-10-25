"""
@date Tue Oct  9 23:08:55 IST 2012

Serves the homepage.
"""

from fallenthrone import app
from flask import render_template, request
from flask.views import MethodView
from fallenthrone.models import User
import sys

class Index (MethodView):

    def get (self):
        """ Serves GET method """
        name = "yahoo"
        #u = User (username = 'pleomax00', first_name = 'Shamail', last_name = 'Tayyab', email = 'pleomax00@gmail.com')
        #u.save ()
        return render_template ('index.jade', name=name)

app.add_url_rule ('/', view_func = Index.as_view ('index'))

