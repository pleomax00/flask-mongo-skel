"""
@date Thu Nov  1 16:14:48 IST 2012

Shows user /album/handle page
"""

from fallenthrone import app
from flask import render_template, request
from flask.views import MethodView
from fallenthrone.models import User, CacheData
from flask_login import *

from fallenthrone.lib.tweetparser import TweetParser
import sys

class Album (MethodView):

    def read_images (self, handle):
        tparser = TweetParser (app.config['TWITTER_CONSUMER_KEY'], app.config['TWITTER_CONSUMER_SECRET'], current_user.twitter_access_key, current_user.twitter_secret_key)
        images = tparser.parse (handle)
        return images

    def get (self, handle):
        images = self.read_images (handle)
        #images = CacheData.getset ("images", current_user.handle + ":" + handle, self.read_images, [handle])
        print images
        return render_template ('album.jade', **locals ())

app.add_url_rule ('/album/<handle>', view_func = Album.as_view ('album'))
