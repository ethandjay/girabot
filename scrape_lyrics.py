import requests
import re
from get_artist_data import get_artist_id, get_artist_songs
from bs4 import BeautifulSoup
import sys
import os


print "Starting..."

artist_links = sys.argv[1:]
artist_ids = []
name_matches = []
artist_names = []


for link in artist_links:

	# Storing artist id's

	artist_ids.append(get_artist_id(link))

	# Scraping artist names from URLs

	artist_names.append(re.search(r'artists\/[^\/]+', link).group(0)[8:])

# Gets song objects for each artist via ID

lyrics_sheet = ""
for ID in artist_ids:

	# Visual counter for which artist is being processed

	counter = str(artist_ids.index(ID)+1) + " of " + str(len(artist_ids)) + "\n"
	songs = get_artist_songs(ID)

	songs = [song for song in songs if song['primary_artist']['id'] == int(ID)]
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
		print counter + "\n"
		print "Compiling lyrics... "
		print str(round(float(songs.index(song))/len(songs), 4) * 100.) + "%"


os.system('cls' if os.name == 'nt' else 'clear')
print "Compiling lyrics... "
print "100.0%, complete\n"

# Overwrites or creates new file with song name and all lyrics
filename = artist_names[0]
for name in artist_names[1:]:
	filename += "_" +str(name)
filename += ".txt"

text_file = open("source/"+filename, "w")

text_file.write(lyrics_sheet)
text_file.close()

print "Lyrics sheet at " + text_file.name + " in source directory"