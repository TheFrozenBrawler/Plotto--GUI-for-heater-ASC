from config.config import cfg

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout

# later move to create widget file
from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPalette, QColor

from components.widgets.WConnection import WConnectionCreate
from components.widgets.WSetControlValues import WSetControlValues

def MSetLayout():
    MLayout = QVBoxLayout()
    GraphWidget = QLabel("Graph")
    GraphWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
    GraphWidget.setMinimumSize( int(cfg['MAIN']['AppInitW']), round(int(cfg['MAIN']['AppInitH'])/3*2) )

    SettingsLayout = QHBoxLayout()
    
    MLayout.addWidget(GraphWidget)
    MLayout.addLayout(SettingsLayout)

    # Create connection widget
    SettingsLayout.addWidget(WConnectionCreate())

    # Create Set PID widgets
    SettingsLayout.addWidget(WSetControlValues())

    SettingsLayout.addWidget(Color('red'))
    SettingsLayout.addWidget(Color('blue'))

    return MLayout


# later move to create widget file
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)