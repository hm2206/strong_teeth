from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject, QAbstractItemModel
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QListWidget, QListWidgetItem, QDoubleSpinBox, QTextEdit, QComboBox, QDateEdit, QTimeEdit
from PyQt5 import uic
from sqlalchemy import desc, asc
from message_boxs.critical_message_box import CriticalMessageBox
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from screens.paciente_frame import PacienteFrame
from models.cita import Cita
from models.tratamiento import Tratamiento
from models.odontograma import Odontograma
from models.historia import Historia
from models.producto import Producto
from sqlalchemy.orm.collections import InstrumentedList
from models.doctor import Doctor
from datetime import datetime
from utils.cita_util import estado_to_str, str_to_estado
from models.cita_odontograma import CitaOdontograma
from models.cita_producto import CitaProducto


class PacienteCitaDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    btn_nuevo: QPushButton
    btn_cancelar: QPushButton

    cmb_info_cita: QComboBox
    date_fecha: QDateEdit
    time_hora: QTimeEdit
    cmb_doctor: QComboBox
    cmb_tratamiento: QComboBox
    cmb_estado: QComboBox
    txt_detalles: QTextEdit
    cmb_dientes: QComboBox
    cmb_prescripcion: QComboBox
    list_dientes: QListWidget
    list_prescripcion: QListWidget
    dbl_precio: QDoubleSpinBox
    dbl_pagado: QDoubleSpinBox

    dientes = InstrumentedList([])
    productos = InstrumentedList([])

    def __init__(self, app: App, parent: PacienteFrame, title=""):
        super(PacienteCitaDialog, self).__init__(parent=parent)
        uic.loadUi("ui/paciente_cita_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.paciente = parent.entity
        self.entity = Cita()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)
        self.btn_nuevo.clicked.connect(self.nuevo)
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.cmb_info_cita.currentIndexChanged.connect(self.select_cita)
        self.cmb_dientes.currentIndexChanged.connect(self.add_dientes)
        self.list_dientes.doubleClicked.connect(self.remove_dientes)
        self.cmb_prescripcion.currentIndexChanged.connect(
            self.add_prescripcion)
        self.list_prescripcion.doubleClicked.connect(self.remove_prescripcion)

    def showEvent(self, evt: QShowEvent):
        self.btn_cancelar.setEnabled(False)
        self.btn_nuevo.setEnabled(True)
        self.load_citas()
        self.load_doctor()
        self.load_tratamientos()
        self.load_dientes()
        self.load_prescripcion()
        self.datetime()
        return super().showEvent(evt)

    def datetime(self):
        self.time_hora.setTime(datetime.now().time())
        self.date_fecha.setDate(datetime.now().date())

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Cita):
        self.cmb_info_cita.setCurrentText(entity.display_info())
        self.date_fecha.setDate(entity.fecha)
        self.time_hora.setTime(entity.hora)
        self.cmb_doctor.setCurrentText(entity.doctor.display_info())
        self.cmb_tratamiento.setCurrentText(entity.tratamiento.display_info())
        self.cmb_estado.setCurrentText(estado_to_str(entity.estado))
        self.txt_detalles.setPlainText(entity.detalles)
        self.dbl_precio.setValue(entity.precio)
        self.dbl_pagado.setValue(entity.pagado)
        self.dientes = InstrumentedList(entity.odontogramas)
        self.productos = InstrumentedList(entity.productos)
        self.entity = entity
        self.draw_list_dientes()
        self.draw_list_prescripcion()

    def select_cita(self):
        obj: QComboBox = self.sender()
        self.entity: Cita = obj.currentData()
        if (self.entity and self.entity.id):
            self.load(self.entity)

    def load_citas(self):
        datos = session.query(Cita).filter_by(
            paciente_id=self.paciente.id).all()
        for item in datos:
            cita: Cita = item
            self.cmb_info_cita.addItem(cita.display_info(), cita)
        if (len(datos) > 0):
            self.load(datos[0])
            self.cmb_info_cita.setEnabled(True)
        else:
            self.cmb_info_cita.setEnabled(False)
            self.btn_nuevo.setEnabled(False)
            self.btn_cancelar.setEnabled(True)

    def load_doctor(self):
        self.cmb_doctor.addItem("seleccionar", None)
        datos = session.query(Doctor).all()
        for item in datos:
            doctor: Doctor = item
            self.cmb_doctor.addItem(doctor.display_info(), doctor)

    def load_tratamientos(self):
        self.cmb_tratamiento.addItem("Seleccionar", None)
        datos = session.query(Tratamiento).all()
        for item in datos:
            tratamiento: Tratamiento = item
            self.cmb_tratamiento.addItem(tratamiento.nombre, tratamiento)

    def load_dientes(self):
        historia: Historia = session.query(Historia).filter(
            Historia.paciente_id == self.paciente.id
        ).order_by(
            desc(Historia.fecha_inicio),
            desc(Historia.hora_inicio)
        ).first()

        self.cmb_dientes.addItem("seleccionar", None)

        if (not historia):
            return None

        datos = session.query(Odontograma).filter(
            Odontograma.historia_id == historia.id
        ).order_by(
            asc(Odontograma.numero_diente)
        ).all()

        for item in datos:
            odontograma: Odontograma = item
            self.cmb_dientes.addItem(
                odontograma.display_info(), odontograma)

    def add_dientes(self):
        combo: QComboBox = self.sender()
        data: Odontograma = combo.currentData()

        if (not data):
            return None

        count = list(filter(lambda x: (x.id == data.id), self.dientes))

        if (len(count)):
            return None

        item = QListWidgetItem()
        item.setText(data.display_info())
        item.setData(1, data)
        self.list_dientes.addItem(item)
        self.dientes.append(data)
        self.cmb_dientes.setCurrentIndex(0)

    def remove_dientes(self):
        list_items: QListWidget = self.sender()
        item: QListWidgetItem = list_items.currentItem()
        self.list_dientes.takeItem(list_items.currentRow())
        odontograma: Odontograma = item.data(1)
        tmp_datos = list(
            filter(lambda x: (x.id != odontograma.id), self.dientes))
        self.dientes = InstrumentedList(tmp_datos)
        self.cmb_dientes.setCurrentIndex(0)

    def draw_list_dientes(self):
        self.list_dientes.clear()
        for diente in self.dientes:
            item = QListWidgetItem()
            item.setText(diente.display_info())
            item.setData(1, diente)
            self.list_dientes.addItem(item)

    def load_prescripcion(self):
        datos = session.query(Producto).all()
        self.cmb_prescripcion.addItem("Seleccionar", None)
        for item in datos:
            producto: Producto = item
            self.cmb_prescripcion.addItem(producto.display_info(), producto)

    def add_prescripcion(self):
        combo: QComboBox = self.sender()
        data: Producto = combo.currentData()

        if (not data):
            return None

        count = list(filter(lambda x: (x.id == data.id), self.productos))

        if (len(count)):
            return None

        item = QListWidgetItem()
        item.setText(data.display_info())
        item.setData(1, data)
        self.list_prescripcion.addItem(item)
        self.productos.append(data)
        self.cmb_prescripcion.setCurrentIndex(0)

    def remove_prescripcion(self):
        list_items: QListWidget = self.sender()
        item: QListWidgetItem = list_items.currentItem()
        self.list_prescripcion.takeItem(list_items.currentRow())
        producto: Producto = item.data(1)
        tmp_datos = list(
            filter(lambda x: (x.id != producto.id), self.productos))
        self.productos = InstrumentedList(tmp_datos)
        self.cmb_prescripcion.setCurrentIndex(0)

    def draw_list_prescripcion(self):
        self.list_prescripcion.clear()
        for producto in self.productos:
            item = QListWidgetItem()
            item.setText(producto.display_info())
            item.setData(1, producto)
            self.list_prescripcion.addItem(item)

    def save(self, evt: QObject):
        try:
            self.entity.fecha = self.date_fecha.date().toPyDate()
            self.entity.hora = self.time_hora.time().toPyTime()
            self.entity.estado = str_to_estado(self.cmb_estado.currentText())
            self.entity.detalles = self.txt_detalles.toPlainText()
            self.entity.precio = self.dbl_precio.value()
            self.entity.pagado = self.dbl_pagado.value()
            self.entity.paciente = self.paciente

            # add doctor
            doctor = self.cmb_doctor.currentData()
            if (doctor):
                self.entity.doctor = doctor

            # add tratamiento
            tratamiento = self.cmb_tratamiento.currentData()
            if (tratamiento):
                self.entity.tratamiento = tratamiento

            session.add(self.entity)

            # eliminar datos temporales
            if (self.entity.id):
                session.query(CitaOdontograma).filter_by(
                    cita_id=self.entity.id).delete()
                session.query(CitaProducto).filter_by(
                    cita_id=self.entity.id).delete()

            # add odontogramas
            self.entity.odontogramas.extend(self.dientes)

            # add productos
            self.entity.productos.extend(self.productos)

            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self.load_citas()
        except Exception as e:
            print(e)
            self.btn_nuevo.setEnabled(False)
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
        finally:
            self.btn_nuevo.setEnabled(True)
            self.btn_cancelar.setEnabled(False)

    def nuevo(self):
        self.entity = Cita()
        self.cmb_info_cita.setEnabled(False)
        self.btn_cancelar.setEnabled(True)
        self.btn_nuevo.setEnabled(False)
        self.datetime()
        self.txt_detalles.setPlainText("")
        self.dbl_precio.setValue(0)
        self.dbl_pagado.setValue(0)
        self.cmb_estado.setCurrentIndex(0)
        self.cmb_dientes.setCurrentIndex(0)
        self.cmb_prescripcion.setCurrentIndex(0)
        self.cmb_doctor.setCurrentIndex(0)
        self.cmb_tratamiento.setCurrentIndex(0)
        self.cmb_estado.setCurrentIndex(0)
        self.dientes = InstrumentedList([])
        self.productos = InstrumentedList([])
        self.list_dientes.clear()
        self.list_prescripcion.clear()
        self.cmb_info_cita.clear()

    def cancelar(self):
        self.nuevo()
        self.btn_cancelar.setEnabled(False)
        self.btn_nuevo.setEnabled(True)
        self.load_citas()
