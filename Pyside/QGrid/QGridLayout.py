from PySide6.QtWidgets import QWidget , QPushButton , QLabel , QLineEdit , QGridLayout , QVBoxLayout , QApplication

class Grid(QWidget):
    def __init__(self):
        super().__init__()

        main_lay = QVBoxLayout()

        g_lay = QGridLayout()
        self.setLayout(main_lay)
        main_lay.addLayout(g_lay)

        name_label = QLabel(" :نام")
        family_label = QLabel(" :نام خانوادگی")
        age = QLabel(" :سن")
        phone_label = QLabel(" :شماره تلفن")

        n_line = QLineEdit()
        f_line = QLineEdit()
        a_line = QLineEdit()
        p_line = QLineEdit()

        g_lay.addWidget(name_label , 0 , 0)
        g_lay.addWidget(n_line , 0 , 1)
        g_lay.addWidget(family_label , 0 , 2)
        g_lay.addWidget(f_line , 0 , 3)
        g_lay.addWidget(age , 1 , 0)
        g_lay.addWidget(a_line , 1 , 1)
        g_lay.addWidget(phone_label , 1 , 2)
        g_lay.addWidget(p_line , 1 , 3)

        button = QPushButton("خروج")
        button.clicked.connect(QApplication.quit)
        main_lay.addWidget(button)
