from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QPlainTextEdit, QSpinBox, QComboBox
from PyQt5 import uic
from message_boxs.critical_message_box import CriticalMessageBox
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from models.odontograma import Odontograma
from dialogs.paciente_odontograma_dialog import PacienteOdontogramaDialog
from models.condicion_dental import CondicionDental


class OdontogramaDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    spn_diente: QSpinBox
    cmb_condicion: QComboBox
    txt_observacion: QPlainTextEdit

    def __init__(self, app: App, parent: PacienteOdontogramaDialog, title=""):
        super(OdontogramaDialog, self).__init__(parent=parent)
        uic.loadUi("ui/odontograma_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Odontograma()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)

    def showEvent(self, evt: QShowEvent):
        self.load_condicion()
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Odontograma):
        self.entity = entity
        self.spn_diente.setValue(entity.numero_diente)
        self.cmb_condicion.setCurrentText(entity.condicion.nombre)
        self.txt_observacion.setPlainText(entity.observacion)

    def load_condicion(self):
        condiciones = session.query(CondicionDental).all()
        for condicion in condiciones:
            self.cmb_condicion.addItem(condicion.nombre, condicion)

    def save(self, evt: QObject):
        self.entity.numero_diente = self.spn_diente.value()

        condicion = self.cmb_condicion.currentData()
        if (condicion):
            self.entity.condicion = condicion

        self.entity.observacion = self.txt_observacion.toPlainText()
        session.add(self.entity)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load_data()
            self.close()
        except Exception:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
