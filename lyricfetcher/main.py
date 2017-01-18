from .sources import AZlyrics as az
from .sources import Lyricswikia as lw
from .sources import MetroLyrics as ml
from .sources import Genius

"""
Lyric Fetcher to fetch lyrics from different sources!
"""


def get_lyrics(source, artist, song):
    """
    Function to return Lyrics from selective sources
    NOTE: All content is scraped from public web pages, only to be used for personal purposes
    """
    if source == 'azlyrics':
        return az.lyrics_get(az.urlmaker(artist, song))
    elif source == 'lyricswikia':
        return lw.lyrics_get(lw.urlmaker(artist, song))
    elif source == 'metrolyrics':
        return ml.lyrics_get(ml.urlmaker(artist, song))
    elif source == 'genius':
        return Genius.lyrics_get(Genius.urlmaker(artist, song))
    else:
        raise RuntimeError('argument source not valid')
