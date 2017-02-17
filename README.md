# girabot
Compiles all lyrics from a given artist into a text document, generates Markov text from the file, and tweets it

**Arguments for girabot.py [*arg1 (optional)*]:**  
	[filename] - the filename of the source text file  
	DESTROY - will delete all tweets on account and will wipe TweetIDs.txt and Tweets.txt  
	LOCAL   - will generate text for a tweet and print it but will not post it on the linked account

**Arguments for scrape_lyrics.py [*arg1*]:**  
	[Genius Artist URL] - takes in URL for artist on https://genius.com, in the format of https://genius.com/artists/xxxx
	

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

* markovify
https://github.com/jsvine/markovify  
* BeautifulSoup4  
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* OAuthlib  
https://github.com/requests/requests-oauthlib
* Python Twitter  
https://github.com/bear/python-twitter

Some structuring borrowed from <a href="https://jeffreythompson.org">Jeff's</a> <a href='https://github.com/jeffThompson/RandomArtAssignmentBot'>bot</a>, and some GET functions from <a href="http://www.jw.pe/landing/about/">Jon's</a> <a href='http://www.jw.pe/blog/post/quantifying-sufjan-stevens-with-the-genius-api-and-nltk/'>tutorial</a>

This project is released under a <a href='http://creativecommons.org/licenses/by-nc-sa/3.0/'>Creative Commons BY-NC-SA License</a> - feel free to use, but <a href='mailto:ethandjay@gmail.com'>please let me know</a>.

