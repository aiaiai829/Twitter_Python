
# user-search - performs a search for users matching a certain query
# twitter API docs: https://dev.twitter.com/docs/api/1/get/users/search

from twitter import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# load our API credentials 
config = {}
execfile("config3.py", config)
twitter = Twitter(
		auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

# perform a user search (read a file including username)
file = open("test.txt")
 
while 1:
    line = file.readline()
    line = line.strip('\n') 
    if not line:
        break
    results = twitter.users.search(q = line , count = 5)
    
    # loop through each of the users, and print out info
    for user in results:
	    print "$$$%s" % (line)
	    print "@@@%s\n---%s\n***%s" % (user["screen_name"], user["name"], user["location"])
	    print "\n&&&statuses_count: %d\nfriends_count: %d\n---followers_count: %d" %(user["statuses_count"], user["friends_count"], user["followers_count"])