from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize


def WOnOFF():
    # create layouts
    WOnOFF = QWidget()
    LOnOff = QVBoxLayout()
    LToggleHeating = QHBoxLayout()
    LTogglePlotting = QHBoxLayout()

    # add widgets to layouts
    WHeatButton_obj = WHeatButton_class()
    LToggleHeating.addWidget(WHeatButton_obj)
    LToggleHeating.addWidget(WHeatLabel())

    WPlotButton_obj = WPlotButton_class()
    LTogglePlotting.addWidget(WPlotButton_obj)
    LTogglePlotting.addWidget(WPlotLabel())

    # nest layouts
    LOnOff.addLayout(LToggleHeating)
    LOnOff.addLayout(LTogglePlotting)
    WOnOFF.setLayout(LOnOff)

    return WOnOFF


# TURN ON HEATING BUTTON
class WHeatButton_class(QPushButton):
    def __init__(self):
        super(WHeatButton_class, self).__init__()
        SButtonSize = QSize(20, 20)
        self.setFixedSize(SButtonSize)
        self.setIcon(QIcon('components/icons/tick-button.png'))
        self.setIconSize(SButtonSize)
        self.setCheckable(True)
        self.setChecked(True)
        self.toggled.connect(self.HeatButton_toggled)

    def HeatButton_toggled(self, check):
        if (check):
            self.setIcon(QIcon('components/icons/tick-button.png'))
            # turn heating on
        else:
            self.setIcon(QIcon('components/icons/cross-button.png'))
            # turn heating off

def WHeatLabel():
    WHeatLabel = QLabel("Toggle heating")
    return WHeatLabel


# TURN ON PLOTTING BUTTON
class WPlotButton_class(QPushButton):
    def __init__(self):
        super(WPlotButton_class, self).__init__()
        SButtonSize = QSize(20, 20)
        self.setFixedSize(SButtonSize)
        self.setIcon(QIcon('components/icons/tick-button.png'))
        self.setIconSize(SButtonSize)
        self.setCheckable(True)
        self.setChecked(True)
        self.toggled.connect(self.PlotButton_toggled)

    def PlotButton_toggled(self, check):
        if (check):
            self.setIcon(QIcon('components/icons/tick-button.png'))
            # turn ploting on
        else:
            self.setIcon(QIcon('components/icons/cross-button.png'))
            # turn ploting off

def WPlotLabel():
    WPlotLabel = QLabel("Toggle plotting")
    return WPlotLabel