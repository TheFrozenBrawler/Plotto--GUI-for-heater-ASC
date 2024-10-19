from config.config import cfg

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor

from components.widgets.WSetControllValues_widgetDefs import (WPlabel, WPset,
                                                              WIlabel, WIset,
                                                              WDlabel, WDset,
                                                              WTempLabel, WTempSet)

def WSetControlValues():
    WSetControlValues = QWidget()

    LSetControlValues = QHBoxLayout()
    LSetPIDValues = QVBoxLayout()

    # # P setting layout
    LSetP = QHBoxLayout()
    LSetP.addWidget(WPlabel())
    LSetP.addWidget(WPset())

    # # I setting layout
    LSetI = QHBoxLayout()
    LSetI.addWidget(WIlabel())
    LSetI.addWidget(WIset())

    # # D setting layout
    LSetD = QHBoxLayout()
    LSetD.addWidget(WDlabel())
    LSetD.addWidget(WDset())

    # # Add PID layouts
    LSetPIDValues.addLayout(LSetP)
    LSetPIDValues.addLayout(LSetI)
    LSetPIDValues.addLayout(LSetD)


    # # Temperature layout
    LSetTempValue = QVBoxLayout()
    LSetTempValue.addWidget(WTempLabel())
    LSetTempValue.addWidget(WTempSet())

    # # Add Control layouts
    LSetControlValues.addLayout(LSetPIDValues)
    LSetControlValues.addLayout(LSetTempValue)

    WSetControlValues.setLayout(LSetControlValues)

    ## remove below ###


    return WSetControlValues



# later move to create widget file
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)