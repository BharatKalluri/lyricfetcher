# PyLyricFetcher 🔥🔥

A Package and API to search lyrics from different web sources

#### Note: All the lyrics are scraped from a public web pages of their respective domains, Please do not use this in Production as it is not allowed by the scraped website.Use this at your own discretion.

# API
The API is hosted at pylyricfetcher.herokuapp.com. It is written using the super fast
[Sanic](https://github.com/channelcat/sanic) as the backend. (Please be patient if your
first call is slow, as it uses Heroku free plan so the system takes time to start)

## API calls
An example call to the API can be as follows

Usage : http://pylyricfetcher.herokuapp.com/api/lyricswikia/ArtistName/SongName

Example: https://pylyricfetcher.herokuapp.com/api/lyricswikia/eminem/berzerk

to retrive the lyrics of berzerk from lyrics wikia. Try it Out!

There are 2 sources as of now
+ lyricswikia
+ MetroLyrics
+ Genius

The next arguments are The artist name and the song name!

# [LyricFetcher](https://github.com/BharatKalluri/lyricfetcher/tree/master/lyricfetcher)

[![PyPI version](https://badge.fury.io/py/lyricfetcher.svg)](https://badge.fury.io/py/lyricfetcher)

A python Package/Command Line Utility to get the lyrics of a Song

To install the package

```bash
pip install lyricfetcher
```

and import and use

```bash
>>> import lyricfetcher
>>> print(lyricfetcher.get_lyrics('azlyrics','linkin park','numb'))
```

or, You can use it directly from the terminal

```bash
# For help, just type
lyricfetcher -h
# Just call lyricfetcher, with the artist name and song name
lyricfetcher eminem "lose yourself" 
# Or jsut indicate a --source and you are good to go!
lyricfetcher --source lyricswikia eminem "lose yourself"
```

This prints out all the lyrics of linkin parks's awesome song

## Options
The get_lyrics takes 3 arguments
+ Source
  + azlyrics - Queries azlyrics for song lyrics
  + metrolyrics - source of information will be metrolyrics.com
  + genius - genius.com , you get it
+ Artist - The second argument takes in the name of the artist seperated by spaces
+ Song - The song name speprated by spaces

And returns the lyrics in text form!
