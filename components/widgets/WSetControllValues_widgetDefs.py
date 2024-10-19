from config.config import cfg

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QDoubleSpinBox


# P setting widgets
def WPlabel():
    WPlabel = QLabel("Set P value")
    WPlabel.setAlignment(Qt.AlignmentFlag.AlignRight)
    return WPlabel

def WPset():
    WPset = QDoubleSpinBox()
    WPset.setValue(float(cfg['WIDGETS']['Pinit']))
    WPset.setMinimum(float(cfg['WIDGETS']['Pmin']))
    WPset.setMaximum(float(cfg['WIDGETS']['Pmax']))
    WPset.setSingleStep(0.1)
    return WPset

# I setting widgets
def WIlabel():
    WIlabel = QLabel("Set I value")
    WIlabel.setAlignment(Qt.AlignmentFlag.AlignRight)
    return WIlabel

def WIset():
    WIset = QDoubleSpinBox()
    WIset.setValue(float(cfg['WIDGETS']['Iinit']))
    WIset.setMinimum(float(cfg['WIDGETS']['Imin']))
    WIset.setMaximum(float(cfg['WIDGETS']['Imax']))
    WIset.setSingleStep(0.1)
    return WIset

# D setting widgets
def WDlabel():
    WDlabel = QLabel("Set D value")
    WDlabel.setAlignment(Qt.AlignmentFlag.AlignRight)
    return WDlabel

def WDset():
    WDset = QDoubleSpinBox()
    WDset.setValue(float(cfg['WIDGETS']['Dinit']))
    WDset.setMinimum(float(cfg['WIDGETS']['Dmin']))
    WDset.setMaximum(float(cfg['WIDGETS']['Dmax']))
    WDset.setSingleStep(0.1)
    return WDset


# temperature setting
def WTempLabel():
    WTempLabel = QLabel("Set temperature value")
    WTempLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return WTempLabel


def WTempSet():
    WTempSet = QDoubleSpinBox()
    WTempSet.setAlignment(Qt.AlignmentFlag.AlignTop)
    WTempSet.setValue(float(cfg['WIDGETS']['Tinit']))
    WTempSet.setMinimum(float(cfg['WIDGETS']['Tmin']))
    WTempSet.setMaximum(float(cfg['WIDGETS']['Tmax']))
    WTempSet.setSingleStep(0.1)
    return WTempSet