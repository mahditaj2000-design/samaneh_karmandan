from PySide6.QtWidgets import QWidget , QPushButton , QLabel , QVBoxLayout
from PySide6.QtGui import QPixmap

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.image_label = QLabel()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(self.image_label)

        self.image_label.setPixmap(QPixmap(r"C:\Users\am.shayesteh\OneDrive\Desktop\samaneh_karmandan\assets\back.png"))
