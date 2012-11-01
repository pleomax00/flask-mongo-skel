from mongoengine import *
from fallenthrone import app
import time, json

class CacheData (Document):
    key = StringField ()
    type = StringField (default = "user")
    data = StringField ()
    timestamp = IntField (default=time.time)

    @classmethod
    def getset (cls, type, handle, fn_on_fail, params_as_list):
        """ Try to get something from cache, if it does not exists
        execute fn_on_fail passing it params_as_list arguments,
        whatever comes back, serialize it and store it in cache """

        key = "user:%s:%s" % (type, handle)
        try:
            cacheobj = cls.objects.get (key = key)
            now = time.time ()
            timeout = app.config.get ('CACHE_%s_INTERVAL' %(type.upper()), 3600)
            if now - cacheobj.timestamp > timeout:
                # Cache is invalid now
                dataobj = fn_on_fail (*params_as_list)
                cacheobj.data = json.dumps (dataobj)
                cacheobj.timestamp = time.time ()
                cacheobj.save ()
                print "Cache set but invalid"
            else:
                dataobj = json.loads (cacheobj.data)
                print "From cache"
        except CacheData.DoesNotExist:
            print "From new"
            dataobj = fn_on_fail (*params_as_list)
            cacheobj = cls (key = key, type = key, data = json.dumps (dataobj))
            cacheobj.save ()

        return dataobj

