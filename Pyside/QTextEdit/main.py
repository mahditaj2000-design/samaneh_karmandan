from PySide6.QtWidgets import QApplication
import sys
from QTextEdit import TextEdit

app = QApplication(sys.argv)

window = TextEdit()
window.setWindowTitle("متن نگاری")
window.show()

app.exec()