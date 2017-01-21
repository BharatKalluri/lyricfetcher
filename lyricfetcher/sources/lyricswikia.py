import re
import urllib.request

from bs4 import BeautifulSoup


class LyricsWikia:
    @staticmethod
    def urlmaker(artist, song):
        """
        Make A url for lyricswikia.com
        """
        artist = '_'.join(artist.split(' '))
        song = '_'.join(song.split(' '))
        url = 'http://lyrics.wikia.com/wiki/' + artist + ':' + song
        return url

    @staticmethod
    def lyrics_get(url):
        """
        A function to get lyrics from a url
        """
        try:
            html_doc = urllib.request.urlopen(url)
            soup = BeautifulSoup(html_doc, 'html.parser')
            lyrics = soup.find("div", attrs={"class": "lyricbox"})
            refined = BeautifulSoup(re.sub(r'<br/>', '\n', str(lyrics)),
                                    'html.parser')
            return refined.get_text()
        except urllib.error.HTTPError as err:
            return err.getcode()
