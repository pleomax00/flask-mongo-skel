"""
@date Tue Oct  9 23:08:04 IST 2012

Gives flask's documentation on tips at http://localhost/docs
"""

from flask import Blueprint
from fallenthrone import app
from flask import make_response, send_file
import os

docs_pages = Blueprint ('docs_pages', __name__)

@docs_pages.route ('/', defaults={'filename': 'index.html'})
@docs_pages.route ('/<path:filename>')
def docserver (filename):
    ifile = os.path.join ("docs", "flask", filename)
    return send_file (ifile)

app.register_blueprint (docs_pages, url_prefix='/docs')

