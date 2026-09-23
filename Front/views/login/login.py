from PySide6.QtWidgets import QWidget , QMessageBox
from .LoginPage import Ui_login_page
from services.API_client import login , get_me
from PySide6.QtCore import Signal

class LoginPage(QWidget , Ui_login_page):

    login_success = Signal(str)                 #در صورت موفق بودن لاگین یک سیگنال برای مین فرستاده می شود 

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.login_button.clicked.connect(self.handel_login)

    def handel_login(self):

        username = self.username_lineedit.text()
        password = self.password_lineedit.text()

        result = login(username, password)

        if "access_token" in result:

            self.login_success.emit(username)

        else:

            QMessageBox.warning(
                self,
                "ورود ناموفق",
                result.get("detail", "خطایی در ورود رخ داد")
            )

