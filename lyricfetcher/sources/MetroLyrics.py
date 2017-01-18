import urllib.request
from bs4 import BeautifulSoup


def urlmaker(artist, song):
    """
    Make A url from the given artist and song name
    """
    artist = '-'.join(artist.split(' '))
    song = '-'.join(song.split(' '))
    url = 'http://www.metrolyrics.com/'+song+'-lyrics-'+artist+'.html'
    return url


def lyrics_get(url):
    """
    A function to get lyrics from a url
    """
    try:
        html_doc = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        complete_lyrics = []
        for i in soup.find_all("p", class_='verse'):
            complete_lyrics.append(i.get_text())
        lyrics = '\n'.join(complete_lyrics)
        if lyrics:
            return lyrics
        else:
            return 404
    except urllib.error.HTTPError as err:
        return err.getcode()
