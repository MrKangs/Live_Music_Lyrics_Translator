import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from spotipy import cache_handler
from Selection_Screen import Ui_Selection_Window
from Spotify_Window import Ui_Spotify_Window
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import Variables.Selection_Screen as data
import MicroService.SIMP as SIMP
from SIMP_Lyrics import Ui_SIMP_Lyrics_Window

def test_selection_screen():
    app = QtWidgets.QApplication(sys.argv)
    Selection_Window = QtWidgets.QMainWindow()
    ui = Ui_Selection_Window()
    ui.setupUi(Selection_Window)
    Selection_Window.show()
    Selection_Window.close()

def test_spotify_window():
    CACHE = eval(os.environ['CACHE'])
    SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
    SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
    app = QtWidgets.QApplication(sys.argv)
    Spotify_Window = QtWidgets.QMainWindow()
    ui = Ui_Spotify_Window()
    CACHE = spotipy.cache_handler.CacheFileHandler().save_token_to_cache(CACHE) 
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, 
    client_secret=SPOTIFY_CLIENT_SECRET, 
    redirect_uri="https://open.spotify.com", scope=data.SPOTIFY_SCOPE, cache_handler=CACHE))
    ui.setupUi(Spotify_Window, spotify, True)
    Spotify_Window.show()
    Spotify_Window.close()

def test_SIMP_window():
    app = QtWidgets.QApplication(sys.argv)
    SIMP_Window = SIMP.MediaWindow()
    SIMP_Window.resize(450,25)
    SIMP_Window.show()
    SIMP_Window.close()

def test_SIMP_lyrics_window():
    app = QtWidgets.QApplication(sys.argv)
    SIMP_Window = QtWidgets.QMainWindow()
    ui = Ui_SIMP_Lyrics_Window()
    ui.setupUi(SIMP_Window, song_name="Hello", artist_name="Hello",Lyrics="Hello")
    SIMP_Window.show()
    SIMP_Window.close()

if __name__ == "__main__":
    test_selection_screen()
    # test_spotify_window()
    test_SIMP_window()
    test_SIMP_lyrics_window()