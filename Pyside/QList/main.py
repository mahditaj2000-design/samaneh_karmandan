from PySide6.QtWidgets import QApplication
from QListWidget import List
import sys

app = QApplication(sys.argv)

window = List()
window.setWindowTitle("لیست")
window.show()

app.exec()