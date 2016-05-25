
# twitter-friends
# lists all of a given user's following
# twitter API docs: https://dev.twitter.com/docs/api/1/get/friends/ids

from twitter import *

# load our API credentials 
config = {}
execfile("config1.py", config)

twitter = Twitter(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

# this is the user whose friends we will list
username = "PCLConstruction"
query = twitter.friends.ids(screen_name = username)

print "found %d friends" % (len(query["ids"]))

for n in range(0, len(query["ids"]), 100):
	ids = query["ids"][n:n+100]

	# twitter API docs: https://dev.twitter.com/docs/api/1/get/users/lookup
	subquery = twitter.users.lookup(user_id = ids)

	for user in subquery:
		# now print out user info, starring any users that are Verified.
		print " [%s] %s" % ("*" if user["verified"] else " ", user["screen_name"])