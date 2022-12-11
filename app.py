from PyQt5 import QtWidgets
from configs.migration import Migration
import sys
import json
import os
from models.usuario import Usuario
from configs.db import session


class App:

    path_session = "storage/session.json"
    auth: Usuario

    def __init__(self):
        self._app = QtWidgets.QApplication([])

    def _imports(self):
        from screens.app import AppScreen
        from screens.login import LoginScreen

        self.app_screen = AppScreen(self)
        self.login_screen = LoginScreen(self)

    def run(self):
        self._imports()
        self.verify_session()
        sys.exit(self._app.exec())

    def configs(self):
        migration = Migration()
        migration.run()

    def context(self):
        return self._app

    def verify_session(self):
        exists_session = os.path.exists(self.path_session)

        if (not exists_session):
            self.login_screen.show()
            return None

        self.open_session()

    def open_session(self):
        with open(self.path_session) as file:
            try:
                info = json.load(file)
                user_id = info["user_id"]
                token = info["token"]
                user: Usuario = session.query(
                    Usuario).filter_by(id=user_id).first()

                if (not user):
                    raise Exception("El usuario es invalido")

                if (token != user.password):
                    raise Exception("El token es invalido")

                self.auth = user
                self.app_screen.show()
            except Exception as e:
                print(e)
                self.login_screen.show()

    def distroy_session(self):
        self.auth = None
        if (os.path.exists(self.path_session)):
            os.remove(self.path_session)

    def exit(self):
        sys.exit()
