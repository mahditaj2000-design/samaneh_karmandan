from PySide6.QtWidgets import QApplication
import sys
from main_widget import MainWidget

app = QApplication(sys.argv)

Window = MainWidget()
Window.setWindowTitle("سامانه")
Window.show()

app.exec()