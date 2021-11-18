import lyricsgenius as lg 
from musixmatch import Musixmatch
def get_lyrics(song_name, song_artist, GENINUS_CLIENT_TOKEN, MUSIC_MATCH_CLIENT_TOKEN):
    
    """
    This function will get the song lyrics based on the 
    user input of name of the song and the artist.
    If the Genius API cannot find the song with the artist, 
    it will do a broad search based on the song lyrics.

    Args:
        song_name: String value that will be the name the song.
        song_artist: String value that will be the artist of the song.

    Return:
        If the song lyrics can be found,
        then it will return a String of the entire lyrics of the song.
        Otherwise, it will return None.
    """
    
    genius = lg.Genius(GENINUS_CLIENT_TOKEN, skip_non_songs=True, 
    remove_section_headers=True)

    musicmatch = Musixmatch(MUSIC_MATCH_CLIENT_TOKEN)

    from_music_match = True
    
    song_detail = musicmatch.matcher_lyrics_get(song_name, song_artist)
    
    song_lyrics = song_detail['message']['body']['lyrics']['lyrics_body']

    print(song_lyrics)
    
    if song_lyrics is None:
        song_lyrics = genius.search_song(song_name, song_artist)
        from_music_match = False
    
    if song_lyrics is None:
        song = genius.search_song(song_name)
    
    if song_lyrics is not None and from_music_match is False:
        song_lyrics = song_lyrics.lyrics.replace("EmbedShare URLCopyEmbedCopy"
        , "")
        first, *middle, last = song_lyrics.split()
        remove_pyong = ''.join([i for i in last if not i.isdigit()])
        song_lyrics = song_lyrics.replace(last, remove_pyong)
    
    return song_lyrics
