from PyQt5 import QtCore, QtGui, QtWidgets
import os
from MicroService.translate_lyrics import translate_lyrics
from Variables.language_option import language_option

# Global Variables
current_song_name = ''
current_artist_name = ''
user_selection_language = 'en'
lyrics_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Lyrics")
OG_PATH = os.path.join(lyrics_path, "OG.txt")
TRANSLATED_PATH = os.path.join(lyrics_path, "TRANSLATED.txt")


class Ui_SIMP_Lyrics_Window(object):
    def setupUi(self, SIMP_Lyrics_Window, song_name, artist_name, Lyrics):
        SIMP_Lyrics_Window.setObjectName("SIMP_Lyrics_Window")
        SIMP_Lyrics_Window.resize(604, 631)
        self.centralwidget = QtWidgets.QWidget(SIMP_Lyrics_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.lyrics_holder = QtWidgets.QScrollArea(self.centralwidget)
        self.lyrics_holder.setGeometry(QtCore.QRect(30, 140, 541, 461))
        self.lyrics_holder.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lyrics_holder.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lyrics_holder.setWidgetResizable(True)
        self.lyrics_holder.setObjectName("lyrics_holder")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 539, 459))
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
        self.language_box = QtWidgets.QComboBox(self.centralwidget)
        self.language_box.setGeometry(QtCore.QRect(110, 90, 391, 29))
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
        SIMP_Lyrics_Window.setCentralWidget(self.centralwidget)
        self.language_box.currentIndexChanged.connect(self.language_change)

        self.retranslateUi(SIMP_Lyrics_Window)
        QtCore.QMetaObject.connectSlotsByName(SIMP_Lyrics_Window)

        global current_song_name, current_artist_name, user_selection_language 
        current_song_name = song_name
        current_artist_name = artist_name
        user_selection_language = 'en'

        self.update(Lyrics)

    def language_change(self):
        """
        This function will update the global variable called user_selection_language based upon the user selection from the dropdown
        It will retrieve information from the user and language_option dictionary
        After that, it will run translate_lyrics function
        """
        global user_selection_language
        user_selection_language = language_option[self.language_box.currentText()]
        translate_lyrics(user_selection_language, OG_PATH, TRANSLATED_PATH)
        self.display()

    def display(self):
        """
        This function will be triggered after the translate_lyrics function
        It will read both original lyrics, translated lyrics, song name, and artist name on the GUI
        """

        global current_song_name, current_artist_name
        
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
        self.song_name.setText(current_song_name)
        self.song_artists.setText("By {}".format(current_artist_name))

        translated_file.close()

    def update(self, Lyrics):
        lyrics = open(OG_PATH, "w", encoding= "utf=8")
        lyrics.write(Lyrics)
        lyrics.close()
        translate_lyrics(user_selection_language, OG_PATH, TRANSLATED_PATH)
        self.display()
    
    def retranslateUi(self, SIMP_Lyrics_Window):
        _translate = QtCore.QCoreApplication.translate
        SIMP_Lyrics_Window.setWindowTitle(_translate("SIMP_Lyrics_Window", "SIMP Lyrics"))
        self.og_lyrics.setText(_translate("SIMP_Lyrics_Window", ""))
        self.translated_lyrics.setText(_translate("SIMP_Lyrics_Window", ""))
        self.song_name.setText(_translate("SIMP_Lyrics_Window", ""))
        self.song_artists.setText(_translate("SIMP_Lyrics_Window", ""))
        key_values = list(language_option.keys())
        for i in range(106):
            self.language_box.setItemText(i, _translate("Spotify_Window", key_values[i]))