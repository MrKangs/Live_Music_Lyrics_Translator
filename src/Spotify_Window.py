import os
from PyQt5 import QtCore, QtGui, QtWidgets
from Variables.language_option import language_option
from MicroService.get_song_lyrics import get_lyrics
from MicroService.translate_lyrics import translate_lyrics
import Variables.Spotify_Window as data
import time

class Ui_Spotify_Window(object):
    def setupUi(self, Spotify_Window, spotify_api, testing=False):
        Spotify_Window = self.creation_MainWindow(Spotify_Window)
        self.creation_centralwidget(Spotify_Window)
        self.creation_lyrics_holder()
        self.creation_scrollAreaWidgetContents()
        self.creation_og_lyrics(self.declare_font())
        self.creation_translated_lyrics(self.declare_font())
        self.creation_horizontalLayout()
        self.creation_song_name(self.declare_font())
        self.creation_song_artists(self.declare_font())
        self.creation_progression_bar()
        self.creation_lbl_current_progression(self.declare_font())
        self.creation_lbl_total_period(self.declare_font())
        self.creation_btn_play_pause(self.declare_font())
        self.creation_btn_previous(self.declare_font())
        self.creation_btn_skip(self.declare_font())
        self.creation_btn_refresh(self.declare_font())
        self.creation_language_box(self.declare_font())

        self.spotify_api = spotify_api

        self.retranslateUi(Spotify_Window)
        self.assign_functions()
        status = self.first_checker(testing)
        if testing:
            return status
        self.get_current_track()

    def declare_font(self):
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        return font
    
    def creation_MainWindow(self, Window):
        Window.setObjectName("Spotify_Window")
        Window.resize(604, 631)
        Window.setMinimumSize(QtCore.QSize(604, 631))
        Window.setMaximumSize(QtCore.QSize(604, 631))
        return Window
    
    def creation_centralwidget(self, Window):
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        Window.setCentralWidget(self.centralwidget)
    
    def creation_lyrics_holder(self):
        self.lyrics_holder = QtWidgets.QScrollArea(self.centralwidget)
        self.lyrics_holder.setGeometry(QtCore.QRect(30, 220, 541, 381))
        self.lyrics_holder.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.lyrics_holder.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.lyrics_holder.setWidgetResizable(True)
        self.lyrics_holder.setObjectName("lyrics_holder")
    
    def creation_scrollAreaWidgetContents(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 539, 379))
        self.scrollAreaWidgetContents.setObjectName(
            "scrollAreaWidgetContents")
        self.lyrics_holder.setWidget(
            self.scrollAreaWidgetContents)
    
    def creation_og_lyrics(self, font):
        self.og_lyrics = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        font.setPointSize(16)
        self.og_lyrics.setFont(font)
        self.og_lyrics.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.og_lyrics.setAlignment(
            QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.og_lyrics.setWordWrap(True)
        self.og_lyrics.setObjectName("og_lyrics")
   
    def creation_translated_lyrics(self, font):
        self.translated_lyrics = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        font.setPointSize(16)
        self.translated_lyrics.setFont(font)
        self.translated_lyrics.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.translated_lyrics.setAlignment(
            QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.translated_lyrics.setWordWrap(True)
        self.translated_lyrics.setObjectName("translated_lyrics")
    
    def creation_horizontalLayout(self):
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.og_lyrics)
        self.horizontalLayout.addWidget(self.translated_lyrics)
    
    def creation_song_name(self, font):
        self.song_name = QtWidgets.QLabel(self.centralwidget)
        self.song_name.setGeometry(QtCore.QRect(30, 10, 291, 70))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.song_name.setFont(font)
        self.song_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.song_name.setAlignment(QtCore.Qt.AlignCenter)
        self.song_name.setWordWrap(True)
        self.song_name.setObjectName("song_name")

    def creation_song_artists(self, font):
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.song_artists = QtWidgets.QLabel(self.centralwidget)
        self.song_artists.setGeometry(QtCore.QRect(340, 10, 231, 70))
        self.song_artists.setFont(font)
        self.song_artists.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.song_artists.setAlignment(QtCore.Qt.AlignCenter)
        self.song_artists.setWordWrap(True)
        self.song_artists.setObjectName("song_artists")

    def creation_progression_bar(self):
        self.progression_bar = QtWidgets.QSlider(self.centralwidget)
        self.progression_bar.setGeometry(QtCore.QRect(30, 90, 531, 22))
        self.progression_bar.setOrientation(QtCore.Qt.Horizontal)
        self.progression_bar.setTickInterval(1)
        self.progression_bar.setObjectName("progression_bar")
    
    def creation_lbl_current_progression(self, font):
        self.lbl_current_progression = QtWidgets.QLabel(self.centralwidget)
        self.lbl_current_progression.setGeometry(QtCore.QRect(25, 120, 47, 20))
        self.lbl_current_progression.setFont(font)
        self.lbl_current_progression.setObjectName("lbl_current_progression")
    
    def creation_lbl_total_period(self, font):
        self.lbl_total_period = QtWidgets.QLabel(self.centralwidget)
        self.lbl_total_period.setGeometry(QtCore.QRect(550, 120, 47, 20))
        self.lbl_total_period.setFont(font)
        self.lbl_total_period.setObjectName("lbl_total_period")
    
    def creation_btn_play_pause(self,font):
        font.setPointSize(11)
        self.btn_play_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play_pause.setGeometry(QtCore.QRect(260, 130, 75, 23))
        self.btn_play_pause.setFont(font)
        self.btn_play_pause.setObjectName("btn_play_pause")

    def creation_btn_previous(self, font):
        font.setPointSize(11)
        self.btn_previous = QtWidgets.QPushButton(self.centralwidget)
        self.btn_previous.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.btn_previous.setFont(font)
        self.btn_previous.setObjectName("btn_previous")
    
    def creation_btn_skip(self, font):
        font.setPointSize(11)
        self.btn_skip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_skip.setFont(font)
        self.btn_skip.setGeometry(QtCore.QRect(350, 130, 75, 23))
        self.btn_skip.setObjectName("btn_skip")
    
    def creation_btn_refresh(self, font):
        font.setPointSize(11)
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setFont(font)
        self.btn_refresh.setGeometry(QtCore.QRect(490, 182, 75, 23))
        self.btn_refresh.setObjectName("btn_refresh")
    
    def creation_language_box(self, font):
        font.setPointSize(16)
        self.language_box = QtWidgets.QComboBox(self.centralwidget)
        self.language_box.setGeometry(QtCore.QRect(30, 170, 391, 40))
        self.language_box.setFont(font)
        self.language_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.language_box.setFrame(True)
        self.language_box.setObjectName("language_box")
        for i in range(106):
            self.language_box.addItem("")
        self.language_box.setCurrentIndex(21)
    
    def assign_functions(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1)
        self.language_box.currentIndexChanged.connect(self.language_change)
        self.btn_play_pause.clicked.connect(self.play_pause)
        self.btn_previous.clicked.connect(self.previous)
        self.btn_skip.clicked.connect(self.skip)
        self.btn_refresh.clicked.connect(self.get_current_track)
        self.progression_bar.sliderMoved.connect(self.moving_new_position)
        self.progression_bar.sliderReleased.connect(self.new_position)

    def first_checker(self, testing):
        first_warning = True
        while self.spotify_api.current_user_playing_track() is None:
            if testing:
                print("Need to play a song on Spotify")
                first_warning = False
 
            if first_warning:
                self.please_play_a_song()
    
    def language_change(self):
        data.user_selection_language = language_option[
            self.language_box.currentText()]
        translate_lyrics(data.user_selection_language, 
        data.OG_PATH, data.TRANSLATED_PATH)
        self.display()
    
    def conversion(self, ms):
        seconds = int((ms/1000)%60)
        minutes = int(ms/(1000*60))%60
        return minutes, seconds
    
    def update(self):
        data.current_position += 1

        if data.current_position == data.total_period:
            self.get_current_track()

        minutes, seconds = self.conversion(data.current_position)
        self.lbl_current_progression.setText(
            "{:02}:{:02}".format(minutes, seconds))
        self.progression_bar.setValue(data.current_position)
        
    def play_pause(self):
        self.get_play_status()
        
        if data.is_playing is True:
            self.btn_play_pause.setText("Play")
            self.spotify_api.pause_playback()
            self.timer.stop()
        
        elif data.is_playing is False:
            self.btn_play_pause.setText("Pause")
            self.spotify_api.start_playback()
            self.timer.start(1)
        
    def get_play_status(self):
        responses_json = self.spotify_api.current_user_playing_track()
        data.is_playing = responses_json["is_playing"]
    
    def please_play_a_song(self):
        please_play_song = QtWidgets.QMessageBox()
        please_play_song.setWindowTitle("Play a Song")
        please_play_song.setText("Please play a song on Spotify")
        please_play_song.setIcon(QtWidgets.QMessageBox.Critical)
        please_play_song.exec_()
    
    def previous(self):
        self.spotify_api.previous_track()
        time.sleep(0.5)
        self.get_current_track()
        data.is_paused = False
        self.btn_play_pause.setText("Pause")
        self.timer.start(1)

    def skip(self):
        self.spotify_api.next_track()
        time.sleep(0.5)
        self.get_current_track()
        data.is_paused = False
        self.btn_play_pause.setText("Pause")
        self.timer.start(1)
    
    def moving_new_position(self):
        self.play_pause()
        self.progression_bar.sliderMoved.disconnect()
    
    def new_position(self):
        data.current_position = self.progression_bar.sliderPosition()
        self.spotify_api.seek_track(data.current_position)
        self.progression_bar.sliderMoved.connect(self.moving_new_position)
        self.play_pause()

    def get_current_track(self):
        if os.path.exists(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "Lyrics")) is False:
            os.makedirs(os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "Lyrics"))
                
        responses_json = self.spotify_api.current_user_playing_track()
        print(responses_json)
        track_name = responses_json['item']['name']
        artists = responses_json['item']['artists']
        current_progression = responses_json['progress_ms']
        total_progression = responses_json['item']['duration_ms']
        data.current_position = current_progression
        data.total_period = total_progression

        main_artist = artists[0]['name']
        artists = self.get_all_artist_name(artists)
        

        self.update_total_progression()

        if (data.current_song_title is not track_name) and (data.current_song_artists is not artists):
            data.current_song_title = track_name
            data.current_song_artists = artists
            self.get_lyrics_and_translate_it(main_artist)
        
        self.display()
    
    def get_all_artist_name(self, json):
        artists = ""
        for i in range(len(json)):
            name = json[i]['name']
            artists += name + ", "
        artists = artists[:-2]
        return artists
    
    def update_total_progression(self):
        self.progression_bar.setMaximum(data.total_period)
        minutes, seconds = self.conversion(data.total_period)
        self.lbl_total_period.setText(
            "{:02}:{:02}".format(minutes,seconds))

    def get_lyrics_and_translate_it(self, main_artist):
        lyrics = open(data.OG_PATH, "w", encoding= "utf=8")
        song_lyrics = get_lyrics(data.current_song_title, 
        main_artist, data.GENINUS_CLIENT_TOKEN)
        if song_lyrics is None:
            song_lyrics = "Specified song does not contain lyrics."
        lyrics.write(song_lyrics)
        lyrics.close()
        translate_lyrics(data.user_selection_language, 
        data.OG_PATH, data.TRANSLATED_PATH)
    
    def display(self):
        og_file = open(data.OG_PATH, "r", encoding= "utf-8")
        translated_file = open(data.TRANSLATED_PATH, "r", encoding= "utf-8")

        og_lyrics = ''
        translated_lyrics = ''
        
        for x in og_file.readlines():
            og_lyrics += x

        for y in translated_file.readlines():
            translated_lyrics += y

        self.og_lyrics.setText(og_lyrics)
        self.translated_lyrics.setText(translated_lyrics)
        self.song_name.setText(data.current_song_title)
        self.song_artists.setText("By {}".format(
            data.current_song_artists))

        og_file.close()
        translated_file.close()

    def retranslateUi(self, Spotify_Window):
        _translate = QtCore.QCoreApplication.translate
        Spotify_Window.setWindowTitle(
            _translate("Spotify_Window", "Spotify"))
        self.og_lyrics.setText(
            _translate("Spotify_Window", ""))
        self.translated_lyrics.setText(
            _translate("Spotify_Window", ""))
        self.song_name.setText(
            _translate("Spotify_Window", ""))
        self.song_artists.setText(
            _translate("Spotify_Window", ""))
        self.btn_play_pause.setText(
            _translate("Spotify_Window", "Pause"))
        self.btn_previous.setText(
            _translate("Spotify_Window", "Previous"))
        self.btn_skip.setText(
            _translate("Spotify_Window", "Skip"))
        self.btn_refresh.setText(
            _translate("Spotify_Window", "Refresh"))
        self.lbl_current_progression.setText(
            _translate("Spotify_Window", ""))
        self.lbl_total_period.setText(
            _translate("Spotify_Window", ""))
        key_values = list(language_option.keys())
        for i in range(106):
            self.language_box.setItemText(i, 
            _translate("Spotify_Window", key_values[i]))