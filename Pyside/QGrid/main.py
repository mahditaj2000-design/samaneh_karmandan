from QGridLayout import Grid
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

window = Grid()
window.setWindowTitle("گرید")
window.show()

app.exec()