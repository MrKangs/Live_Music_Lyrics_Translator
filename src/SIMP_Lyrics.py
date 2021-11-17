from PyQt5 import QtCore, QtGui, QtWidgets
from MicroService.translate_lyrics import translate_lyrics
from Variables.language_option import language_option
import Variables.SIMP_Lyrics as data
import os
class Ui_SIMP_Lyrics_Window(object):
    def setupUi(self, SIMP_Lyrics_Window, song_name, artist_name, Lyrics):
        SIMP_Lyrics_Window = self.creation_MainWindow(SIMP_Lyrics_Window)
        self.creation_centralwidget(SIMP_Lyrics_Window)
        self.creation_lyrics_holder()
        self.creation_lyrics_holder()
        self.creation_scrollAreaWidgetContents()
        self.creation_og_lyrics(self.declare_font())
        self.creation_translated_lyrics(self.declare_font())
        self.creation_horizontalLayout()
        self.creation_song_name(self.declare_font())
        self.creation_song_artists(self.declare_font())
        self.creation_language_box(self.declare_font())
        self.declare_variables(song_name, artist_name)
        self.assign_functions()        
        self.retranslateUi(SIMP_Lyrics_Window)
        self.update(Lyrics)

    def declare_font(self):
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        return font
    
    def assign_functions(self):
        self.language_box.currentIndexChanged.connect(self.language_change)
    
    def declare_variables(self, song, artist):
        data.user_selection_language = 'en'
        data.current_song_name = song
        data.current_artist_name = artist

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
        self.lyrics_holder.setGeometry(QtCore.QRect(30, 150, 541, 451))
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
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lyrics_holder.setWidget(self.scrollAreaWidgetContents)
    
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
        self.song_name.setGeometry(QtCore.QRect(30, 20, 291, 41))
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
        self.song_artists.setGeometry(QtCore.QRect(340, 20, 231, 41))
        self.song_artists.setFont(font)
        self.song_artists.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.song_artists.setAlignment(QtCore.Qt.AlignCenter)
        self.song_artists.setWordWrap(True)
        self.song_artists.setObjectName("song_artists")  
    
    def creation_language_box(self, font):
        font.setPointSize(16)
        self.language_box = QtWidgets.QComboBox(self.centralwidget)
        self.language_box.setGeometry(QtCore.QRect(100, 90, 391, 40))
        self.language_box.setFont(font)
        self.language_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.language_box.setFrame(True)
        self.language_box.setObjectName("language_box")
        for i in range(106):
            self.language_box.addItem("")
        self.language_box.setCurrentIndex(21)

    def language_change(self):
        data.user_selection_language = language_option[
            self.language_box.currentText()]
        translate_lyrics(data.user_selection_language, 
        data.OG_PATH, data.TRANSLATED_PATH)
        self.display()

    def update(self, Lyrics):
        
        if os.path.exists(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "Lyrics")) is False:
            os.makedirs(os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "Lyrics"))
        
        self.translate_it(Lyrics)
        self.display()
    
    def translate_it(self, Lyrics):
        lyrics = open(data.OG_PATH, "w", encoding= "utf=8")
        lyrics.write(Lyrics)
        lyrics.close()
        translate_lyrics(data.user_selection_language, 
        data.OG_PATH, data.TRANSLATED_PATH)

    def display(self):
        og_lyrics, translated_lyrics = self.reading_lyrics()
        self.og_lyrics.setText(og_lyrics)
        self.translated_lyrics.setText(translated_lyrics)
        self.song_name.setText(data.current_song_name)
        self.song_artists.setText("By {}".format(
            data.current_artist_name))  

    def reading_lyrics(self):
        og_file = open(data.OG_PATH, "r", encoding= "utf-8")
        translated_file = open(data.TRANSLATED_PATH, "r", encoding= "utf-8")

        og_lyrics = ''
        translated_lyrics = ''
        
        for x in og_file.readlines():
            og_lyrics += x

        for y in translated_file.readlines():
            translated_lyrics += y

        og_file.close()
        translated_file.close()
        
        return og_lyrics, translated_lyrics
    
    def retranslateUi(self, SIMP_Lyrics_Window):
        _translate = QtCore.QCoreApplication.translate
        SIMP_Lyrics_Window.setWindowTitle(
            _translate("SIMP_Lyrics_Window", "SIMP Lyrics"))
        self.og_lyrics.setText(
            _translate("SIMP_Lyrics_Window", ""))
        self.translated_lyrics.setText(
            _translate("SIMP_Lyrics_Window", ""))
        self.song_name.setText(
            _translate("SIMP_Lyrics_Window", ""))
        self.song_artists.setText(
            _translate("SIMP_Lyrics_Window", ""))
        key_values = list(language_option.keys())
        for i in range(106):
            self.language_box.setItemText(i, 
            _translate("Spotify_Window", key_values[i]))