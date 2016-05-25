# twitter_followers
# lists all of a given user's followers

from twitter import *

# load our API credentials 
config = {}
execfile("config1.py", config)     
twitter = Twitter(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

# this is the user whose follower we will read
file = open("company_user.txt")
 
while 1:
    line = file.readline()
    line = line.strip('\n') 
    if not line:
        break

    query = twitter.followers.ids(screen_name = line)

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
