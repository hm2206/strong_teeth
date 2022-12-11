from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QPlainTextEdit, QDateEdit, QTimeEdit
from PyQt5 import uic
from message_boxs.critical_message_box import CriticalMessageBox
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from dialogs.paciente_odontograma_dialog import PacienteOdontogramaDialog
from models.historia import Historia
from datetime import datetime


class HistoriaDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    date_fecha: QDateEdit
    time_hora: QTimeEdit
    txt_observacion: QPlainTextEdit

    def __init__(self, app: App, parent: PacienteOdontogramaDialog, title=""):
        super(HistoriaDialog, self).__init__(parent=parent)
        uic.loadUi("ui/historia_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Historia()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)
        self.date_fecha.setDate(datetime.now().date())
        self.time_hora.setTime(datetime.now().time())

    def showEvent(self, evt: QShowEvent):
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Historia):
        self.entity = entity
        self.date_fecha.setDate(entity.fecha_inicio)
        self.time_hora.setTime(entity.hora_inicio)
        self.txt_observacion.setPlainText(entity.observacion)

    def save(self, evt: QObject):
        self.entity.fecha_inicio = self.date_fecha.date().toPyDate()
        self.entity.hora_inicio = self.time_hora.time().toPyTime()
        self.entity.observacion = self.txt_observacion.toPlainText()
        self.entity.paciente_id = self._frm_parent.paciente.id
        session.add(self.entity)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load_historial()
            self._frm_parent.load_data()
            self.close()
        except Exception as e:
            print(e)
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
