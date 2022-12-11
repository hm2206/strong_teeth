from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt5 import uic
from message_boxs.critical_message_box import CriticalMessageBox
from models.persona import Persona
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from screens.persona_frame import PersonaFrame
from models.trabajador import Trabajador
from models.turno import Turno
from models.doctor import Doctor


class TrabajadorDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    input_numero_essalud: QLineEdit
    input_cmp: QLineEdit
    cmb_persona: QComboBox
    cmb_turno: QComboBox

    def __init__(self, app: App, parent: PersonaFrame, title=""):
        super(TrabajadorDialog, self).__init__(parent=parent)
        uic.loadUi("ui/trabajador_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Trabajador()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)

    def showEvent(self, evt: QShowEvent):
        self.load_personas()
        self.load_turnos()
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Trabajador):
        self.entity = entity
        persona: Persona = entity.persona
        turno: Turno = entity.turno
        doctor: Doctor = entity.doctor
        self.input_numero_essalud.setText(entity.numero_essalud)
        self.cmb_persona.setCurrentText(persona.display_info())
        self.cmb_turno.setCurrentText(turno.nombre)

        if (doctor):
            self.input_cmp.setText(doctor.cmp)

    def load_personas(self):
        datos = session.query(Persona).all()
        for item in datos:
            persona: Persona = item
            self.cmb_persona.addItem(persona.display_info(), persona)

    def load_turnos(self):
        datos = session.query(Turno).all()
        for item in datos:
            turno: Turno = item
            self.cmb_turno.addItem(turno.nombre, turno)

    def save(self, evt: QObject):
        persona: Persona = self.cmb_persona.currentData()
        turno: Turno = self.cmb_turno.currentData()
        doctor: Doctor = self.entity.doctor

        cmp = self.input_cmp.text()

        self.entity.numero_essalud = self.input_numero_essalud.text()
        self.entity.persona_id = persona.id
        self.entity.turno_id = turno.id

        try:
            if (doctor and cmp):
                doctor.cmp = cmp
            elif (doctor and not cmp):
                session.delete(doctor)
            elif (not doctor and cmp):
                doctor = Doctor()
                doctor.cmp = cmp
                session.add(doctor)
            else:
                doctor = None

            self.entity.doctor = doctor
            session.add(self.entity)

            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load()
            self.close()
        except Exception:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
