import urlparse
import os

class ImageServiceProvider (object):

    def __init__ (self):
        pass
    
    def instagram (self, url, parsed):
        return self.instagr (url, parsed)

    def instagr (self, url, parsed):
        path = parsed.path
        if path.endswith ("/"):
            path = path[:-1]
        shortcode = os.path.basename (path)
        print shortcode
        return {
            "image": "http://instagr.am/p/%s/media/?size=l" % (shortcode),
            "thumbnail": "http://instagr.am/p/%s/media/?size=t" % (shortcode),
        }
    
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
            print "Unknown provider: %s (%s)" % (urlname, url)
            return False

