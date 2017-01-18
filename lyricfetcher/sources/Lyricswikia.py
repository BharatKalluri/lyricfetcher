import urllib.request,re
from bs4 import BeautifulSoup


def urlmaker(artist, song):
    """
    Make A url from the given artist and song name
    """
    artist = '_'.join(artist.split(' '))
    song = '_'.join(song.split(' '))
    url = 'http://lyrics.wikia.com/wiki/'+artist+':'+song
    return url


def lyrics_get(url):
    """
    A function to get lyrics from a url
    """
    try:
        html_doc = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        lyrics = soup.find("div", attrs={"class": "lyricbox"})
        refined = BeautifulSoup(re.sub(r'<br/>', '\n', str(lyrics)), \
        'html.parser')
        return refined.get_text()
    except urllib.error.HTTPError as err:
        return err.getcode()
