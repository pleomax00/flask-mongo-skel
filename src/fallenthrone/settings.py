import os

class Config (object):
    DEBUG = False
    TESTING = False
    PORT = 5000
    APP_SECRET_KEY = "rule number 1: you will not touch anything!"
    DATABASE_HOST = 'localhost'
    DATABASE_NAME = "fallenthrone"
    DATABASE_PORT = 27017
    MONGO_USER = 'fallenthrone'
    MONGO_PASSWORD = 'mongo'

    JSFILES = ['effects.js']
    CSSFILES = ['style.css']

    ENV = os.environ.get ("MODE", "DEVELOPMENT")

    TWITTER_CONSUMER_KEY = "y85IR4x0fwu7SCUeWN2xsQ"
    TWITTER_CONSUMER_SECRET = "9qvw00vE9dwaeivtykR9fvpYEiXwBWdllAOYSGOZs"
    REQUEST_TOKEN_URL = 'https://twitter.com/oauth/request_token'
    ACCESS_TOKEN_URL  = 'https://twitter.com/oauth/access_token'
    AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
    SIGNIN_URL        = 'https://twitter.com/oauth/authenticate'

    CACHE_FRIENDS_INTERVAL = 3600
    CACHE_IMAGES_INTERVAL = 3600

    def __init__ (self):
        raise Exception ("Cannot initialize Config directly, use subclasses.")


class DevelopmentConfig (Config):
    DEBUG = True
    DATABASE_NAME = "fallenthrone_dev"


class ProductionConfig (Config):
    DEBUG = False
    PORT = 8765
    DATABASE_NAME = "fallenthrone_prod"

