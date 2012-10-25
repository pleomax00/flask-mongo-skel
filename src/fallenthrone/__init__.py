from flask import Flask
from jinja2 import TemplateNotFound
from mongoengine import *
import os

ENV = os.environ.get ("MODE", "DEVELOPMENT")

app = Flask(__name__)

# Lets use Jade Template Engine instead.
app.jinja_env.add_extension ('pyjade.ext.jinja.PyJadeExtension')
try:
    app.config.from_object ('fallenthrone.settings.%sConfig' % ENV.title())
except ImportError:
    print "Failed to load configuration for %s, Loading default configuration." % ENV.title()
    app.config.from_object ('fallenthrone.settings.Config')

# Lets connect to MongoDB
connect (app.config['DATABASE_NAME'])

if __name__ == "__main__":
    app.run()

