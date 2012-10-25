#! /usr/bin/env python

import os, sys

# Thirdparty modules goes into 3rd party, lets add it to path.
dirname, filename = os.path.split (os.path.abspath (__file__))
sys.path.append (os.path.join (dirname, "thirdparty"))

from fallenthrone import app

# Our application port
# There are two application modes, PRODUCTION or DEVELOPMENT
# They are loaded as per the ENVironment variable set.
ENV = os.environ.get ("MODE", "DEVELOPMENT")
PORT = app.config['PORT']

# In production mode, we would want to use gevent to serve our requests.
using_gevent = False
if ENV == "PRODUCTION":
    try:
        from gevent.wsgi import WSGIServer
        using_gevent = True
    except ImportError:
        print "Cannot use WSGIServer, please install.."
        sys.exit (1)

if using_gevent:
    http_server = WSGIServer(('0.0.0.0', PORT), app)
    http_server.serve_forever()
else:
    print "This is Flask Development Server at %d (Don't use it in the production)..." % (PORT)
    app.run (host = '0.0.0.0', port = PORT)

