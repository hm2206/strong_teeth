from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from PyQt5.QtCore import QEvent
import json
from validations.login_validator import login_validator
from app import App
import bcrypt
import json
from configs.db import session
from models.usuario import Usuario
from message_boxs.critical_message_box import CriticalMessageBox


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

        is_valid_data = login_validator(
            username=self.input_username.text(),
            password=self.input_password.text()
        )

        if (not is_valid_data):
            self.clear_submit()
            return None

        is_valid = self.validate_user()

        if (not is_valid):
            self.error_credential()
            return None

        self.save_session()
        self.close()
        self.clear_submit()
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

    def clear_password(self):
        self.input_username.setEnabled(True)
        self.input_password.setText("")
        self.input_password.setEnabled(True)
        self.btn_save.setText("Entrar")
        self.btn_save.setEnabled(False)

    def block_components(self):
        self.btn_save.setEnabled(False)
        self.input_password.setEnabled(False)
        self.input_username.setEnabled(False)

    def validate_user(self) -> bool:
        try:
            email = self.input_username.text()
            user: Usuario = session.query(
                Usuario).filter_by(email=email).first()

            if (not user):
                return False

            bytes_hashed = str(user.password).encode("utf-8")
            bytes_password = self.input_password.text().encode("utf-8")

            is_valid = bcrypt.checkpw(bytes_password, bytes_hashed)

            if (is_valid):
                self._app.auth = user

            return is_valid
        except Exception:
            return False

    def save_session(self):
        auth = self._app.auth
        with open(self._app.path_session, "w") as file:
            json.dump({"user_id": auth.id, "token": auth.password}, file)

    def clear_submit(self):
        self.input_username.setText("")
        self.input_username.setEnabled(True)
        self.input_password.setText("")
        self.input_password.setEnabled(False)
        self.btn_save.setText("Entrar")
        self.btn_save.setEnabled(False)

    def enable_submit(self):
        self.btn_save.setEnabled(True)
        self.btn_save.setText("Entrar")

    def error_credential(self):
        msg = CriticalMessageBox(
            title="No autorizado",
            text="Las credenciales de accesso son invalidas!!!"
        )

        msg.exec()
        self.clear_password()
