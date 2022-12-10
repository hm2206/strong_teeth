from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QPushButton, QFrame, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from configs.db import session
from models.producto import Producto


class ProductoFrame(QFrame):

    table: QTableWidget
    btn_plus: QPushButton

    def __init__(self, app: App, parent=None):
        super(ProductoFrame, self).__init__(parent=parent)
        uic.loadUi("ui/producto_frame.ui", self)
        self._app = app

        self.btn_plus.clicked.connect(self.action_create)
        self.table.doubleClicked.connect(self.action_edit)

    def showEvent(self, evt: QShowEvent):
        self.load()
        return super().showEvent(evt)

    def action_create(self, evt: QEvent):
        from dialogs.producto_dialog import ProductoDialog
        self._app.app_screen.set_enabled_window(False)
        self.msg = ProductoDialog(self._app, self, title="Crear Producto")
        self.msg.show()

    def action_edit(self, evt: QEvent):
        from dialogs.producto_dialog import ProductoDialog
        self._app.app_screen.set_enabled_window(False)
        row = self.table.selectionModel().currentIndex().row()
        id = self.table.item(row, 0).text()
        producto = session.query(Producto).get(id)
        self.msg = ProductoDialog(self._app, self, title="Editar Producto")
        self.msg.show()
        self.msg.load(producto)

    def load(self):
        self.data = session.query(Producto).all()
        self.table.setRowCount(self.data.__len__())
        for index, item in enumerate(self.data):
            producto: Producto = item
            self.table.setItem(index, 0, QTableWidgetItem(str(producto.id)))
            self.table.setItem(
                index, 1, QTableWidgetItem(str(producto.nombre)))
            self.table.setItem(
                index, 2, QTableWidgetItem(str(producto.descripcion)))
            self.table.setItem(
                index, 3, QTableWidgetItem(str(producto.stock)))
            self.table.setItem(
                index, 4, QTableWidgetItem(str(producto.precio_compra)))
            self.table.setItem(index, 5, QTableWidgetItem(
                str(producto.precio_venta)))
            self.table.setItem(index, 6, QTableWidgetItem(
                str(producto.marca.nombre)))
            self.table.setItem(index, 7, QTableWidgetItem(
                str(producto.proveedor.razon_social)))
            self.table.resizeColumnsToContents()
