# twitter-user-timeline
# displays a user's current timeline.

from twitter import *

# load our API credentials 
config = {}
execfile("config1.py", config)
twitter = Twitter(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

# this is the user file we're going to read.
file = open("test.txt")
 
while 1:
    line = file.readline()
    line = line.strip('\n') 
    if not line:
        break
    results = twitter.statuses.user_timeline(screen_name = line, count = 20)
    for status in results:
        print line
        print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))