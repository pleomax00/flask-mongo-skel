import twitter
import json
from providers import ImageServiceProvider


class TweetParser (object):

    def __init__ (self, consumer_key, consumer_secret, access_token, access_secret):
        self.api = twitter.Api (consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token, access_token_secret = access_secret)

    def following (self):
        following = self.api.GetFriends ()
        friends = []
        for user in following:
            friends.append ({
                "handle": user.GetScreenName (),
                "id": user.GetId (),
                "name": user.GetName (),
                "profilepic": "https://api.twitter.com/1/users/profile_image?screen_name=%s&size=bigger" % (user.GetScreenName ()),
            })
        return friends

    def parse (self, handle):
        statuses = self.api.GetUserTimeline (handle, count = 200, include_rts = True, include_entities = True)
        images = []
        serviceprovider = ImageServiceProvider ()
        for i in statuses:
            x = json.loads (i.AsJsonString())
            if len (i.urls) > 0:
                for url in i.urls:
                    image_url = serviceprovider.parse (url.expanded_url)
                    if image_url:
                        images.append (image_url)
        return images
