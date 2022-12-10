from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QPushButton, QFrame, QTableWidget, QDialog, QTableWidgetItem, QLabel, QTableWidgetItem
from PyQt5 import uic
from configs.db import session
from models.paciente import Paciente
from models.persona import Persona
from utils.paciente_util import condicion_to_str


class PacienteFrame(QFrame):

    table: QTableWidget
    btn_plus: QPushButton
    frm_footer: QFrame

    lbl_selected: QLabel

    btn_cita: QPushButton
    btn_historia: QPushButton
    btn_odontograma: QPushButton
    btn_tratamiento: QPushButton

    current_pacient: Paciente

    def __init__(self, app: App, parent=None):
        super(PacienteFrame, self).__init__(parent=parent)
        uic.loadUi("ui/paciente_frame.ui", self)
        self._app = app
        self.entity = Paciente()

        self.btn_plus.clicked.connect(self.action_create)
        self.table.doubleClicked.connect(self.action_edit)
        self.table.itemClicked.connect(self.action_item)
        self.dispatch_dialogs()

    def dispatch_dialogs(self):
        from dialogs.paciente_odontograma_dialog import PacienteOdontogramaDialog
        self.btn_odontograma.clicked.connect(
            lambda x: self.action_dialog(PacienteOdontogramaDialog))

    def showEvent(self, evt: QShowEvent):
        self.load()
        self.frm_footer.setEnabled(False)
        return super().showEvent(evt)

    def action_create(self, evt: QEvent):
        from dialogs.paciente_dialog import PacienteDialog
        self._app.app_screen.set_enabled_window(False)
        self.msg = PacienteDialog(
            self._app, self, title="Crear Paciente")
        self.msg.show()

    def action_edit(self, evt: QEvent):
        from dialogs.paciente_dialog import PacienteDialog
        self._app.app_screen.set_enabled_window(False)
        row = self.table.selectionModel().currentIndex().row()
        id = self.table.item(row, 0).text()
        self.entity = session.query(Paciente).get(id)
        self.msg = PacienteDialog(
            self._app, self, title="Editar Paciente")
        self.msg.show()
        self.msg.load(self.entity)

    def action_item(self, evt: QEvent):
        row = self.table.currentRow()
        id = self.table.item(row, 0).text()
        self.entity: Paciente = session.query(Paciente).get(id)
        persona: Persona = self.entity.persona
        self.frm_footer.setEnabled(True)
        self.lbl_selected.setText(persona.display_info())

    def action_dialog(self, Dialog: QDialog):
        self._app.app_screen.set_enabled_window(False)
        msg: QDialog = Dialog(self._app, self)
        msg.setEnabled(True)
        msg.show()

    def load(self):
        self.data = session.query(Paciente).all()
        self.table.setRowCount(self.data.__len__())
        for index, item in enumerate(self.data):
            entity: Paciente = item
            persona: Persona = entity.persona

            self.table.setItem(index, 0, QTableWidgetItem(str(entity.id)))
            self.table.setItem(index, 1, QTableWidgetItem(
                persona.display_nombre()))
            self.table.setItem(index, 2, QTableWidgetItem(
                persona.numero_identidad))
            self.table.setItem(index, 3, QTableWidgetItem(
                condicion_to_str(entity.condicion)))
            self.table.resizeColumnsToContents()
