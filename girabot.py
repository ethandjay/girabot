from get_artist_songs import get_artist_songs
from scrape_lyrics import scrape_lyrics

songs = get_artist_songs(42141)
songs = [song for song in songs if song['primary_artist']['id'] == 42141]
for song in songs:
	print scrape_lyrics(song['url'])