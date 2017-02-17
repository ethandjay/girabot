import markovify
import sys
import random, os
from OAuthSettings import settings    #import authorization settings
import twitter

# Deletes all tweets with IDs taken from TweetIDs.txt, clears that file and then clears Tweets.txt

def DESTROY():
	consumer_key = settings['consumer_key']
	consumer_secret = settings['consumer_secret']
	access_token_key = settings['access_token_key']
	access_token_secret = settings['access_token_secret']

	try:
		api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)	
	except twitter.TwitterError:
		print api.message

	print "Iterating through stored tweet IDs and deleting corresponding tweets\n"
	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(__location__, 'TweetIDs.txt'), 'r') as file:
		for line in file.readlines():
			try:
				api.DestroyStatus(int(line))
			except:
				print "No tweet corresponds to this ID, moving on"

	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	open(os.path.join(__location__, 'TweetIDs.txt'), 'w')

	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	open(os.path.join(__location__, 'Tweets.txt'), 'w')

	print "All tweets wiped"
	exit()


# Sets API parameters from OAuthSettings (private)

consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']

# Check for special DESTROY argument that wipes all tweets from twitter / Tweets.txt / TweetIDs.txt

if (len(sys.argv) > 1 and sys.argv[1] == "DESTROY"):
	DESTROY();


os.system('cls' if os.name=='nt' else 'clear')

# Opens Markov source from path argument

with open("/Users/ethandjay/Documents/girabot/source/"+sys.argv[1]) as f:
    text = f.read()

# Runs text through Markov chain, treating each line as a new sentence. To use standard punction as breakpoints, use Text() instead

text_model = markovify.NewlineText(text)

# Makes sure it works

done = False
while done == False:
	tweet = text_model.make_short_sentence(140)
	if (tweet != None):
		done = True


try:
	api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)	
	print '\n' + tweet + '\n'

	#LOCAL argument prints generated tweet but doesn't post it
	if (not (len(sys.argv) > 2 and sys.argv[2] == "LOCAL")):
		print 'posting to Twitter...'
		status = api.PostUpdate(tweet)
		print '  post successful!\n'
		tweet_id = status.id 

		# Adding tweets / tweet ID's to respective files

		__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		with open(os.path.join(__location__, 'Tweets.txt'), 'a') as file:
			file.write(tweet + '\n')

		__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		with open(os.path.join(__location__, 'TweetIDs.txt'), 'a') as file:
			file.write(str(tweet_id) + '\n')

except twitter.TwitterError:
	print api.message


exit()



