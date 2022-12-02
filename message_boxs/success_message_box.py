from PyQt5.QtWidgets import QMessageBox


class SuccessMessageBox(QMessageBox):

    def __init__(self, title="Informacion", text="Todo salio bien!!!"):
        super(SuccessMessageBox, self).__init__()
        self.setIcon(QMessageBox.Information)
        self.setWindowTitle(title)
        self.setText(text)
