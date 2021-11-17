import lyricsgenius as lg
import csv

CLIENT_ACCESS_TOKEN = 'hAe4Arvcyuuc9SKMpIm67yfkMGyyPVGg-vro7aDyRI3eqQgRmJmPtOvYWVFdM9mx'

def get_lyrics(song_name, song_artist):
    """
    This function will get the song lyrics based on the user input of name of the song and the artist.
    If the Genius API cannot find the song with the artist, it will do a broad search based on the song lyrics. 

    Args:
        song_name: String value that will be the name the song.
        song_artist: String value that will be the artist of the song.

    Return:
        If the song lyrics can be found, then it will return a String of the entire lyrics of the song.
        Otherwise, it will return None.
    """
    
    genius = lg.Genius(CLIENT_ACCESS_TOKEN, skip_non_songs= True, remove_section_headers= True)

    song = genius.search_song(song_name, song_artist)

    if song is None:
        song = genius.search_song(song_name)
    
    if song is not None:
        song_lyrics = song.lyrics.replace("EmbedShare URLCopyEmbedCopy", "")
        first, *middle, last = song_lyrics.split()
        remove_pyong = ''.join([i for i in last if not i.isdigit()])
        song_lyrics = song_lyrics.replace(last, remove_pyong)
    
    else:
        song_lyrics = None
    
    return song_lyrics