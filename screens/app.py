from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QShowEvent
from app import App


class AppScreen(QMainWindow):

    lbl_username: QLabel
    btn_logout: QPushButton

    def __init__(self, app: App):
        super(AppScreen, self).__init__()
        uic.loadUi("ui/app.ui", self)
        self._app = app

        self.btn_logout.clicked.connect(self.logout)

    def showEvent(self, evt: QShowEvent):
        self.auth = self._app.auth
        self.lbl_username.setText(self.auth.email)
        return super().showEvent(evt)

    def logout(self):
        self.close()
        self._app.distroy_session()
        self._app.login_screen.show()
