# twitter_following
# lists all of a given user's following
# twitter API docs: https://dev.twitter.com/docs/api/1/get/friends/ids

from twitter import *

# load our API credentials 
config = {}
execfile("config2.py", config)     
twitter = Twitter(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

# this is the user whose following we will read
file = open("worker_user.txt")
 
while 1:
    line = file.readline()
    line = line.strip('\n') 
    if not line:
        break

    query = twitter.friends.ids(screen_name = line)

    for n in range(0, 100, 100):
	    ids = query["ids"][n:n+100]

	    subquery = twitter.users.lookup(user_id = ids)
	    count = 0

	    for user in subquery:
		    count += 1
		    print "**********%s**%d*********" % (line,count)
		    print "screen_name: %s" % (user["screen_name"])	    
		    print "location: %s" % (user["location"].encode("ascii", "ignore"))
		    print "friends_count: %d" %(user["friends_count"])
		    print "followers_count: %d" %(user["followers_count"])
		    print "statuses_count: %d" %(user["statuses_count"])
		    print "listed_count: %d" %(user["listed_count"])
		    print "favourites_count: %d" %(user["favourites_count"])
