from PySide6.QtWidgets import QApplication
import sys
from labelandimage import Widget

app = QApplication(sys.argv)

window = Widget()
window.setWindowTitle("لیبل و عکس")
window.show()

app.exec()