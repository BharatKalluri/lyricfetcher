from sanic import Sanic
from sanic.response import json, text
import os

import lyricfetcher as lw

app = Sanic(__name__)
@app.route('/')
async def helper(request):
    """
    A helper function for the home visit
    """
    return text(
        """
        A lyrics api, the first argument is the source \
        [can be metro for metrolyrics or lyricswikia for lyricswikia] \
        the second is the artist name, and the third is the song name.\n
        example: pylyricfetcher.herokuapp.com/lyrics/lyricswikia/linkin park/numb\n
        NOTE: All content is scraped from public web pages, only to be used for personal purposes
        """
)


@app.route('/api/<source>/<artist>/<song>')
async def get_lyrics(request, source, artist, song):
    """
    A route to indicate what to do after the source info is in
    """
    artist = artist.replace("%20", " ")
    song = song.replace("%20", " ")
    if source == "metro":
        return json({
            "source": "MetroLyrics",
            "artist": artist,
            "Song": song,
            "Lyrics": lw.get_lyrics('metrolyrics', artist, song)
            })
    # if source == 'az':
    #     return json({
    #         "source": "az",
    #         "artist": artist,
    #         "Song": song,
    #         "Lyrics": az.lyrics_get(az.urlmaker(artist, song))
    #     })
    if source == 'lyricswikia':
        return json({
            "source": 'lyricswikia',
            "artist": artist,
            "Song": song,
            "Lyrics": lw.get_lyrics('metrolyrics', artist, song)
        })
    if source == 'genius':
        return json({
            "source": 'genius',
            "artist": artist,
            "Song": song,
            "Lyrics": lw.get_lyrics('genius', artist, song)
        })
    else:
        return text("Bad Request! Try visiting Home page for help")

app.run(host='0.0.0.0', port=int(os.environ['PORT']),debug=True)
