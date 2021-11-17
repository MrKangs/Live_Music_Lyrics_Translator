from PyQt5 import QtCore, QtGui, QtWidgets
import googletrans as google

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


class Ui_Spotify_Window(object):
    def setupUi(self, Spotify_Window):
        Spotify_Window.setObjectName("Spotify_Window")
        Spotify_Window.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(Spotify_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.language_box = QtWidgets.QComboBox(self.centralwidget)
        self.language_box.setGeometry(QtCore.QRect(30, 30, 531, 41))
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
        self.og_lyrics_line_1 = QtWidgets.QLabel(self.centralwidget)
        self.og_lyrics_line_1.setGeometry(QtCore.QRect(40, 110, 521, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.og_lyrics_line_1.setFont(font)
        self.og_lyrics_line_1.setAlignment(QtCore.Qt.AlignCenter)
        self.og_lyrics_line_1.setObjectName("og_lyrics_line_1")
        self.translated_lyrics_line_2 = QtWidgets.QLabel(self.centralwidget)
        self.translated_lyrics_line_2.setGeometry(QtCore.QRect(40, 180, 521, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.translated_lyrics_line_2.setFont(font)
        self.translated_lyrics_line_2.setAlignment(QtCore.Qt.AlignCenter)
        self.translated_lyrics_line_2.setObjectName("translated_lyrics_line_2")
        self.og_lyrics_line_2 = QtWidgets.QLabel(self.centralwidget)
        self.og_lyrics_line_2.setGeometry(QtCore.QRect(40, 280, 521, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.og_lyrics_line_2.setFont(font)
        self.og_lyrics_line_2.setAlignment(QtCore.Qt.AlignCenter)
        self.og_lyrics_line_2.setObjectName("og_lyrics_line_2")
        self.translated_lyrics_line_3 = QtWidgets.QLabel(self.centralwidget)
        self.translated_lyrics_line_3.setGeometry(QtCore.QRect(40, 360, 521, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.translated_lyrics_line_3.setFont(font)
        self.translated_lyrics_line_3.setAlignment(QtCore.Qt.AlignCenter)
        self.translated_lyrics_line_3.setObjectName("translated_lyrics_line_3")
        Spotify_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Spotify_Window)
        QtCore.QMetaObject.connectSlotsByName(Spotify_Window)

        self.language_box.currentIndexChanged.connect(self.language_change)

        self.timer = QtCore.QTimer()

        self.translate_lyrics(user_selection_language)

        self.timer.timeout.connect(self.update)
        self.timer.start(10)

    def update(self):
        pass
    
    def language_change(self):
        self.translate_lyrics(language_option[self.language_box.currentText()])
        

    def translate_lyrics(self, language:str):
        translator = google.Translator()
        og_file = open("UI_Design\og.txt", "r", encoding= "utf-8")
        translated_file = open("UI_Design\Translated.txt", "w", encoding= "utf-8")

        og_lyrics = og_file.read()
        result = translator.translate(og_lyrics, dest = language)
        translated_file.write(result.text)
        

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
        self.og_lyrics_line_1.setText(_translate("Spotify_Window", "TextLabel"))
        self.translated_lyrics_line_2.setText(_translate("Spotify_Window", "TextLabel"))
        self.og_lyrics_line_2.setText(_translate("Spotify_Window", "TextLabel"))
        self.translated_lyrics_line_3.setText(_translate("Spotify_Window", "TextLabel"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Spotify_Window = QtWidgets.QMainWindow()
    ui = Ui_Spotify_Window()
    ui.setupUi(Spotify_Window)
    Spotify_Window.show()
    sys.exit(app.exec_())
