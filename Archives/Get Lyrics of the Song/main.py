import lyricsgenius as lg

def get_lyrics(genius, song_name, artist_name):
    
    file = open("D:\CS361_Project\Archives\Get Lyrics of the Song\OG.txt", "w", encoding= "utf-8")
    
    song = genius.search_song(song_name, artist_name)
    
    if song is None:
        print("Can't find the song' lyrics: Will find similar lyrics")
        song = genius.search_song(song_name)

    song_lyrics = song.lyrics.replace("EmbedShare URLCopyEmbedCopy", "")
    file.write(song_lyrics)


def main():
    
    CLIENT_ACCESS_TOKEN = 'hAe4Arvcyuuc9SKMpIm67yfkMGyyPVGg-vro7aDyRI3eqQgRmJmPtOvYWVFdM9mx'
    # This is the token from Genius API

    genius = lg.Genius(CLIENT_ACCESS_TOKEN, skip_non_songs= True, remove_section_headers= True)

    get_lyrics(genius, "Is It Still Beautiful", "Mido and Falasol")
    get_lyrics(genius,"To You", "Yoo Yeon Seok")
    get_lyrics(genius, "Gorgeous", "Kanye West")


if __name__ == "__main__":
    main()

    
    
    

