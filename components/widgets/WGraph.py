from config.config import cfg
from PyQt6.QtCore import QTimer

import pyqtgraph as pg
from random import randint


def WGraph():
    WGraph_obj = WGraph_class()

    return WGraph_obj

class WGraph_class(pg.PlotWidget):
    def __init__(self):
        super(WGraph_class, self).__init__()

        self.TimeData = list(range(-59,1))
        self.TemperatureData = [0] * 60

        # graph settings
        self.setBackground("white")
        self.TemperaturePen = pg.mkPen(color="red")
        self.setTitle(str(cfg['WIDGETS']['GraphTitle']))
        styles = {"color": "black", "font-size": "15px"}
        self.setLabel("left", "Temperature (°C)", **styles)
        self.setLabel("bottom", "Time (s)", **styles)
        self.addLegend()
        self.showGrid(x=True, y=True)
        self.setYRange(20, 60)
        
        self.line = self.plot(
            self.TimeData,
            self.TemperatureData,
            name = "Temperature Sensor",
            pen = self.TemperaturePen,
        )

        # timer settings
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_data_slot)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        if 
            self.line.setData(self.TimeData, self.TemperatureData)

    def update_data_slot(self):
        self.TimeData = self.TimeData[1:]
        self.TimeData.append( self.TimeData[-1] + 1 )
        self.TemperatureData = self.TemperatureData[1:]
        self.TemperatureData.append( randint(20, 40) )
