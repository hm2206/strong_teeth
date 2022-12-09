from PyQt5 import uic
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame
from PyQt5.QtGui import QShowEvent
from app import App


class AppScreen(QMainWindow):

    lbl_username: QLabel
    btn_logout: QPushButton

    frm_header: QFrame
    frm_main: QFrame
    frm_barra: QFrame

    btn_personas: QPushButton
    btn_usuarios: QPushButton
    btn_marcas: QPushButton
    btn_proveedores: QPushButton
    btn_turno: QPushButton
    btn_trabajadores: QPushButton
    btn_tratamiento: QPushButton
    btn_pacientes: QPushButton

    def __init__(self, app: App):
        super(AppScreen, self).__init__()
        uic.loadUi("ui/app.ui", self)
        self._app = app

        self.btn_logout.clicked.connect(self.logout)

    def showEvent(self, evt: QShowEvent):
        self.event_module()
        self.auth = self._app.auth
        self.lbl_username.setText(self.auth.email)
        return super().showEvent(evt)

    def logout(self):
        self.hide()
        self._app.distroy_session()
        self._app.login_screen.show()

    def event_module(self):
        from screens.persona_frame import PersonaFrame
        from screens.usuario_frame import UsuarioFrame
        from screens.marca_frame import MarcaFrame
        from screens.proveedor_frame import ProveedorFrame
        from screens.turno_frame import TurnoFrame
        from screens.trabajador_frame import TrabajadorFrame
        from screens.tratamiento_frame import TratamientoFrame
        from screens.paciente_frame import PacienteFrame

        self.btn_personas.clicked.connect(
            lambda evt: self.open_module(evt, PersonaFrame))
        self.btn_usuarios.clicked.connect(
            lambda evt: self.open_module(evt, UsuarioFrame))
        self.btn_marcas.clicked.connect(
            lambda evt: self.open_module(evt, MarcaFrame))
        self.btn_proveedores.clicked.connect(
            lambda evt: self.open_module(evt, ProveedorFrame))
        self.btn_turno.clicked.connect(
            lambda evt: self.open_module(evt, TurnoFrame))
        self.btn_trabajadores.clicked.connect(
            lambda evt: self.open_module(evt, TrabajadorFrame))
        self.btn_tratamiento.clicked.connect(
            lambda evt: self.open_module(evt, TratamientoFrame))
        self.btn_pacientes.clicked.connect(
            lambda evt: self.open_module(evt, PacienteFrame))

    def open_module(self, evt: QObject, Frame: QFrame):
        frame = Frame(self._app, parent=self.frm_main)
        frame.setFrameRect(self.frm_main.frameRect())
        self.frm_main = frame
        self.frm_main.show()

    def set_enabled_window(self, value: bool):
        self.frm_main.setEnabled(value)
        self.frm_barra.setEnabled(value)
        self.btn_logout.setEnabled(value)
