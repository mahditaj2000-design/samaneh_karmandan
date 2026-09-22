from PySide6.QtWidgets import QApplication
from QTabs import Main
import sys

app = QApplication(sys.argv)

window = Main()
window.setWindowTitle("سامانه")
window.show()

app.exec()