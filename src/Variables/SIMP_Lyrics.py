import os
from pathlib import Path

current_song_name = ''
current_artist_name = ''
user_selection_language = 'en'
lyrics_path = Path(__file__).parent.parent.resolve()
lyrics_path = os.path.join(lyrics_path, "Lyrics")
OG_PATH = os.path.join(lyrics_path, "OG.txt")
TRANSLATED_PATH = os.path.join(lyrics_path, "TRANSLATED.txt")