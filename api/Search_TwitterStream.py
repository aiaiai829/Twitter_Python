try:
    import json
except ImportError:
    import simplejson as json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# load our API credentials 
config = {}
execfile("config1.py", config)
twitter = TwitterStream(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

iterator = twitter.statuses.filter(track="test")
#iterator = twitter.statuses.filter(track="worker", language="en", locations="-74,40,-73,41")
tweet_count = 5
for tweet in iterator:
    tweet_count -= 1
    print json.dumps(tweet)
    if tweet_count <= 0:
    	break