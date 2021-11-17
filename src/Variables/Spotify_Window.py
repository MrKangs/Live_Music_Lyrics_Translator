from pathlib import Path
import os

user_selection_language = 'en'
current_song_title = ''
current_song_artists = ''
current_position = 0
total_period = 0
is_playing = False
lyrics_path = Path(__file__).parent.parent.resolve()
lyrics_path = os.path.join(lyrics_path, "Lyrics")
OG_PATH = os.path.join(lyrics_path, "OG.txt")
TRANSLATED_PATH = os.path.join(lyrics_path, "TRANSLATED.txt")
GENINUS_CLIENT_TOKEN = "hAe4Arvcyuuc9SKMpIm67yfkMGyyPVGg-vro7aDyRI3eqQgRmJmPtOvYWVFdM9mx"