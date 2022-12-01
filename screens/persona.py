from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtCore import QEvent, QObject
from app import App
from configs.db import session
from models.persona import Persona, PersonGeneroEnum


class PersonScreen(QMainWindow):

    btn_save: QPushButton

    def __init__(self, app: App):
        super(PersonScreen, self).__init__()
        uic.loadUi("ui/persona.ui", self)
        self._app = app

        self.btn_save.clicked.connect(self.btn_save_click)

    def btn_save_click(self, evt: QEvent):
        print("ok")
