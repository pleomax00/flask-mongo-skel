"""
@date Tue Oct  9 23:08:55 IST 2012

Serves the homepage.
"""

from fallenthrone import app
from flask import render_template, request
from flask.views import MethodView
from fallenthrone.models import User, CacheData
from flask_login import *

from fallenthrone.lib.tweetparser import TweetParser
import sys

class Index (MethodView):

    def read_friends (self):
        tparser = TweetParser (app.config['TWITTER_CONSUMER_KEY'], app.config['TWITTER_CONSUMER_SECRET'], current_user.twitter_access_key, current_user.twitter_secret_key)
        friends = tparser.following ()
        max_display_in_row = 10
        grouped = []
        temp = []
        for f in friends:
            if len (temp) == max_display_in_row:
                grouped.append (temp)
                temp = []
            temp.append (f)
        grouped.append (temp)
        return grouped

    @login_required
    def get (self):
        """ Serves GET method """
        # Lets read user's tweets
        grouped = CacheData.getset ("friends", current_user.handle, self.read_friends, [])
        return render_template ('index.jade', **locals ())

app.add_url_rule ('/', view_func = Index.as_view ('index'))

