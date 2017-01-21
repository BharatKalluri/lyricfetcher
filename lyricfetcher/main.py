#!/usr/bin/env python3
import argparse

from lyricfetcher.sources import get_lyrics

def main():
    """
    The Main function to kickstart console applications
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", help="Source [can be azlyrics,genius,\
    lyricswikia, metrolyrics]", default='genius')
    parser.add_argument("artist", help="The Artist Name goes here")
    parser.add_argument("song", help="The Song name goes here")
    args = parser.parse_args()
    lyrics = get_lyrics(args.source, args.artist, args.song)
    if isinstance(lyrics, int):
        print("Sorry, Song Not Found!")
    else:
        print(lyrics)
