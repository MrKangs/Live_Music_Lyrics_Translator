from PyQt5 import QtCore, QtGui, QtWidgets
import googletrans as google
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lyricsgenius as lg
import os



# Global Variables

language_option = {
    "Afrikaans": 'af',
    "Albanian": 'sq',
    "Amharic": 'am',
    "Arabic": 'ar',
    "Armenian": 'hy',
    "Azerbaijani": 'az',
    "Basque": 'eu',
    "Belarusian": 'be',
    "Bengali": 'bn',
    "Bosnian": 'bs',
    "Bulgarian": 'bg',
    "Catalan": 'ca',
    "Cebuano": 'ceb',
    "Chichewa": 'ny',
    "Chinese (Simplified)": 'zh-cn',
    "Chinese (Traditional)": 'zh-tw',
    "Corsican": 'co',
    "Croatian": 'hr',
    "Czech": 'cs',
    "Danish": 'da',
    "Dutch": 'nl',
    "English": 'en',
    "Esperanto": 'eo',
    "Estonian": 'et',
    "Filipino": 'tl',
    "Finnish": 'fi',
    "French": 'fr',
    "Frisian": 'fy',
    "Galician": 'gl',
    "Georgian": 'ka',
    "German": 'de',
    "Greek": 'el',
    "Gujarati": 'gu',
    "Haitian Creole": 'ht',
    "Hausa": 'ha',
    "Hawaiian": 'haw',
    "Hebrew": 'he',
    "Hindi": 'hi',
    "Hmong": 'hmn',
    "Hungarian": 'hu',
    "Icelandic": 'is',
    "Igbo": 'ig',
    "Indonesian": 'id',
    "Irish": 'ga',
    "Italian": 'it',
    "Japanese": "ja",
    "Javanese": 'jw',
    "Kannada": 'kn',
    "Kazakh": 'kk',
    "Khmer": 'km',
    "Korean": 'ko',
    "Kurdish (Kurmanji)": "ku",
    "Kyrgyz": 'ky',
    "Lao": 'lo',
    "Latin": 'la',
    "Latvian": 'lv',
    "Lithuanian": 'lt',
    "Luxembourgish": 'lb',
    "Macedonian":'mk',
    "Malagasy": 'mg',
    "Malay": 'ms',
    "Malayalam": "ml",
    "Maltese": 'mt',
    "Maori": 'mi',
    "Marathi": 'mr',
    "Mongolian": 'mn',
    "Myanmar (Burmese)": 'my',
    "Nepali": 'ne',
    "Norwegian": 'no',
    "Odia": 'or',
    "Pashto": 'ps',
    "Persian": 'fa',
    "Polish": 'pl',
    "Portuguese": 'pt',
    "Punjabi": 'pa',
    "Romanian": 'ro',
    "Russian":'ru',
    "Samoan": 'sm',
    "Scots Gaelic": 'gd',
    "Serbian": 'sr',
    "Sesotho": 'st',
    "Shona": 'sn',
    "Sindhi": 'sd',
    "Sinhala": 'si',
    "Slovak": 'sk',
    "Slovenian": 'sl',
    "Somali": 'so',
    "Spanish": 'es',
    "Sundanese": 'su',
    "Swahili": 'sw',
    "Swedish": 'sv',
    "Tajik": 'tg',
    "Tamil": 'ta',
    "Telugu": 'te',
    "Thai": 'th',
    "Turkish": 'tr',
    "Ukrainian": 'uk',
    "Urdu": 'ur',
    "Uyghur": 'ug',
    "Uzbek": 'uz',
    "Vietnamese": 'vi',
    "Welsh": 'cy',
    "Xhosa": 'xh',
    "Yiddish": 'yi',
    "Yoruba": 'yo',
    "Zulu": 'zu'
}

user_selection_language = 'en'
current_song_title = ''
current_song_artists = ''

