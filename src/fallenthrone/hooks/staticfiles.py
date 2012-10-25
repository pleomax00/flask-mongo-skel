from flask import g
from fallenthrone import app

@app.before_request
def staticfileconfig ():
    """ Lets keep some variables in the context of template processor """
    g.javascript_filelist = app.config['JSFILES']
    g.css_filelist = app.config['CSSFILES']
    g.MODE = app.config['ENV']

