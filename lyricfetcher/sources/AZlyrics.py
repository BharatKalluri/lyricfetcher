import urllib.request
from bs4 import BeautifulSoup


def urlmaker(artist, song):
    """
    Make A url from the given artist and song name
    """
    artist = ''.join(artist.split(' '))
    song = ''.join(song.split(' '))
    url = 'https://crossorigin.me/http://www.azlyrics.com/lyrics/'+artist+'/'+song+'.html'
    return url

def lyrics_get(url):
    """
    A function to get lyrics from a url
    """
    html_doc = urllib.request.urlopen(url)
    print(url,html_doc)
    soup = BeautifulSoup(html_doc, 'html.parser')
    lyrics = soup.find_all("div", attrs={"class": None, "id": None})
    lyrics = [x.getText() for x in lyrics]
    return lyrics[0]
