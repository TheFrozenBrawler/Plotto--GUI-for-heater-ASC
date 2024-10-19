import sys
from config.config import cfg

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from components.MLayoutCreate import MSetLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(cfg['MAIN']['AppTitle'])
        self.setFixedSize(int(cfg['MAIN']['AppInitW']), int(cfg['MAIN']['AppInitH']))
        
        # set main layout
        MWidget = QWidget()
        MWidget.setLayout(MSetLayout())
        self.setCentralWidget(MWidget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()