from PyQt5 import QtCore, QtGui, QtWidgets
from Spotify_1 import Ui_Spotify_Window
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import os.path


class Ui_Selection_Window(object):
    def setupUi(self, Selection_Window):
        Selection_Window.setObjectName("Selection_Window")
        Selection_Window.resize(256, 256)
        self.centralwidget = QtWidgets.QWidget(Selection_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_spotify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_spotify.setGeometry(QtCore.QRect(80, 90, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btn_spotify.setFont(font)
        self.btn_spotify.setObjectName("btn_spotify")
        self.btn_local_music = QtWidgets.QPushButton(self.centralwidget)
        self.btn_local_music.setGeometry(QtCore.QRect(80, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btn_local_music.setFont(font)
        self.btn_local_music.setObjectName("btn_local_music")
        self.lbl_selection = QtWidgets.QLabel(self.centralwidget)
        self.lbl_selection.setGeometry(QtCore.QRect(10, 20, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_selection.setFont(font)
        self.lbl_selection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_selection.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_selection.setObjectName("lbl_selection")
        Selection_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Selection_Window)
        QtCore.QMetaObject.connectSlotsByName(Selection_Window)
    
    def get_authorization_for_users(self,spotify_api):
        
        is_authorizated = False
        while is_authorizated is False:
            url = spotify_api.auth_manager.get_authorize_url()
            webbrowser.open(url)

            key, status = QtWidgets.QInputDialog.getText(self.centralwidget, 'Input Dialog', "Enter the URL you got.\nIt should start as https://open.spotify.com/?code=: ")
            
            if key.__contains__("https://open.spotify.com/?code=") and status:
                code = spotify_api.auth_manager.parse_response_code(key)
                spotify_api.auth_manager.get_access_token(code)
                is_authorizated = True
                return True

            elif status is False:
                is_authorizated = True
                return False

            else:
                not_working = QtWidgets.QMessageBox()
                not_working.setWindowTitle("Invalid Input")
                not_working.setText("Please Enter the Correct URL.")
                not_working.setIcon(QtWidgets.QMessageBox.Critical)
                x = not_working.exec_()

            
        
    def open_web_spotify_player(self):
        webbrowser.open("https://open.spotify.com")
        return True

    def connect_spotify(self):
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fd435a4fa71949f2a235179ff3ef3010", client_secret= "4bb5c3ce498847bfbdfde31c3e615080", redirect_uri="https://open.spotify.com", scope="user-read-playback-state, user-modify-playback-state"))
        if os.path.exists(spotify.auth_manager.cache_handler.cache_path) is False:
            status = self.get_authorization_for_users(spotify)
        else:
            status = self.open_web_spotify_player()

        if status:
            self.open_spotify_window(spotify)
        
    def open_spotify_window(self, spotify_api):
        self.Spotify_Lyrics = QtWidgets.QMainWindow()
        self.spotify_window = Ui_Spotify_Window()
        self.spotify_window.setupUi(self.Spotify_Lyrics, spotify_api)
        self.Spotify_Lyrics.show()
    
    def connect_local_music(self):
        print("clicked")
        pass
    
    def retranslateUi(self, Selection_Window):
        _translate = QtCore.QCoreApplication.translate
        Selection_Window.setWindowTitle(_translate("Selection_Window", "MainWindow"))
        self.btn_spotify.setText(_translate("Selection_Window", "Spotify"))
        self.btn_local_music.setText(_translate("Selection_Window", "Local Music"))
        self.lbl_selection.setText(_translate("Selection_Window", "Select Your Music Player"))
        self.btn_spotify.clicked.connect(self.connect_spotify)
        self.btn_local_music.clicked.connect(self.connect_local_music)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Selection_Window = QtWidgets.QMainWindow()
    ui = Ui_Selection_Window()
    ui.setupUi(Selection_Window)
    Selection_Window.show()
    sys.exit(app.exec_())