"""
@date Tue Oct  9 23:08:55 IST 2012

Serves the homepage.
"""

from fallenthrone import app
from flask import render_template
from flask.views import MethodView
from fallenthrone.models import User

@app.route ("/")
def index ():
    name = "haha"
    u = User (username = 'pleomax00', first_name = 'Shamail', last_name = 'Tayyab', email = 'pleomax00@gmail.com')
    u.save ()
    return render_template ('hello.jade', name=name)

class Index (MethodView):

    def get (self):
        name = "yahoo"
        #global request
        #print request
        print "ha"
        u = User (username = 'pleomax00', first_name = 'Shamail', last_name = 'Tayyab', email = 'pleomax00@gmail.com')
        u.save ()
        return render_template ('hello.jade', name=name)

#index_view = Index.as_view ('index')
#app.add_url_rule ('/', view_func = Index.as_view ('users'))
