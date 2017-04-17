# girabot
Compiles all lyrics from given artist(s) into a single text document, generates Markov text from the file, and tweets it

**Arguments for girabot.py [*arg<sub>1</sub> (optional)*] [*arg<sub>2</sub> (optional assuming arg<sub>1</sub>==[filename])*]:**  
* arg<sub>1</sub>
	* [filename] - the filename of the source text file  
	* DESTROY - will delete all tweets on account and will wipe TweetIDs.txt and Tweets.txt (be careful)  
* arg<sub>2</sub>
	* LOCAL   - will generate text for a tweet and print it but will not post it on the linked account

**Arguments for scrape_lyrics.py [*arg<sub>1</sub>*] [*arg<sub>2</sub>*] ... [*arg<sub>n</sub>*]:**  
* arg<sub>i</sub>
	* [Genius Artist URL] - takes in URL for artist on https://genius.com, in the format of https://genius.com/artists/xxxx
	

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

Some Twitter API config borrowed from <a href="https://jeffreythompson.org">Jeff's</a> <a href='https://github.com/jeffThompson/RandomArtAssignmentBot'>bot</a>, and some GET functions from <a href="http://www.jw.pe/landing/about/">Jon's</a> <a href='http://www.jw.pe/blog/post/quantifying-sufjan-stevens-with-the-genius-api-and-nltk/'>tutorial</a>  
Twitterbot aspect modelled off of my <a href="https://github.com/ethandjay/vicebot">vicebot</a>

This project is released under a <a href='http://creativecommons.org/licenses/by-nc-sa/3.0/'>Creative Commons BY-NC-SA License</a> - feel free to use, but <a href='mailto:ethandjay@gmail.com'>please let me know</a>.