class Ui_Spotify_Window(object):
    def setupUi(self, Spotify_Window, spotify_api):
        # TODO: scrollable Label creation for both lyrics
        Spotify_Window.setObjectName("Spotify_Window")
        Spotify_Window.resize(598, 480)
        self.centralwidget = QtWidgets.QWidget(Spotify_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.language_box = QtWidgets.QComboBox(self.centralwidget)
        self.language_box.setGeometry(QtCore.QRect(30, 30, 470, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.language_box.setFont(font)
        self.language_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.language_box.setFrame(True)
        self.language_box.setObjectName("language_box")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.addItem("")
        self.language_box.setCurrentIndex(-1)
        self.og_lyrics = QtWidgets.QLabel(self.centralwidget)
        self.og_lyrics.setGeometry(QtCore.QRect(30, 110, 261, 321))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.og_lyrics.setFont(font)
        self.og_lyrics.setAlignment(QtCore.Qt.AlignCenter)
        self.og_lyrics.setObjectName("og_lyrics")
        self.og_lyrics.setWordWrap(True)
        self.og_lyrics.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.translated_lyrics = QtWidgets.QLabel(self.centralwidget)
        self.translated_lyrics.setGeometry(QtCore.QRect(300, 110, 261, 321))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.translated_lyrics.setFont(font)
        self.translated_lyrics.setAlignment(QtCore.Qt.AlignCenter)
        self.translated_lyrics.setObjectName("translated_lyrics")
        self.translated_lyrics.setWordWrap(True)
        self.translated_lyrics.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(510, 30, 60, 41))
        self.btn_refresh.setFont(font)
        self.btn_refresh.setObjectName("btn_refresh")
        Spotify_Window.setCentralWidget(self.centralwidget)

        self.spotify_api = spotify_api

        self.retranslateUi(Spotify_Window)
        self.get_current_track()
        QtCore.QMetaObject.connectSlotsByName(Spotify_Window)
        self.language_box.currentIndexChanged.connect(self.language_change)
        self.btn_refresh.clicked.connect(self.get_current_track)

    
    def language_change(self):
        global user_selection_language
        user_selection_language = language_option[self.language_box.currentText()]
        self.translate_lyrics(user_selection_language)
        

    def display(self):
        # TODO: Make sure make the file location relative to the current path: it is, but better
        # TODO: Display the song title and artist name on top of the language dropdown
        # TODO: Make sure the label can be scolled to see the entire lyrics. Both at the same time.
        og_file = open("Archives\\UI_Design\\Lyrics\\og.txt", "r", encoding= "utf-8")
        translated_file = open("Archives\\UI_Design\\Lyrics\\Translated.txt", "r", encoding= "utf-8")

        og_lyrics = ''
        translated_lyrics = ''
        
        for x in og_file.readlines():
            og_lyrics += x

        for y in translated_file.readlines():
            translated_lyrics += y

        self.og_lyrics.setText(og_lyrics)
        self.translated_lyrics.setText(translated_lyrics)

        translated_file.close()

    
    def translate_lyrics(self, language:str):
        
        translator = google.Translator()
        og_file = open("Archives\\UI_Design\\Lyrics\\og.txt", "r", encoding= "utf-8")
        translated_file = open("Archives\\UI_Design\\Lyrics\\Translated.txt", "w", encoding= "utf-8")

        og_lyrics = og_file.read()
        result = translator.translate(og_lyrics, dest = language)
        translated_file.write(result.text)

        translated_file.close()
        self.display()

    def get_current_track(self):
        
        if os.path.exists("Archives\\UI_Design\\Lyrics") is False:
            os.makedirs("Archives\\UI_Design\\Lyrics")
                
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


        current_track_info = {
            "name": track_name,
            "artists": artists
        }

        global current_song_title, current_song_artists

        if current_song_title is not current_track_info['name'] and current_song_artists is not current_track_info['artists']:
            current_song_title = current_track_info['name']
            current_song_artists = current_track_info['artists']
            self.get_lyrics(current_track_info)


    def get_lyrics(self, song_info):
        
        # TODO: Sometimes gives interesting lyrics... need to know what is the issue is
        lyrics = open("Archives\\UI_Design\\Lyrics\\og.txt", "w", encoding= "utf=8")

        CLIENT_ACCESS_TOKEN = 'hAe4Arvcyuuc9SKMpIm67yfkMGyyPVGg-vro7aDyRI3eqQgRmJmPtOvYWVFdM9mx'
        genius = lg.Genius(CLIENT_ACCESS_TOKEN, skip_non_songs= True, remove_section_headers= True)
        
        song = genius.search_song(song_info["name"], song_info["artists"])

        if song is None:
            song = genius.search_song(song_info["name"])
        
        if song is not None:
            song_lyrics = song.lyrics.replace("EmbedShare URLCopyEmbedCopy", "")
        
        else:
            song_lyrics = "No Song Lyrics can be found."

        lyrics.write(song_lyrics)
        lyrics.close()

        self.translate_lyrics(user_selection_language)


    def retranslateUi(self, Spotify_Window):
        _translate = QtCore.QCoreApplication.translate
        Spotify_Window.setWindowTitle(_translate("Spotify_Window", "MainWindow"))
        self.language_box.setItemText(0, _translate("Spotify_Window", "Afrikaans"))
        self.language_box.setItemText(1, _translate("Spotify_Window", "Albanian"))
        self.language_box.setItemText(2, _translate("Spotify_Window", "Amharic"))
        self.language_box.setItemText(3, _translate("Spotify_Window", "Arabic"))
        self.language_box.setItemText(4, _translate("Spotify_Window", "Armenian"))
        self.language_box.setItemText(5, _translate("Spotify_Window", "Azerbaijani"))
        self.language_box.setItemText(6, _translate("Spotify_Window", "Basque"))
        self.language_box.setItemText(7, _translate("Spotify_Window", "Belarusian"))
        self.language_box.setItemText(8, _translate("Spotify_Window", "Bengali"))
        self.language_box.setItemText(9, _translate("Spotify_Window", "Bosnian"))
        self.language_box.setItemText(10, _translate("Spotify_Window", "Bulgarian"))
        self.language_box.setItemText(11, _translate("Spotify_Window", "Catalan"))
        self.language_box.setItemText(12, _translate("Spotify_Window", "Cebuano"))
        self.language_box.setItemText(13, _translate("Spotify_Window", "Chichewa"))
        self.language_box.setItemText(14, _translate("Spotify_Window", "Chinese (Simplified)"))
        self.language_box.setItemText(15, _translate("Spotify_Window", "Chinese (Traditional)"))
        self.language_box.setItemText(16, _translate("Spotify_Window", "Corsican"))
        self.language_box.setItemText(17, _translate("Spotify_Window", "Croatian"))
        self.language_box.setItemText(18, _translate("Spotify_Window", "Czech"))
        self.language_box.setItemText(19, _translate("Spotify_Window", "Danish"))
        self.language_box.setItemText(20, _translate("Spotify_Window", "Dutch"))
        self.language_box.setItemText(21, _translate("Spotify_Window", "English"))
        self.language_box.setItemText(22, _translate("Spotify_Window", "Esperanto"))
        self.language_box.setItemText(23, _translate("Spotify_Window", "Estonian"))
        self.language_box.setItemText(24, _translate("Spotify_Window", "Filipino"))
        self.language_box.setItemText(25, _translate("Spotify_Window", "Finnish"))
        self.language_box.setItemText(26, _translate("Spotify_Window", "French"))
        self.language_box.setItemText(27, _translate("Spotify_Window", "Frisian"))
        self.language_box.setItemText(28, _translate("Spotify_Window", "Galician"))
        self.language_box.setItemText(29, _translate("Spotify_Window", "Georgian"))
        self.language_box.setItemText(30, _translate("Spotify_Window", "German"))
        self.language_box.setItemText(31, _translate("Spotify_Window", "Greek"))
        self.language_box.setItemText(32, _translate("Spotify_Window", "Gujarati"))
        self.language_box.setItemText(33, _translate("Spotify_Window", "Haitian Creole"))
        self.language_box.setItemText(34, _translate("Spotify_Window", "Hausa"))
        self.language_box.setItemText(35, _translate("Spotify_Window", "Hawaiian"))
        self.language_box.setItemText(36, _translate("Spotify_Window", "Hebrew"))
        self.language_box.setItemText(37, _translate("Spotify_Window", "Hindi"))
        self.language_box.setItemText(38, _translate("Spotify_Window", "Hmong"))
        self.language_box.setItemText(39, _translate("Spotify_Window", "Hungarian"))
        self.language_box.setItemText(40, _translate("Spotify_Window", "Icelandic"))
        self.language_box.setItemText(41, _translate("Spotify_Window", "Igbo"))
        self.language_box.setItemText(42, _translate("Spotify_Window", "Indonesian"))
        self.language_box.setItemText(43, _translate("Spotify_Window", "Irish"))
        self.language_box.setItemText(44, _translate("Spotify_Window", "Italian"))
        self.language_box.setItemText(45, _translate("Spotify_Window", "Japanese"))
        self.language_box.setItemText(46, _translate("Spotify_Window", "Javanese"))
        self.language_box.setItemText(47, _translate("Spotify_Window", "Kannada"))
        self.language_box.setItemText(48, _translate("Spotify_Window", "Kazakh"))
        self.language_box.setItemText(49, _translate("Spotify_Window", "Khmer"))
        self.language_box.setItemText(50, _translate("Spotify_Window", "Korean"))
        self.language_box.setItemText(51, _translate("Spotify_Window", "Kurdish (Kurmanji)"))
        self.language_box.setItemText(52, _translate("Spotify_Window", "Kyrgyz"))
        self.language_box.setItemText(53, _translate("Spotify_Window", "Lao"))
        self.language_box.setItemText(54, _translate("Spotify_Window", "Latin"))
        self.language_box.setItemText(55, _translate("Spotify_Window", "Latvian"))
        self.language_box.setItemText(56, _translate("Spotify_Window", "Lithuanian"))
        self.language_box.setItemText(57, _translate("Spotify_Window", "Luxembourgish"))
        self.language_box.setItemText(58, _translate("Spotify_Window", "Macedonian"))
        self.language_box.setItemText(59, _translate("Spotify_Window", "Malagasy"))
        self.language_box.setItemText(60, _translate("Spotify_Window", "Malay"))
        self.language_box.setItemText(61, _translate("Spotify_Window", "Malayalam"))
        self.language_box.setItemText(62, _translate("Spotify_Window", "Maltese"))
        self.language_box.setItemText(63, _translate("Spotify_Window", "Maori"))
        self.language_box.setItemText(64, _translate("Spotify_Window", "Marathi"))
        self.language_box.setItemText(65, _translate("Spotify_Window", "Mongolian"))
        self.language_box.setItemText(66, _translate("Spotify_Window", "Myanmar (Burmese)"))
        self.language_box.setItemText(67, _translate("Spotify_Window", "Nepali"))
        self.language_box.setItemText(68, _translate("Spotify_Window", "Norwegian"))
        self.language_box.setItemText(69, _translate("Spotify_Window", "Odia"))
        self.language_box.setItemText(70, _translate("Spotify_Window", "Pashto"))
        self.language_box.setItemText(71, _translate("Spotify_Window", "Persian"))
        self.language_box.setItemText(72, _translate("Spotify_Window", "Polish"))
        self.language_box.setItemText(73, _translate("Spotify_Window", "Portuguese"))
        self.language_box.setItemText(74, _translate("Spotify_Window", "Punjabi"))
        self.language_box.setItemText(75, _translate("Spotify_Window", "Romanian"))
        self.language_box.setItemText(76, _translate("Spotify_Window", "Russian"))
        self.language_box.setItemText(77, _translate("Spotify_Window", "Samoan"))
        self.language_box.setItemText(78, _translate("Spotify_Window", "Scots Gaelic"))
        self.language_box.setItemText(79, _translate("Spotify_Window", "Serbian"))
        self.language_box.setItemText(80, _translate("Spotify_Window", "Sesotho"))
        self.language_box.setItemText(81, _translate("Spotify_Window", "Shona"))
        self.language_box.setItemText(82, _translate("Spotify_Window", "Sindhi"))
        self.language_box.setItemText(83, _translate("Spotify_Window", "Sinhala"))
        self.language_box.setItemText(84, _translate("Spotify_Window", "Slovak"))
        self.language_box.setItemText(85, _translate("Spotify_Window", "Slovenian"))
        self.language_box.setItemText(86, _translate("Spotify_Window", "Somali"))
        self.language_box.setItemText(87, _translate("Spotify_Window", "Spanish"))
        self.language_box.setItemText(88, _translate("Spotify_Window", "Sundanese"))
        self.language_box.setItemText(89, _translate("Spotify_Window", "Swahili"))
        self.language_box.setItemText(90, _translate("Spotify_Window", "Swedish"))
        self.language_box.setItemText(91, _translate("Spotify_Window", "Tajik"))
        self.language_box.setItemText(92, _translate("Spotify_Window", "Tamil"))
        self.language_box.setItemText(93, _translate("Spotify_Window", "Telugu"))
        self.language_box.setItemText(94, _translate("Spotify_Window", "Thai"))
        self.language_box.setItemText(95, _translate("Spotify_Window", "Turkish"))
        self.language_box.setItemText(96, _translate("Spotify_Window", "Ukrainian"))
        self.language_box.setItemText(97, _translate("Spotify_Window", "Urdu"))
        self.language_box.setItemText(98, _translate("Spotify_Window", "Uyghur"))
        self.language_box.setItemText(99, _translate("Spotify_Window", "Uzbek"))
        self.language_box.setItemText(100, _translate("Spotify_Window", "Vietnamese"))
        self.language_box.setItemText(101, _translate("Spotify_Window", "Welsh"))
        self.language_box.setItemText(102, _translate("Spotify_Window", "Xhosa"))
        self.language_box.setItemText(103, _translate("Spotify_Window", "Yiddish"))
        self.language_box.setItemText(104, _translate("Spotify_Window", "Yoruba"))
        self.language_box.setItemText(105, _translate("Spotify_Window", "Zulu"))
        self.btn_refresh.setText(_translate("Spotify_Window", "Refresh"))
        
        
        
