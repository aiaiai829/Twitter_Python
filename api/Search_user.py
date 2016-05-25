
# twitter-user-search - performs a search for users matching a certain query
# twitter API docs: https://dev.twitter.com/docs/api/1/get/users/search

from twitter import *

# load our API credentials 
config = {}
execfile("config1.py", config)
twitter = Twitter(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

# perform a user search 
results = twitter.users.search(q = 'work')

for user in results:
	print "@%s (%s): %s" % (user["screen_name"], user["name"], user["location"])