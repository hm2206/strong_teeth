from PyQt5.QtWidgets import QMessageBox


class CriticalMessageBox(QMessageBox):

    def __init__(self, title="Error", text="Algo salió mal"):
        super(CriticalMessageBox, self).__init__()
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle(title)
        self.setText(text)
