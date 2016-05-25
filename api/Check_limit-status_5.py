try:
    import json
    import sys
except ImportError:
    import simplejson as json
    
from twitter import *
reload(sys)
sys.setdefaultencoding('utf-8')

# load our API credentials 
config = {}
execfile("config1.py", config)
twitter = Twitter(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

limit = twitter.application.rate_limit_status()
print limit