from PySide6.QtWidgets import QApplication
import sys
from views.login.login import LoginPage
from views.main.main_window import MainWindow

app = QApplication(sys.argv)

login_window = LoginPage()

main_window = None

def show_main_window(username):

    global main_window

    main_window = MainWindow(username)
    main_window.show()

    login_window.close()
    

login_window.login_success.connect(show_main_window)


login_window.show()

app.exec()