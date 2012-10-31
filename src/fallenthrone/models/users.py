from mongoengine import *

class User (Document):
    handle = StringField ()
    first_name = StringField ()
    last_name = StringField ()
    _password = StringField ()
    email = StringField ()
    active = BooleanField (default = True)

    twitter_access_key = StringField ()
    twitter_secret_key = StringField ()

    @property
    def get_full_name (self):
        """ Get's user's full name """
        return "%s %s" % (self.first_name, self.last_name)
    
    def auth (self, password):
        if self._hash (password) == self._password:
            return True
        else:
            return False

    def _hash (self, string):
        return hashlib.sha1 (string + "SOME_SALT_HERE").hexdigest ()

    def setpassword (self, password):
        self._password = self._hash (password)

    def is_active (self):
        return self.active
    
    def get_id (self):
        return unicode (self.handle)

    def is_anonymous (self):
        return False

    def is_authenticated (self):
        return True

