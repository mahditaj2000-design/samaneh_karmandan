from PySide6.QtWidgets import QWidget , QListWidget , QVBoxLayout ,QAbstractItemView , QPushButton , QHBoxLayout , QLineEdit

class List(QWidget):
    def __init__(self):
        super().__init__()

        list = QListWidget()
        main_layout = QVBoxLayout()

        self.setLayout(main_layout)

        list.setSelectionMode(QAbstractItemView.MultiSelection)

        main_layout.addWidget(list)

        list.addItems(["علی" , "حسن" , "حسین"])

        add_button = QPushButton("اضافه کردن")
        h_layout = QHBoxLayout()
        main_layout.addLayout(h_layout)

        h_layout.addWidget(add_button)

        add_line = QLineEdit()

        h_layout.addWidget(add_line)

        def add():
            text = add_line.text()
            list.addItem(text)

        add_button.clicked.connect(add)

        rem_button = QPushButton("پاک کردن")

        h_layout2 = QHBoxLayout()
        main_layout.addLayout(h_layout2)

        h_layout2.addWidget(rem_button)

        def rem():
            for item in list.selectedItems():
                list.takeItem(list.row(item))

        rem_button.clicked.connect(rem)


            




