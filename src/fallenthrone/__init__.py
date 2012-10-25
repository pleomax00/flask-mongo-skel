from flask import Flask
from jinja2 import TemplateNotFound
import middlewares
import mongoengine
import os

ENV = os.environ.get ("MODE", "DEVELOPMENT")
print "Loading %s..." % (ENV)

app = Flask(__name__)
if app.config['DEBUG']:
    app.debug = True

# Lets use Jade Template Engine instead.
app.jinja_env.add_extension ('pyjade.ext.jinja.PyJadeExtension')
try:
    app.config.from_object ('fallenthrone.settings.%sConfig' % ENV.title())
except ImportError:
    print "Failed to load configuration for %s, Loading default configuration." % ENV.title()
    app.config.from_object ('fallenthrone.settings.Config')

# Lets add middlewares.
# app.wsgi_app = middlewares.ContextMiddleware (app.wsgi_app)

# Lets connect to MongoDB
try:
    mongoengine.connect (app.config['DATABASE_NAME'], host = app.config['DATABASE_HOST'], port = app.config['DATABASE_PORT'], username = app.config['MONGO_USER'], password = app.config['MONGO_PASSWORD'])
except mongoengine.connection.ConnectionError:
    print "Cannot connect to MongoDB on %s:%s using user '%s' with password '*****'.." % ('localhost', app.config['DATABASE_PORT'], app.config['MONGO_USER'])
    sys.exit (1)

# Lets bring our views lying there into the application.
import hooks
import views

if __name__ == "__main__":
    app.run()

