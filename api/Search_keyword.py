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

num_results = 200
result_count = 0
last_id = None
# perform a search 
keyword = 'builder'
print 'KEYWORD = [',keyword,']' + '\n'
while result_count <  num_results:
    query = twitter.search.tweets(q = keyword, count = "100", lang = "en", max_id = last_id)#,geocode = "39.6295300000,-79.9559000000,50000mi"
    for result in query["statuses"]:
    	result_count += 1
    	print "#",result_count
    	print "- Author: %s  [Id: %s, Tweets: %s, Followings: %s, Followers: %s]" % (result["user"]["screen_name"], result["user"]["id"], result["user"]["statuses_count"], result["user"]["friends_count"], result["user"]["followers_count"])
        print "- Created at:  %s  %s" % (result["created_at"], result["user"]["location"])
        print "-> %s  " % (result["text"]) + '\n'
        last_id = result["id"]