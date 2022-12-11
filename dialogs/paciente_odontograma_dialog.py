from app import App
from PyQt5.QtGui import QShowEvent, QStandardItemModel, QStandardItem
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QFrame, QComboBox, QTimeEdit, QPlainTextEdit
from PyQt5 import uic
from configs.db import session
from sqlalchemy import desc
from screens.paciente_frame import PacienteFrame
from models.odontograma import Odontograma
from models.condicion_dental import CondicionDental
from models.historia import Historia
from models.paciente import Paciente


class PacienteOdontogramaDialog(QDialog):

    lbl_title: QLabel
    frm_odontograma: QFrame
    cmb_fecha: QComboBox
    time_hora: QTimeEdit
    txt_observacion: QPlainTextEdit
    btn_nuevo: QPushButton
    btn_editar: QPushButton

    btn_11: QPushButton
    btn_12: QPushButton
    btn_13: QPushButton
    btn_14: QPushButton
    btn_15: QPushButton
    btn_16: QPushButton
    btn_17: QPushButton
    btn_18: QPushButton
    btn_21: QPushButton
    btn_22: QPushButton
    btn_23: QPushButton
    btn_24: QPushButton
    btn_25: QPushButton
    btn_26: QPushButton
    btn_27: QPushButton
    btn_28: QPushButton
    btn_31: QPushButton
    btn_32: QPushButton
    btn_33: QPushButton
    btn_34: QPushButton
    btn_35: QPushButton
    btn_36: QPushButton
    btn_37: QPushButton
    btn_38: QPushButton
    btn_41: QPushButton
    btn_42: QPushButton
    btn_43: QPushButton
    btn_44: QPushButton
    btn_45: QPushButton
    btn_46: QPushButton
    btn_47: QPushButton
    btn_48: QPushButton
    btn_51: QPushButton
    btn_52: QPushButton
    btn_53: QPushButton
    btn_54: QPushButton
    btn_55: QPushButton
    btn_56: QPushButton
    btn_61: QPushButton
    btn_62: QPushButton
    btn_63: QPushButton
    btn_64: QPushButton
    btn_65: QPushButton
    btn_71: QPushButton
    btn_72: QPushButton
    btn_73: QPushButton
    btn_74: QPushButton
    btn_75: QPushButton
    btn_81: QPushButton
    btn_82: QPushButton
    btn_83: QPushButton
    btn_84: QPushButton
    btn_85: QPushButton

    def __init__(self, app: App, parent: PacienteFrame):
        super(PacienteOdontogramaDialog, self).__init__(parent=parent)
        uic.loadUi("ui/paciente_odontograma_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Odontograma()
        self.historia = Historia()
        self.paciente: Paciente = parent.entity
        self.lbl_title.setText(
            f"Historia Dental: {parent.entity.persona.display_nombre()}")
        self.dispatch_events()

    def dispatch_events(self):
        self.btn_11.clicked.connect(self.toggle_odontograma)
        self.btn_12.clicked.connect(self.toggle_odontograma)
        self.btn_13.clicked.connect(self.toggle_odontograma)
        self.btn_14.clicked.connect(self.toggle_odontograma)
        self.btn_15.clicked.connect(self.toggle_odontograma)
        self.btn_16.clicked.connect(self.toggle_odontograma)
        self.btn_17.clicked.connect(self.toggle_odontograma)
        self.btn_18.clicked.connect(self.toggle_odontograma)
        self.btn_21.clicked.connect(self.toggle_odontograma)
        self.btn_22.clicked.connect(self.toggle_odontograma)
        self.btn_23.clicked.connect(self.toggle_odontograma)
        self.btn_24.clicked.connect(self.toggle_odontograma)
        self.btn_25.clicked.connect(self.toggle_odontograma)
        self.btn_26.clicked.connect(self.toggle_odontograma)
        self.btn_27.clicked.connect(self.toggle_odontograma)
        self.btn_28.clicked.connect(self.toggle_odontograma)
        self.btn_31.clicked.connect(self.toggle_odontograma)
        self.btn_32.clicked.connect(self.toggle_odontograma)
        self.btn_33.clicked.connect(self.toggle_odontograma)
        self.btn_34.clicked.connect(self.toggle_odontograma)
        self.btn_35.clicked.connect(self.toggle_odontograma)
        self.btn_36.clicked.connect(self.toggle_odontograma)
        self.btn_37.clicked.connect(self.toggle_odontograma)
        self.btn_38.clicked.connect(self.toggle_odontograma)
        self.btn_41.clicked.connect(self.toggle_odontograma)
        self.btn_42.clicked.connect(self.toggle_odontograma)
        self.btn_43.clicked.connect(self.toggle_odontograma)
        self.btn_44.clicked.connect(self.toggle_odontograma)
        self.btn_45.clicked.connect(self.toggle_odontograma)
        self.btn_46.clicked.connect(self.toggle_odontograma)
        self.btn_47.clicked.connect(self.toggle_odontograma)
        self.btn_48.clicked.connect(self.toggle_odontograma)
        self.btn_51.clicked.connect(self.toggle_odontograma)
        self.btn_52.clicked.connect(self.toggle_odontograma)
        self.btn_53.clicked.connect(self.toggle_odontograma)
        self.btn_54.clicked.connect(self.toggle_odontograma)
        self.btn_55.clicked.connect(self.toggle_odontograma)
        self.btn_61.clicked.connect(self.toggle_odontograma)
        self.btn_62.clicked.connect(self.toggle_odontograma)
        self.btn_63.clicked.connect(self.toggle_odontograma)
        self.btn_64.clicked.connect(self.toggle_odontograma)
        self.btn_65.clicked.connect(self.toggle_odontograma)
        self.btn_71.clicked.connect(self.toggle_odontograma)
        self.btn_72.clicked.connect(self.toggle_odontograma)
        self.btn_73.clicked.connect(self.toggle_odontograma)
        self.btn_74.clicked.connect(self.toggle_odontograma)
        self.btn_75.clicked.connect(self.toggle_odontograma)
        self.btn_81.clicked.connect(self.toggle_odontograma)
        self.btn_82.clicked.connect(self.toggle_odontograma)
        self.btn_83.clicked.connect(self.toggle_odontograma)
        self.btn_84.clicked.connect(self.toggle_odontograma)
        self.btn_85.clicked.connect(self.toggle_odontograma)
        self.btn_nuevo.clicked.connect(self.nueva_historia)
        self.btn_editar.clicked.connect(self.editar_historia)
        self.cmb_fecha.currentIndexChanged.connect(self.change_fecha)

    def showEvent(self, evt: QShowEvent):
        self.cmb_fecha.setEnabled(False)
        self.btn_editar.setEnabled(False)
        self.load_historial()
        self.load_data()
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load_historial(self):
        paciente: Paciente = self._frm_parent.entity
        items = session.query(Historia).filter(
            Historia.paciente_id == paciente.id).order_by(
                desc(Historia.fecha_inicio), desc(Historia.hora_inicio)
        ).all()

        model = QStandardItemModel(0, 1)
        self.cmb_fecha.setModel(model)

        for item in items:
            historia: Historia = item
            self.cmb_fecha.addItem(historia.display_info(), historia)

        if (len(items) > 0):
            self.historia: Historia = items[0]

    def load_data(self):
        self.validate_historia()

    def load_odontogramas(self):
        self.frm_odontograma.setEnabled(False)
        self.datos = session.query(Odontograma).filter(
            Odontograma.historia_id == self.historia.id).all()
        self.clear_teeth()
        self.draw_teeth()
        self.frm_odontograma.setEnabled(True)

    def validate_historia(self):
        if (self.historia.id):
            self.draw_historia()
        else:
            self.btn_editar.setEnabled(False)
            self.cmb_fecha.setEnabled(False)
            self.frm_odontograma.setEnabled(False)

    def draw_historia(self):
        self.cmb_fecha.setEnabled(True)
        self.cmb_fecha.setCurrentText(self.historia.display_info())
        self.txt_observacion.setPlainText(self.historia.observacion)
        self.load_odontogramas()
        self.btn_editar.setEnabled(True)

    def draw_teeth(self, ):
        for data in self.datos:
            item: Odontograma = data
            object_name = f"btn_{item.numero_diente}"
            btn: QPushButton = self.__getattribute__(object_name)
            color_fondo = item.condicion.color_fondo
            color_texto = item.condicion.color_texto
            btn.setStyleSheet(
                f"background-color: {color_fondo}; color: {color_texto}")

    def toggle_odontograma(self):
        from dialogs.odontograma_dialog import OdontogramaDialog
        btn: QPushButton = self.sender()
        numero_diente = int(btn.text())
        tmp_teeth = list(filter(lambda i: (i.numero_diente ==
                         numero_diente), self.datos))
        # config dialog
        self._app.app_screen.set_enabled_window(False)
        # validar teeth editar
        if (len(tmp_teeth) == 1):
            dialog = OdontogramaDialog(self._app, self, "Editar Odontograma")
            id = tmp_teeth[0].id
            self.entity = session.query(Odontograma).get(id)
        else:
            dialog = OdontogramaDialog(self._app, self, "Crear Odontograma")
            self.entity = Odontograma()
            self.entity.condicion = session.query(CondicionDental).first()
            self.entity.numero_diente = numero_diente
            self.entity.historia = self.historia

        # cargar datos
        dialog.setEnabled(True)
        dialog.show()
        dialog.load(self.entity)

    def change_fecha(self, evt: QEvent):
        obj: QComboBox = self.sender()
        self.historia: Historia = obj.currentData()
        if (self.historia and self.historia.id):
            self.load_data()

    def clear_teeth(self):
        collects = [
            range(11, 19),
            range(21, 29),
            range(31, 39),
            range(41, 49),
            range(51, 56),
            range(61, 66),
            range(71, 76),
            range(81, 86)
        ]

        for teeths in collects:
            for teeth in teeths:
                object_name = f"btn_{teeth}"
                btn: QPushButton = self.__getattribute__(object_name)
                color_fondo = "white"
                color_texto = "gray"
                btn.setStyleSheet(
                    f"background-color: {color_fondo}; color: {color_texto}"
                )

    def nueva_historia(self):
        from dialogs.historia_dialog import HistoriaDialog
        dialog = HistoriaDialog(self._app, self, title="Crear Historia Dental")
        dialog.show()

    def editar_historia(self):
        from dialogs.historia_dialog import HistoriaDialog
        dialog = HistoriaDialog(
            self._app, self, title="Editar Historia Dental")
        dialog.show()
        dialog.load(self.historia)
