from PySide6.QtWidgets import QApplication
import sys
from SIZES import Size

app = QApplication(sys.argv)

window = Size()
window.setWindowTitle("تنظیمات سایز ویجت")
window.show()

app.exec()