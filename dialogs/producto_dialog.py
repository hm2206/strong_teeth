from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QComboBox, QPlainTextEdit, QDoubleSpinBox
from PyQt5 import uic
from message_boxs.critical_message_box import CriticalMessageBox
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from models.producto import Producto
from models.proveedor import Proveedor
from models.marca import Marca
from screens.producto_frame import ProductoFrame


class ProductoDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    cmb_proveedor: QComboBox
    cmb_marca: QComboBox
    input_nombre: QLineEdit
    txt_descripcion: QPlainTextEdit
    dbl_stock: QDoubleSpinBox
    dbl_precio_compra: QDoubleSpinBox
    dbl_precio_venta: QDoubleSpinBox

    def __init__(self, app: App, parent: ProductoFrame, title=""):
        super(ProductoDialog, self).__init__(parent=parent)
        uic.loadUi("ui/producto_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Producto()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)

    def showEvent(self, evt: QShowEvent):
        self.load_proveedor()
        self.load_marca()
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Producto):
        self.entity = entity
        self.cmb_proveedor.setCurrentText(entity.proveedor.razon_social)
        self.cmb_marca.setCurrentText(entity.marca.nombre)
        self.input_nombre.setText(entity.nombre)
        self.txt_descripcion.setPlainText(entity.descripcion)
        self.dbl_stock.setValue(entity.stock)
        self.dbl_precio_compra.setValue(entity.precio_compra)
        self.dbl_precio_venta.setValue(entity.precio_venta)

    def load_proveedor(self):
        datos = session.query(Proveedor).all()
        for item in datos:
            preveedor: Proveedor = item
            self.cmb_proveedor.addItem(preveedor.razon_social, preveedor)

    def load_marca(self):
        datos = session.query(Marca).all()
        for item in datos:
            marca: Marca = item
            self.cmb_marca.addItem(marca.nombre, marca)

    def save(self, evt: QObject):
        proveedor: Proveedor = self.cmb_proveedor.currentData()
        marca: Marca = self.cmb_marca.currentData()

        self.entity.nombre = self.input_nombre.text()
        self.entity.descripcion = self.txt_descripcion.toPlainText()
        self.entity.stock = self.dbl_stock.value()
        self.entity.precio_compra = self.dbl_precio_compra.value()
        self.entity.precio_venta = self.dbl_precio_venta.value()

        if (proveedor):
            self.entity.proveedor_id = proveedor.id

        if (marca):
            self.entity.marca_id = marca.id

        session.add(self.entity)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load()
            self.close()
        except Exception:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
