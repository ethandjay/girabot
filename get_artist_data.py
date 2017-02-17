import requests
import re
from bs4 import BeautifulSoup

CLIENT_ACCESS_TOKEN = "GR47WTYM28fcP1vuZecwLOnnI8PHRNSMpuB14F9pTmkOmm1np4My086fi4Q6skD_"

BASE_URI = "https://api.genius.com"

# General GET request to Genius API, thanks Jon! See README for more.

def _get(path, params=None, headers=None):

    url = '/'.join([BASE_URI, path])

    token = "Bearer {}".format(CLIENT_ACCESS_TOKEN)

    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    response = requests.get(url=url, params=params, headers=headers)
    response.raise_for_status()

    return response.json()

# Gets all song objects from a given artist, accounting for pagination in results, thanks Jon! See README for more.

def get_artist_songs(artist_id):

    current_page = 1
    next_page = True
    songs = []

    while next_page:

        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page}
        data = _get(path=path, params=params)

        page_songs = data['response']['songs']

        if page_songs:
            songs += page_songs
            current_page += 1
        else:
            next_page = False

    return songs

# Scrapes artist ID from artist page metadata

def get_artist_id(artist_url):


    response = requests.get(artist_url)
    html = response.text

    match = re.search(r'<meta content="\/artists\/[0-9]+', html)
    artist_id=match.group(0)[24:]

    return artist_id







