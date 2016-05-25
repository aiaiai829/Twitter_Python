# user-search - performs a search for users matching a certain query
# twitter API docs: https://dev.twitter.com/docs/api/1/get/users/search

from twitter import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# load our API credentials 
config = {}
execfile("config1.py", config)     
twitter = Twitter(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

# perform a user search (read a file including username)
file = open("n.txt")        
 
while 1:
    line = file.readline()
    line = line.strip('\n') 
    if not line:
        break
    results = twitter.users.lookup(screen_name = line)
    
    # loop through each of the users, and print out info
    for user in results:
	    print "*********%s*********" % (line)
	    print "location: %s" % (user["location"])
	    print "friends_count: %d" %(user["friends_count"])
	    print "followers_count: %d" %(user["followers_count"])
	    print "description: %s" %(user["description"])
	    print "statuses_count: %d" %(user["statuses_count"])
	    #print "retweet_count: %d" %(user['status']["retweet_count"])
	    print "listed_count: %d" %(user["listed_count"])
	    print "favourites_count: %d" %(user["favourites_count"])