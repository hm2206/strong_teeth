from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton
from app import App


class AppScreen(QMainWindow):

    btn_save: QPushButton

    def __init__(self, app: App):
        super(AppScreen, self).__init__()
        uic.loadUi("ui/app.ui", self)
        self._app = app
