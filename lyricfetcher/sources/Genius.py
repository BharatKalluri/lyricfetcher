import requests
from bs4 import BeautifulSoup


def urlmaker(artist, song):
    """
    Make A url for genius.com
    """
    artist = '-'.join(artist.split(' '))
    song = '-'.join(song.split(' '))
    url = 'https://genius.com/{}-{}-lyrics'.format(artist, song)
    return url


def lyrics_get(url):
    """
    A function to get lyrics from a url
    """
    req = requests.get(url)
    if req.status_code == 200:
        soup = BeautifulSoup(req.content, 'html.parser')
        lyrics = soup.find("lyrics")
        return lyrics.text.strip()
    else:
        return req.status_code
