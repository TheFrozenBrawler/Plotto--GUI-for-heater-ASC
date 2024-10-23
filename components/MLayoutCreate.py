from config.config import cfg

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout

# later move to create widget file
from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPalette, QColor

from components.widgets.WGraph import WGraph
from components.widgets.WConnection import WConnection
from components.widgets.WSetControlValues import WSetControlValues
from components.widgets.WOnOff import WOnOFF

def MSetLayout():
    MLayout = QVBoxLayout()

    SettingsLayout = QHBoxLayout()
    
    # Create graph widget
    MLayout.addWidget(WGraph())

    MLayout.addLayout(SettingsLayout)

    # Create connection widget
    SettingsLayout.addWidget(WConnection())

    # Create Set PID widget
    SettingsLayout.addWidget(WSetControlValues())

    # Create ON/OFF widget
    SettingsLayout.addWidget(WOnOFF())

    # SettingsLayout.addWidget(Color('blue'))

    return MLayout


# later move to create widget file
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)