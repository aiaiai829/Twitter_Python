# twitter-user-timeline
# displays a user's current timeline.

try:
    import json
    import sys
except ImportError:
    import simplejson as json
from twitter import *

# load our API credentials 
config = {}
execfile("config1.py", config)
twitter = Twitter(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

# this is the user file we're going to read.
file = open("test2copy.txt")
 
while 1:                                        
    line = file.readline()
    line = line.strip('\n') 
    if not line:
        break
    results = twitter.statuses.user_timeline(screen_name = line, count = 20)
    for result in query["statuses"]:
    	result_count += 1
    	print "#",result_count
    	print "- Author: %s  [Id: %s, Tweets: %s, Followings: %s, Followers: %s]" % (result["user"]["screen_name"], result["user"]["id"], result["user"]["statuses_count"], result["user"]["friends_count"], result["user"]["followers_count"])
        print "- Created at:  %s  %s" % (result["created_at"], result["user"]["location"])
        print "-> %s  " % (result["text"]) + '\n'