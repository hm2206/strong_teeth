# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hans/Documentos/eva/dental/ui/persona_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(751, 615)
        Frame.setLineWidth(0)
        self.vboxlayout = QtWidgets.QVBoxLayout(Frame)
        self.vboxlayout.setContentsMargins(40, 0, 0, 0)
        self.vboxlayout.setSpacing(10)
        self.vboxlayout.setObjectName("vboxlayout")
        self.frame = QtWidgets.QFrame(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(486, 30, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #cfd8dc;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.btn_plus = QtWidgets.QPushButton(self.frame)
        self.btn_plus.setGeometry(QtCore.QRect(0, 30, 31, 31))
        self.btn_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_plus.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/hans/Documentos/eva/dental/ui/../assets/images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_plus.setIcon(icon)
        self.btn_plus.setIconSize(QtCore.QSize(25, 25))
        self.btn_plus.setFlat(True)
        self.btn_plus.setObjectName("btn_plus")
        self.vboxlayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableWidget(self.frame_2)
        self.table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setStyleSheet("color: #cfd8dc;")
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(False)
        self.table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.table.setShowGrid(True)
        self.table.setGridStyle(QtCore.Qt.SolidLine)
        self.table.setCornerButtonEnabled(False)
        self.table.setRowCount(0)
        self.table.setColumnCount(7)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.horizontalHeader().setMinimumSectionSize(85)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(True)
        self.table.verticalHeader().setHighlightSections(True)
        self.table.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.table)
        self.vboxlayout.addWidget(self.frame_2)
        self.vboxlayout.setStretch(0, 1)
        self.vboxlayout.setStretch(1, 8)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Personas"))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "#ID"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Nombres"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Apellido Paterno"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "Apellido Materno"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "N° Identidad"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "F. Nacimiento"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "Género"))