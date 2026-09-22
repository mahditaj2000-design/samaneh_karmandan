from PySide6.QtWidgets import QWidget , QVBoxLayout , QHBoxLayout , QTabWidget , QComboBox , QPushButton

class Main(QWidget):
    def __init__(self):
        super().__init__()

        main_lay = QVBoxLayout()
        self.setLayout(main_lay)

        tabs = QTabWidget()
        main_lay.addWidget(tabs)

        employee_tab = QWidget()
        user_tab =QWidget()

        tabs.addTab(employee_tab , "کارمندان")
        tabs.addTab(user_tab , "کاربران")

        employee_tab_ley = QVBoxLayout()
        user_tab_lay = QVBoxLayout()

        employee_tab.setLayout(employee_tab_ley)
        user_tab.setLayout(user_tab_lay)

        button_emp = QPushButton("کارمند")
        button_usr = QPushButton("کاربر")

        employee_tab_ley.addWidget(button_emp)
        user_tab_lay.addWidget(button_usr)

        role1 = QComboBox()
        role2 = QComboBox()

        role1.addItems(["کاربر1" , "کاربر12" , "کاربر13" , "کاربر14"])
        role2.addItems(["dsfdf" , "vsdfvfd" , "nhgn" , "jhmhj"])

        employee_tab_ley.addWidget(role1)
        user_tab_lay.addWidget(role2)
