import urllib.request
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
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"})
    soup = BeautifulSoup(urllib.request.urlopen(req), 'html.parser')
    lyrics = soup.find("lyrics")
    return lyrics.text.strip()
