from PySide6.QtWidgets import QTextEdit , QWidget , QVBoxLayout , QPushButton , QHBoxLayout , QApplication

class TextEdit(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()

        self.text_edit = QTextEdit()

        self.setLayout(main_layout)

        main_layout.addLayout(buttons_layout)

        copy_button = QPushButton("کپی")
        paste_button = QPushButton("چسباندن")
        undo_button = QPushButton("قبلی")
        redo_button = QPushButton("بعدی")
        quit_button = QPushButton("خروج")
        clear_button = QPushButton("پاک کردن همه")
        

        buttons_layout.addWidget(copy_button)
        buttons_layout.addWidget(paste_button)
        buttons_layout.addWidget(undo_button)
        buttons_layout.addWidget(redo_button)
        buttons_layout.addWidget(clear_button)
        buttons_layout.addWidget(quit_button)


        main_layout.addWidget(self.text_edit)


        copy_button.clicked.connect(self.text_edit.copy)
        paste_button.clicked.connect(self.text_edit.paste)
        undo_button.clicked.connect(self.text_edit.undo)
        redo_button.clicked.connect(self.text_edit.redo)
        quit_button.clicked.connect(QApplication.quit)
        clear_button.clicked.connect(self.text_edit.clear)

        copy_button.clicked.connect(self.copyed_text)

    def copyed_text (self):
        copyed = self.text_edit.textCursor().selectedText()
        print(copyed)


