
class Config (object):
    DEBUG = False
    TESTING = False
    PORT = 5000
    DATABASE_NAME = "fallenthrone"

class DevelopmentConfig (Config):
    DEBUG = True
    DATABASE_NAME = "fallenthrone_dev"

class ProductionConfig (Config):
    DEBUG = False
    PORT = 8765
    DATABASE_NAME = "fallenthrone_prod"
