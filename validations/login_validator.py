from donttrust import DontTrust, Schema
from PyQt5.QtWidgets import QMessageBox


def login_validator(username: str, password: str):
    trust = DontTrust(
        username=Schema().string().email(),
        password=Schema().string().min(6).max(24)
    )

    try:
        trust.validate(
            username=username,
            password=password
        )
    except Exception:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("Datos incorrectos")
        msg.exec_()
