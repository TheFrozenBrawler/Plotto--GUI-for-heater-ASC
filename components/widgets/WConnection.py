from config.config import cfg

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel


# MAIN CONNECTION WIDGET
def WConnectionCreate():
    ConnectWidget = QWidget()
    ConnectWidget.setMaximumWidth(round(int(cfg['MAIN']['AppInitW'])/4/5*4))
    
    ConnectLayout = QVBoxLayout()
    ConnectLayout.addWidget(WConnectButton())
    ConnectLayout.addWidget(WConnectStatus())
    ConnectLayout.setContentsMargins(10,50,10,10)
    ConnectLayout.setSpacing(20)

    ConnectWidget.setLayout(ConnectLayout)

    return ConnectWidget

# CONNECT BUTTON
def WConnectButton():
    con_button = QPushButton("Connect")
    con_button.setIconSize(QSize(15, 15))
    con_button.setIcon(QIcon('components/icons/arrow.png'))
    
    con_button.clicked.connect(ConnectButton_clicked)

    return con_button

def ConnectButton_clicked():
    print("click")

#   CONNECT STATUS LABEL
def WConnectStatus():
    con_status_bar = QLabel("Device is not connected.")
    con_status_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

    return con_status_bar