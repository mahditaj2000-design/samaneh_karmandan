from PySide6.QtWidgets import QWidget , QDialog , QMessageBox
from .ChangePass import Ui_Dialog
from services.API_client import change_password

class ChangePass(QDialog , Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("تغییر رمز عبور")

        self.pushButton.clicked.connect(self.change_the_pass)


    def change_the_pass(self):

        old_password = self.lineEdit.text()
        new_password = self.lineEdit_2.text()
        conf_password = self.lineEdit_3.text()

        if not old_password or not new_password or not conf_password:
            QMessageBox.warning(
                self,
                "عملیات ناموفق",
                "لطفاً همه فیلدها را پر کنید!"
            )
            return

        if old_password == new_password:
            QMessageBox.warning(
                self,
                "عملیات ناموفق",
                "رمز عبور جدید باید با رمز عبور قبلی متفاوت باشد!"
            )
            return

        if new_password != conf_password:
            QMessageBox.warning(
                self,
                "عملیات ناموفق",
                "رمز عبور جدید و تکرار آن یکسان نیست!"
            )
            return

        password_data = {
            "old_password": old_password,
            "new_password": new_password
        }

        result = change_password(password_data)

        if "Message" in result:
            QMessageBox.information(
                self,
                "عملیات موفق",
                result["Message"]
            )
            self.close()

        else:
            QMessageBox.warning(
                self,
                "عملیات ناموفق",
                result.get("detail", "خطایی رخ داد")
            )