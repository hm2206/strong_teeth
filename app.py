from PyQt5 import QtWidgets
from configs.migration import Migration
import sys


class App:

    def __init__(self):
        self._app = QtWidgets.QApplication([])

    def _imports(self):
        from screens.app import AppScreen
        from screens.login import LoginScreen
        from screens.persona import PersonScreen

        self.app_screen = AppScreen(self)
        self.login_screen = LoginScreen(self)
        self.persona_screen = PersonScreen(self)

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
        print("ok")
        self.app_screen.show()
        self.app_screen.setFocus(False)
        self.login_screen.show()

    def exit(self):
        sys.exit()
