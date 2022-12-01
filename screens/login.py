from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtGui import QCloseEvent
import sys
from validations.login_validator import login_validator
from app import App
import bcrypt
from PyQt5.QtWidgets import QMessageBox


class LoginScreen(QMainWindow):

    input_username: QLineEdit
    input_password: QLineEdit
    btn_save: QPushButton

    def __init__(self, app: App):
        super(LoginScreen, self).__init__()
        uic.loadUi("ui/login.ui", self)
        self._app = app

        self.input_username.textChanged.connect(self.change_username)
        self.input_password.textChanged.connect(self.change_password)
        self.btn_save.clicked.connect(self.submit)
        self.disable_default()

    def submit(self, evt: QEvent):
        self.btn_save.setEnabled(False)
        self.btn_save.setText("Validando...")

        login_validator(
            username=self.input_username.text(),
            password=self.input_password.text()
        )

        password = b"nomeacuerdo73"
        hashed = bcrypt.hashpw(b"nomeacuerdo73", bcrypt.gensalt(14))
        is_valid = bcrypt.checkpw(password, hashed)

        if (not is_valid):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.critical)
            msg.setWindowTitle("No autorizado")
            msg.setText("Las credenciales de accesso son invalidas!!!")
            self.disable_default()
            return None

        self.hide()
        self._app.app_screen.show()

    def change_username(self, evt: QEvent):
        if (self.input_username.text().__len__() > 0):
            self.input_password.setEnabled(True)

    def change_password(self, evt: QEvent):
        if (self.input_password.text().__len__() > 0):
            self.btn_save.setEnabled(True)

    def disable_default(self):
        self.btn_save.setEnabled(False)
        self.btn_save.setText("Entrar")
        self.input_password.setEnabled(False)
        self.input_username.setEnabled(True)

    def block_components(self):
        self.btn_save.setEnabled(False)
        self.input_password.setEnabled(False)
        self.input_username.setEnabled(False)

    def closeEvent(self, evt: QCloseEvent):
        self._app.exit()
