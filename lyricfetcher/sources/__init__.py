from lyricfetcher.sources.AZlyrics import AZlyrics
from lyricfetcher.sources.genius import Genius
from lyricfetcher.sources.lyricswikia import LyricsWikia
from lyricfetcher.sources.metrolyrics import MetroLyrics


def get_lyrics(source, artist, song):
    """
    Function to return Lyrics from selective sources
    NOTE: All content is scraped from public web pages, only to be used for
    personal purposes
    """
    if source == 'azlyrics':
        return AZlyrics.lyrics_get(AZlyrics.urlmaker(artist, song))
    elif source == 'lyricswikia':
        return LyricsWikia.lyrics_get(LyricsWikia.urlmaker(artist, song))
    elif source == 'metrolyrics':
        return MetroLyrics.lyrics_get(MetroLyrics.urlmaker(artist, song))
    elif source == 'genius':
        return Genius.lyrics_get(Genius.urlmaker(artist, song))
    else:
        raise RuntimeError('argument source not valid')
