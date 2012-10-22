from flask import Flask
from jinja2 import TemplateNotFound
from mongoengine import *
import os

connect ("fallenthrone")

app = Flask(__name__)
app.debug = True

import views

if __name__ == "__main__":
    app.run()


