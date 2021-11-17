from PyQt5 import QtCore, QtGui, QtWidgets
from Spotify_Window import Ui_Spotify_Window
from MicroService.SIMP import MediaWindow
import Variables.Selection_Screen as data
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import os


class Ui_Selection_Window(object):
    def setupUi(self, Selection_Window):
        Selection_Window = self.creation_MainWindow(Selection_Window)
        self.creation_centralwidget(Selection_Window)
        self.creation_gridLayout()
        self.creation_spacers()
        self.creation_btn_spotify(self.declare_font())
        self.creation_btn_local_music(self.declare_font())
        self.creation_lbl_selection(self.declare_font())
        self.retranslateUi(Selection_Window)
        self.assign_functions()

    def creation_MainWindow(self, Window):
        Window.setObjectName("Selection_Window")
        Window.resize(298, 251)
        Window.setMinimumSize(QtCore.QSize(298, 251))
        Window.setMaximumSize(QtCore.QSize(298, 251))
        return Window

    def creation_centralwidget(self, Window):
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        Window.setCentralWidget(self.centralwidget)

    def creation_gridLayout(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

    def creation_spacers(self):
        spacerItem = QtWidgets.QSpacerItem(20, 40, 
        QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, 
        QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, 
        QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, 
        QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, 
        QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, 
        QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 2, 1, 1)

    def declare_font(self):
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        return font

    def creation_btn_spotify(self, font):
        font.setPointSize(12)
        self.btn_spotify = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_spotify.setFont(font)
        self.btn_spotify.setObjectName("btn_spotify")
        self.gridLayout.addWidget(self.btn_spotify, 3, 1, 1, 1)

    def creation_btn_local_music(self, font):
        font.setPointSize(12)
        self.btn_local_music = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_local_music.setFont(font)
        self.btn_local_music.setObjectName("btn_local_music")
        self.gridLayout.addWidget(self.btn_local_music, 5, 1, 1, 1)

    def creation_lbl_selection(self, font):
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_selection = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_selection.setFont(font)
        self.lbl_selection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_selection.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_selection.setObjectName("lbl_selection")
        self.gridLayout.addWidget(self.lbl_selection, 1, 1, 1, 1)

    def assign_functions(self):
        self.btn_spotify.clicked.connect(self.connect_spotify)
        self.btn_local_music.clicked.connect(self.connect_local_music)

    def connect_spotify(self):
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=data.SPOTIFY_CLIENT_ID, 
        client_secret=data.SPOTIFY_CLIENT_SECRET, 
        redirect_uri="https://open.spotify.com", scope=data.SPOTIFY_SCOPE))
        if os.path.exists(data.CACHE_PATH) is False or os.path.getsize(data.CACHE_PATH) == 0:
            status = self.get_authorization_for_users(spotify)
        else:
            spotify.auth_manager.cache_handler.cache_path = data.CACHE_PATH
            status = self.open_web_spotify_player()

        if status:
            self.open_spotify_window(spotify)

    def get_authorization_for_users(self, spotify_api):
        while True:
            url = spotify_api.auth_manager.get_authorize_url()
            webbrowser.open(url)
            key, status = QtWidgets.QInputDialog.getText(self.centralwidget, 'Input Dialog', "Enter the URL you got." 
            "\nIt should start as https://open.spotify.com/?code=: ")
            if key.__contains__("https://open.spotify.com/?code=") and status:
                self.fetching_cache(key, spotify_api)
                return True
            elif status is False:
                return False
            else:
                self.error_web_spotify_player()

    def fetching_cache(self, key, spotify_api):
        code = spotify_api.auth_manager.parse_response_code(key)
        spotify_api.auth_manager.get_access_token(code)
        old_cache_path = os.path.abspath(os.path.join(os.getcwd(), ".cache"))
        os.replace(old_cache_path, data.CACHE_PATH)
        spotify_api.auth_manager.cache_handler.cache_path = data.CACHE_PATH

    def error_web_spotify_player(self):
        not_working = QtWidgets.QMessageBox()
        not_working.setWindowTitle("Invalid Input")
        not_working.setText("Please Enter the Correct URL.")
        not_working.setIcon(QtWidgets.QMessageBox.Critical)
        not_working.exec_()

    def open_web_spotify_player(self):
        webbrowser.open("https://open.spotify.com")
        return True

    def open_spotify_window(self, spotify_api):
        self.Spotify_Lyrics = QtWidgets.QMainWindow()
        self.spotify_window = Ui_Spotify_Window()
        self.spotify_window.setupUi(self.Spotify_Lyrics, spotify_api)
        self.Spotify_Lyrics.show()
        Selection_Window.close()

    def connect_local_music(self):
        if (os.path.exists(r"C:\\Program Files (x86)\\K-Lite Codec Pack\\MPC-HC64") is False):
            # TODO: Need to make this clear for mac users
            self.error_local_music_player()
        else:
            self.open_local_music_player()

    def error_local_music_player(self):
        webbrowser.open("https://www.codecguide.com/download_k-lite_codec_pack_standard.htm")
        warning = QtWidgets.QErrorMessage()
        warning.setWindowTitle("Warning!")
        warning.showMessage("You need to Download K-Lite Codec Pack!\n"
         "Select Server 1, and just click Next over and over in the Installator."
         "\n Once that is complete, then re-run the program.")
        warning.exec_()

    def open_local_music_player(self):
        self.simp = MediaWindow()
        self.simp.openFile()
        self.simp.resize(450, 25)
        self.simp.show()
        Selection_Window.close()

    def retranslateUi(self, Selection_Window):
        _translate = QtCore.QCoreApplication.translate
        Selection_Window.setWindowTitle(_translate("Selection_Window", 
        "Select your Music Player"))
        self.btn_spotify.setText(_translate("Selection_Window", 
        "Spotify"))
        self.btn_local_music.setText(_translate("Selection_Window", 
        "Local Music"))
        self.lbl_selection.setText(_translate("Selection_Window", 
        "Select Your Music Player"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Selection_Window = QtWidgets.QMainWindow()
    ui = Ui_Selection_Window()
    ui.setupUi(Selection_Window)
    Selection_Window.show()
    sys.exit(app.exec_())
