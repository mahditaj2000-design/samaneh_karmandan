from PySide6.QtWidgets import QWidget
from Widget import Ui_Main_Widget

class MainWidget(QWidget , Ui_Main_Widget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.enter_butt