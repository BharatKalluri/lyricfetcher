# LyricFetcher 🔥🔥

A Package to search lyrics from diffrent web sources

### Note: All the lyrics are scraped from a public webpages of their respective domains, Only for personal use

A python Package to get the lyrics of a Song

To install the package

```bash
pip install lyricfetcher
```

and then it can be imported and used

```bash
>>> import lyricfetcher
>>> print(lyricfetcher.get_lyrics('azlyrics','linkin park','numb'))
```

This prints out all the lyrics of linkin parks's awesome Numb song

## Options
The get_lyrics takes 3 arguments
+ Source
  + azlyrics - Queries azlyrics for song lyrics
  + metrolyrics - source of information will be metrolyrics.com
+ Artist - The second argument takes in the name of the artist seperated by spaces
+ Song - The song name speprated by spaces

And returns the lyrics in text form!
