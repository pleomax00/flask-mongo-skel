from mongoengine import *

class User (Document):
    username = StringField ()
    first_name = StringField ()
    last_name = StringField ()
    _password = StringField ()
    email = StringField ()

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

