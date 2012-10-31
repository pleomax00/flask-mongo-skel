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

# Lets initialize our session engine
app.secret_key = app.config['APP_SECRET_KEY']

# Lets add our middlewares.
# app.wsgi_app = middlewares.ContextMiddleware (app.wsgi_app)

# Lets connect to MongoDB
try:
    mongoengine.connect (app.config['DATABASE_NAME'], host = app.config['DATABASE_HOST'], port = app.config['DATABASE_PORT'], username = app.config['MONGO_USER'], password = app.config['MONGO_PASSWORD'])
except mongoengine.connection.ConnectionError:
    print "Cannot connect to MongoDB on %s:%s using user '%s' with password '*****'.." % ('localhost', app.config['DATABASE_PORT'], app.config['MONGO_USER'])
    sys.exit (1)    # Can't work without Database!

# Lets add our LoginManager
from models.users import User
from flask_login import *
login_manager = LoginManager()
#login_manager.anonymous_user = Anonymous
login_manager.login_view = "/auth/login"
@login_manager.user_loader
def load_user (id):
    try:
        return User.objects.get (handle = str(id))
    except User.DoesNotExist:
        return None
login_manager.setup_app (app)

# Lets bring our views lying there into the application.
import hooks
import views

# Finally run our application.
if __name__ == "__main__":
    app.run()

