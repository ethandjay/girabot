import requests
import re
from get_artist_data import get_artist_id, get_artist_songs
from bs4 import BeautifulSoup
import sys
import os


print "Starting..."


artist_id = get_artist_id(sys.argv[1])

# Scrapes artist name from URL

name_match = re.search(r'artists\/[^\/]+', sys.argv[1])
artist_name = name_match.group(0)[8:]

# Gets song objects

songs = get_artist_songs(artist_id)

lyrics_sheet = ""

songs = [song for song in songs if song['primary_artist']['id'] == int(artist_id)]
for song in songs:
	song_url = song['url']

	# Gets raw HTML of song page

	response = requests.get(song_url)
	html = response.text

	soup = BeautifulSoup(html, 'html.parser')

	# Isolates lyrics tag

	lyrics = soup.find(name="lyrics")

	# Strips all HTML tags and headers ([Verse 1], [Outro], etc.)

	lyrics = re.sub(r'<[^>]*>','',str(lyrics))
	lyrics = re.sub(r'\[[^\]]*\]','',lyrics)


	lyrics_sheet += "\n" + lyrics

	# Progress visualization

	os.system('cls' if os.name == 'nt' else 'clear')
	print "Compiling lyrics... "
	print str(round(float(songs.index(song))/len(songs), 4) * 100.) + "%"


os.system('cls' if os.name == 'nt' else 'clear')
print "Compiling lyrics... "
print "100.0%, complete\n"

# Overwrites or creates new file with song name and all lyrics

filename = str(artist_name) + ".txt"

text_file = open("source/"+filename, "w")

text_file.write(lyrics_sheet)
text_file.close()

print "Lyrics sheet at " + text_file.name + " in source directory"