import urllib.request

from bs4 import BeautifulSoup

"""
The Website Does not want users to scrape their content!
"""


class AZlyrics:
    @staticmethod
    def urlmaker(artist, song):
        """
        Make A url for azlyrics.com
        """
        artist = ''.join(artist.split(' '))
        song = ''.join(song.split(' '))
        url = 'http://www.azlyrics.com/lyrics/' + artist + '/' + song + '.html'
        return url

    @staticmethod
    def lyrics_get(url):
        """
        A function to get lyrics from a url
        """
        try:
            html_doc = urllib.request.urlopen(url)
            soup = BeautifulSoup(html_doc, 'html.parser')
            lyrics = soup.find_all("div", attrs={"class": None, "id": None})
            lyrics = [x.getText() for x in lyrics]
            return lyrics[0]
        except urllib.error.HTTPError as err:
            return err.getcode()
