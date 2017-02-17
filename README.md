# girabot
Compiles all lyrics from a given artist into a text document, generates Markov text from the file, and tweets it

**Arguments for ViceHeadlineGenerator.py [optional]:**  
	DESTROY - will delete all tweets on account and will wipe TweetIDs.txt and Tweets.txt  
	LOCAL   - will generate text for a tweet and print it but will not post it on the linked account
	

**LOAD OAUTH SETTINGS**  
Assumes Twitter OAuth settings, saved in a file
called OAuthSettings.py, saved in the following format:
	
    settings = {
      'consumer_key': 'xxxx',
      'consumer_secret': 'xxxx',
      'access_token_key': 'xxxx',
      'access_token_secret': 'xxxx'
    }
  
**REQUIRES**

* OAuthlib  
https://github.com/requests/requests-oauthlib
* Python Twitter  
https://github.com/bear/python-twitter

Some structuring borrowed from <a href="https://jeffreythompson.org">Jeff's</a> <a href='https://github.com/jeffThompson/RandomArtAssignmentBot'>bot</a>

This project is released under a <a href='http://creativecommons.org/licenses/by-nc-sa/3.0/'>Creative Commons BY-NC-SA License</a> - feel free to use, but <a href='mailto:ethandjay@gmail.com'>please let me know</a>.

