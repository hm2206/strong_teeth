from donttrust import DontTrust, Schema
from PyQt5.QtWidgets import QMessageBox


def login_validator(username: str, password: str) -> bool:
    trust = DontTrust(
        username=Schema().string().email(),
        password=Schema().string().min(6).max(24)
    )

    try:
        trust.validate(
            username=username,
            password=password
        )

        return True
    except Exception:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("Datos incorrectos")
        msg.exec_()
        return False
