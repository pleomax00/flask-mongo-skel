import urlparse

class ImageServiceProvider (object):

    def __init__ (self):
        pass
    
    def yfrog (self, url, parsed):
        return {
            "image": "http://yfrog.com%s:medium" % (parsed.path),
            "thumbnail": "http://yfrog.com%s:small" % (parsed.path),
        }

    def parse (self, url):
        parsed = urlparse.urlparse (url)
        urlname = parsed.netloc.split (".")[0]
        if hasattr (self, urlname):
            parse_fn = getattr (self, urlname)
            print "%s Image Detected" % (urlname)
            return parse_fn (url, parsed)
        else:
            print "Unknown provider:", urlname
            return False

