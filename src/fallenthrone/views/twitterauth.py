"""
@date Wed Oct 31 17:23:00 IST 2012

Twitter authentication handlers.
"""

from fallenthrone import app
from flask import render_template, request, redirect, session
from flask.views import MethodView
from fallenthrone.models import User
import oauth2 as oauth
from cgi import parse_qsl
from flask_login import *
import sys

class TwitterAuth (MethodView):

    def get (self):
        """ Handles /auth/twitter """
        oauth_consumer = oauth.Consumer (key=app.config['TWITTER_CONSUMER_KEY'], secret=app.config['TWITTER_CONSUMER_SECRET'])
        oauth_client = oauth.Client (oauth_consumer)
        resp, content = oauth_client.request (app.config['REQUEST_TOKEN_URL'], 'GET')
        if resp['status'] != '200':
            return 'Error From Twitter'
        else:
            request_token = dict (parse_qsl(content))

        session['request_token'] = request_token
        callback_url = "http://%s/auth/callback" % (request.host)
        redirect_to = '%s?oauth_token=%s' % (app.config['AUTHORIZATION_URL'], request_token['oauth_token'])
        return redirect (redirect_to)


class TwitterCallback (MethodView):

    def get (self):
        """ Handles twitter callback """
        oauth_consumer = oauth.Consumer (key=app.config['TWITTER_CONSUMER_KEY'], secret=app.config['TWITTER_CONSUMER_SECRET'])
        
        token = oauth.Token (session['request_token']['oauth_token'], session['request_token']['oauth_token_secret'])
        oauth_client  = oauth.Client (oauth_consumer, token)
        resp, content = oauth_client.request (app.config['ACCESS_TOKEN_URL'], method='GET' )
        access_token  = dict (parse_qsl(content))
        if resp['status'] != '200':
            raise Exception ( "The request for a Token did not succeed" )
        else:
            tw_access = access_token['oauth_token']
            tw_secret = access_token['oauth_token_secret']
            screen_name = access_token['screen_name'].strip ()
            print tw_access, tw_secret, screen_name
            try:
                u = User.objects.get (handle = screen_name)
            except User.DoesNotExist:
                u = User (handle = screen_name)
            u.twitter_access_key = tw_access
            u.twitter_secret_key = tw_secret
            u.save ()
            print login_user (u, remember = "yes") 

        return redirect ("/")


class Logout (MethodView):

    def get (self):
        logout_user ()
        return redirect ("/")


class Login (MethodView):

    def get (self):
        print current_user.is_authenticated ()
        return render_template ("login.jade", **locals())


app.add_url_rule ('/auth/twitter', view_func = TwitterAuth.as_view ('twitterauth'))
app.add_url_rule ('/auth/callback', view_func = TwitterCallback.as_view ('twittercallback'))
app.add_url_rule ('/auth/logout', view_func = Logout.as_view ('logout'))
app.add_url_rule ('/auth/login', view_func = Login.as_view ('login'))

