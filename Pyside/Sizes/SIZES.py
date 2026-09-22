from PySide6.QtWidgets import QWidget , QPushButton , QVBoxLayout , QHBoxLayout , QLineEdit , QLabel , QSizePolicy

class Size(QWidget):
    def __init__(self):
        super().__init__()

        some_label = QLabel(": لطفا چیزی بنویسید")
        some_box = QLineEdit()
        some_box.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Expanding)
        some_label.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Expanding)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        h_layout_label_box = QHBoxLayout()
        h_layout_buttons = QHBoxLayout()

        main_layout.addLayout(h_layout_label_box)
        main_layout.addLayout(h_layout_buttons)

        h_layout_label_box.addWidget(some_label , 1)
        h_layout_label_box.addWidget(some_box , 1)

        button1 = QPushButton("111")
        button2 = QPushButton("222")

        h_layout_buttons.addWidget(button1 , 1)
        h_layout_buttons.addWidget(button2 , 2)