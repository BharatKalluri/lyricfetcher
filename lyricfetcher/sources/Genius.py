import requests
from bs4 import BeautifulSoup


def urlmaker(artist, song):
    """
    Make A url from the given artist and song name
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
    soup = BeautifulSoup(req.content, 'html.parser')
    lyrics = soup.find("lyrics")
    return lyrics.text.strip()
