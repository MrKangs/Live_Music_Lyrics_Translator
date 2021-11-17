import lyricsgenius as lg
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import googletrans as google
from PyQt5 import QtCore, QtGui, QtWidgets
from Variables.language_option import language_option

# Global Variables

user_selection_language = 'en'
current_song_title = ''
current_song_artists = ''
is_paused = False
current_position = 0
total_period = 0
lyrics_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Lyrics")
OG_PATH = os.path.join(lyrics_path, "OG.txt")
TRANSLATED_PATH = os.path.join(lyrics_path, "TRANSLATED.txt")
CLIENT_ACCESS_TOKEN = 'hAe4Arvcyuuc9SKMpIm67yfkMGyyPVGg-vro7aDyRI3eqQgRmJmPtOvYWVFdM9mx'
class Ui_Spotify_Window(object):
    """
    This is one of the child window from the Selection Screen window
    This window will be presented when the user select the Spotify option
    """
    def setupUi(self, Spotify_Window, spotify_api):
        """
        Initializes the child GUI that the user will be able to control Spotify while reading the lyrics in any language

        Args:
            Spotify_Window: QMainWindow from PyQt5 package
            spotify_api: Spotify API from Spotipy package
        
        Connected Functions:
            These functions will be run if the user do certain behavior within the GUI
            Format: Decription
                Object Name: Function and description

            Timer: Set the timer for every 1 ms to update the progression bar for the music

            Button: By clicking the button will trigger certain functions
                btn_play_pause: play_pause: It will play or resume the spotify player
                btn_previous: previous: It will go to the previous track of the spotify player
                btn_skip: skip: It will go to the next track of the spotify player
                btn_refresh: get_current_track: It will reload the GUI if the user interacted the Spotify Player by updating the song name, artists, and lyrics
            
            Combo Box: It is basically a drop down bar so that the user can select options from the bar
                language_bar: language_change: It will show the language option if they want to read the lyrics in a different language

        Independent Function:
            Unlike Connected Functions, these function will run inside the SetupUi function
            
                Function Name: Description

                retranslateUi: Update all the text values inside the GUI
                get_current_track: It will fetch information about the song that is playing on Spotify
        """
        Spotify_Window.setObjectName("Spotify_Window")
        Spotify_Window.resize(604, 631)
        self.centralwidget = QtWidgets.QWidget(Spotify_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.lyrics_holder = QtWidgets.QScrollArea(self.centralwidget)
        self.lyrics_holder.setGeometry(QtCore.QRect(30, 220, 541, 381))
        self.lyrics_holder.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lyrics_holder.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lyrics_holder.setWidgetResizable(True)
        self.lyrics_holder.setObjectName("lyrics_holder")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 539, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.og_lyrics = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.og_lyrics.setFont(font)
        self.og_lyrics.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.og_lyrics.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.og_lyrics.setWordWrap(True)
        self.og_lyrics.setObjectName("og_lyrics")
        self.horizontalLayout.addWidget(self.og_lyrics)
        self.translated_lyrics = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.translated_lyrics.setFont(font)
        self.translated_lyrics.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.translated_lyrics.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.translated_lyrics.setWordWrap(True)
        self.translated_lyrics.setObjectName("translated_lyrics")
        self.horizontalLayout.addWidget(self.translated_lyrics)
        self.lyrics_holder.setWidget(self.scrollAreaWidgetContents)
        self.song_name = QtWidgets.QLabel(self.centralwidget)
        self.song_name.setGeometry(QtCore.QRect(30, 20, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.song_name.setFont(font)
        self.song_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.song_name.setAlignment(QtCore.Qt.AlignCenter)
        self.song_name.setWordWrap(True)
        self.song_name.setObjectName("song_name")
        self.song_artists = QtWidgets.QLabel(self.centralwidget)
        self.song_artists.setGeometry(QtCore.QRect(340, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.song_artists.setFont(font)
        self.song_artists.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.song_artists.setAlignment(QtCore.Qt.AlignCenter)
        self.song_artists.setWordWrap(True)
        self.song_artists.setObjectName("song_artists")
        self.btn_play_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play_pause.setGeometry(QtCore.QRect(260, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.btn_play_pause.setFont(font)
        self.btn_play_pause.setObjectName("btn_play_pause")
        self.btn_previous = QtWidgets.QPushButton(self.centralwidget)
        self.btn_previous.setGeometry(QtCore.QRect(170, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.btn_previous.setFont(font)
        self.btn_previous.setObjectName("btn_previous")
        self.btn_skip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_skip.setGeometry(QtCore.QRect(350, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.btn_skip.setFont(font)
        self.btn_skip.setObjectName("btn_skip")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 90, 531, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setTickInterval(1000)
        self.lbl_current_progression = QtWidgets.QLabel(self.centralwidget)
        self.lbl_current_progression.setGeometry(QtCore.QRect(25, 120, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.lbl_current_progression.setFont(font)
        self.lbl_current_progression.setObjectName("lbl_current_progression")
        self.lbl_total_period = QtWidgets.QLabel(self.centralwidget)
        self.lbl_total_period.setGeometry(QtCore.QRect(550, 120, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.lbl_total_period.setFont(font)
        self.lbl_total_period.setObjectName("lbl_total_period")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(490, 182, 75, 23))
        self.btn_refresh.setObjectName("btn_refresh")
        self.language_box = QtWidgets.QComboBox(self.centralwidget)
        self.language_box.setGeometry(QtCore.QRect(30, 180, 391, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.language_box.setFont(font)
        self.language_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.language_box.setFrame(True)
        self.language_box.setObjectName("language_box")
        for i in range(106):
            self.language_box.addItem("")
        self.language_box.setCurrentIndex(21)
        Spotify_Window.setCentralWidget(self.centralwidget)

        self.spotify_api = spotify_api
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1)
        self.language_box.currentIndexChanged.connect(self.language_change)
        self.btn_play_pause.clicked.connect(self.play_pause)
        self.btn_previous.clicked.connect(self.previous)
        self.btn_skip.clicked.connect(self.skip)
        self.btn_refresh.clicked.connect(self.get_current_track)
        # self.horizontalSlider.valueChanged.connect(self.new_position)
        
        self.retranslateUi(Spotify_Window)
        self.get_current_track()
        QtCore.QMetaObject.connectSlotsByName(Spotify_Window)

    def language_change(self):
        """
        This function will update the global variable called user_selection_language based upon the user selection from the dropdown
        It will retrieve information from the user and language_option dictionary
        After that, it will run translate_lyrics function
        """
        global user_selection_language
        user_selection_language = language_option[self.language_box.currentText()]
        self.translate_lyrics(user_selection_language)
    
    
    def update(self):
        """
        This function will be triggered every 1 ms based upon the timer that was created from the setupUi function
        It will update the values of the current position of the song and the slider position 
        """
        global current_position, total_period
        current_position += 1

        if current_position == total_period:
            self.get_current_track()

        seconds=(current_position/1000)%60
        seconds = int(seconds)
        minutes=(current_position/(1000*60))%60
        minutes = int(minutes)
        self.lbl_current_progression.setText("{}:{}".format(minutes, seconds))
        self.horizontalSlider.setValue(current_position)
        
    
    def play_pause(self):
        """
        This function will be triggered when the user click play/pause button
        If it was playing, then it will pause both the song and the update timer function
        If it was in paused, then it will resume both the song and the update timer function
        """
        global is_paused

        if is_paused is False:
            self.btn_play_pause.setText("Play")
            self.spotify_api.pause_playback()
            self.timer.stop()
            is_paused = True
        
        else:
            self.btn_play_pause.setText("Pause")
            self.spotify_api.start_playback()
            self.timer.start(1)
            is_paused = False
        

    def previous(self):
        """
        This function will be triggered when the user click the button of Previous
        This will go to the previous track and run get_current_track function
        """
        self.spotify_api.previous_track()
        self.get_current_track()

    def skip(self):
        """
        This function will be triggered when the user click the button of Skip
        This will go to the next track and run get_current_track function
        """
        self.spotify_api.next_track()
        self.get_current_track()
    
    # def new_position(self):
    # TODO: Make this function alive again... need to find an alternative way to do this
    #     global current_position
    #     current_position = self.horizontalSlider.sliderPosition()
    #     self.spotify_api.seek_track(current_position)

    def get_current_track(self):
        """
        This function retrieve the song information from the Spotify player using the Spotify_API
        It will retrieve the song name, artist(s) name(s), curernt song progression in ms, and total song period in ms
        Once that is complete, then it will update the global variables and text GUI and send those information to get_lyrics function  
        """
        
        if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Lyrics")) is False:
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Lyrics"))
            
                
        responses_json = self.spotify_api.current_user_playing_track()
    
        if responses_json is None:
            please_play_song = QtWidgets.QMessageBox()
            please_play_song.setWindowTitle("Play a Song")
            please_play_song.setText("Please play a song on Spotify")
            please_play_song.setIcon(QtWidgets.QMessageBox.Critical)
            x = please_play_song.exec_()
            return False

        track_name = responses_json['item']['name']
        artists = responses_json['item']['artists'][0]['name']
        current_progression = responses_json['progress_ms']
        total_progression = responses_json['item']['duration_ms']


        current_track_info = {
            "name": track_name,
            "artists": artists
        }

        global current_song_title, current_song_artists, current_position, total_period

        current_position = current_progression
        total_period = total_progression

        self.horizontalSlider.setMaximum(total_period)
        seconds=(total_period/1000)%60
        seconds = int(seconds)
        minutes=(total_period/(1000*60))%60
        minutes = int(minutes)
        self.lbl_total_period.setText("{}:{}".format(minutes,seconds))
        

        if current_song_title is not current_track_info['name'] and current_song_artists is not current_track_info['artists']:
            current_song_title = current_track_info['name']
            current_song_artists = current_track_info['artists']
            self.get_lyrics(current_track_info)
    
    def get_lyrics(self, song_info):
        """
        This function will be triggered after the get_current_track function
        This will use Genius API to search the song name and artist name that is associated with the song
        If the song name cannot be found, then just simply search the song name
        If that does not work, then send the users that the Genuius API cannot find it

        If the song is found, then it will save the lyrics as a .txt file and trigger translate_lyrics function

        Args:
            song_info: Dictionary that has at least song name and artists names
        """

        lyrics = open(OG_PATH, "w", encoding= "utf=8")

        genius = lg.Genius(CLIENT_ACCESS_TOKEN, skip_non_songs= True, remove_section_headers= True)
        
        song = genius.search_song(song_info["name"], song_info["artists"])
        
        if song is None:
            song = genius.search_song(song_info["name"])
        
        if song is None:
            lyrics.write("No Song Lyrics can be found.")
        
        else:
            song_lyrics = song.lyrics.replace("EmbedShare URLCopyEmbedCopy", "")
            lyrics.write(song_lyrics)

        lyrics.close()
            
        self.translate_lyrics(user_selection_language) 
    
    def translate_lyrics(self, language:str):
        """
        This function will be triggered after get_lyrics function
        This function will use Google Translate API based on the .txt file

        If the lyrics too large (limit of 5,000 characters), then it will do a split translation of Google Translator API

        Once the translation is complete, then it will write a new .txt file called TRANSLATED that will have the translated version of the lyrics
        At the same time, it will trigger the display function

        Args:
            language: string value that indicates which language to be translated 
        """        
        
        translator = google.Translator()
        og_file = open(OG_PATH, "r", encoding= "utf-8")

        translated_file = open(TRANSLATED_PATH, "w", encoding= "utf-8")

        og_lyrics = og_file.read()

        if len(og_lyrics) > 5000:
            split_lyrics = []

            for i in range(0, len(og_lyrics), 4999):
                split_lyrics.append(og_lyrics[i: i + 5000])

            for i in range(len(split_lyrics)):
                result = translator.translate(split_lyrics[i], dest = language)
                translated_file.write(result.text)
            
            translated_file.close()
            og_file.close()
        
        else:

            result = translator.translate(og_lyrics, dest = language)
            translated_file.write(result.text)
            og_file.close()
            translated_file.close()
       
        self.display()
    
    def display(self):
        """
        This function will be triggered after the translate_lyrics function
        It will read both original lyrics, translated lyrics, song name, and artist name on the GUI
        """

        og_file = open(OG_PATH, "r", encoding= "utf-8")
        translated_file = open(TRANSLATED_PATH, "r", encoding= "utf-8")


        og_lyrics = ''
        translated_lyrics = ''
        
        for x in og_file.readlines():
            og_lyrics += x

        for y in translated_file.readlines():
            translated_lyrics += y

        self.og_lyrics.setText(og_lyrics)
        self.translated_lyrics.setText(translated_lyrics)
        self.song_name.setText(current_song_title)
        self.song_artists.setText("By {}".format(current_song_artists))

        translated_file.close()

    def retranslateUi(self, Spotify_Window):
        """
        This function is updating all the text or num values based on the initialization from the setupUi function
        """
        _translate = QtCore.QCoreApplication.translate
        Spotify_Window.setWindowTitle(_translate("Spotify_Window", "Spotify"))
        self.og_lyrics.setText(_translate("Spotify_Window", "TextLabel"))
        self.translated_lyrics.setText(_translate("Spotify_Window", "TextLabel"))
        self.song_name.setText(_translate("Spotify_Window", "TextLabel"))
        self.song_artists.setText(_translate("Spotify_Window", "TextLabel"))
        self.btn_play_pause.setText(_translate("Spotify_Window", "Pause"))
        self.btn_previous.setText(_translate("Spotify_Window", "Previous"))
        self.btn_skip.setText(_translate("Spotify_Window", "Skip"))
        self.btn_refresh.setText(_translate("Spotify_Window", "Refresh"))
        self.lbl_current_progression.setText(_translate("Spotify_Window", "TextLabel"))
        self.lbl_total_period.setText(_translate("Spotify_Window", "TextLabel"))
        key_values = list(language_option.keys())
        for i in range(106):
            self.language_box.setItemText(i, _translate("Spotify_Window", key_values[i]))