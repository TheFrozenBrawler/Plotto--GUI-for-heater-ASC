from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QLabel

device_connected = False

# CONNECT BUTTON
def WConnectButton():
    con_button = QPushButton("Connect")
    con_button.setIconSize(QSize(15, 15))
    con_button.setIcon(QIcon('components/icons/arrow.png'))
    
    con_button.clicked.connect(ConnectButton_clicked)

    return con_button

def ConnectButton_clicked():
    print("click")


def WConnectStatus():
    con_status_bar = QLabel("Device is not connected.")
    con_status_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

    return con_status_bar