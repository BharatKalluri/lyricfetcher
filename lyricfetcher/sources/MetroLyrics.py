import requests
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
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.content, 'html.parser')

    complete_lyrics = []
    for i in soup.find_all("p", class_='verse'):
        complete_lyrics.append(i.get_text())
    return '\n'.join(complete_lyrics)
