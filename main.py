import sys
from config.config import cfg

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from components.layout_create import MSetLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(cfg['MAIN']['AppTitle'])
        self.setMinimumSize(int(cfg['MAIN']['AppInitW']), int(cfg['MAIN']['AppInitH']))

        # set main layout
        MLayout = MSetLayout()
        MWidget = QWidget()
        MWidget.setLayout(MLayout)
        self.setCentralWidget(MWidget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()