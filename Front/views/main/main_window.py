from PySide6.QtWidgets import QWidget , QMainWindow , QApplication , QMessageBox
from .MainWindow import Ui_MainDashbord
from services.API_client import get_me , edit_my_prof , tedad_users_employees
from PySide6.QtCore import QTimer
from datetime import datetime
import jdatetime
from views.main.change_pass import ChangePass

days = {
    "Saturday": "شنبه",
    "Sunday": "یکشنبه",
    "Monday": "دوشنبه",
    "Tuesday": "سه‌شنبه",
    "Wednesday": "چهارشنبه",
    "Thursday": "پنجشنبه",
    "Friday": "جمعه"
}

months = {
    1: "فروردین",
    2: "اردیبهشت",
    3: "خرداد",
    4: "تیر",
    5: "مرداد",
    6: "شهریور",
    7: "مهر",
    8: "آبان",
    9: "آذر",
    10: "دی",
    11: "بهمن",
    12: "اسفند"
}

class MainWindow(QMainWindow , Ui_MainDashbord):
    def __init__(self , username):
        super().__init__()

        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)

        self.user_data = get_me()

        self.employee_data = self.user_data["res"]

        self.employee_name = self.employee_data[1]

        self.employee_familyname = self.employee_data[2]

        self.employee_email = self.employee_data[3]

        self.employee_mobile = self.employee_data[4]

        self.employee_username = username

        self.user_name.setText(self.employee_name)

        self.label_9.setText(
            f"{self.employee_name} {self.employee_familyname}"
        )

        self.lineEdit.setText(self.employee_name)

        self.lineEdit_2.setText(self.employee_familyname)

        self.lineEdit_3.setText(self.employee_mobile)

        self.lineEdit_4.setText(self.employee_email)

        self.label_16.setText(self.employee_username)

        self.exit_but.clicked.connect(self.exit_program)

        self.changes_but.clicked.connect(self.send_my_edit_data)

        self.btn_change_password.clicked.connect(self.open_change_pass)

        self.tedad = tedad_users_employees()

        self.tedad_employees = self.tedad["employees_count"]

        self.tedad_users = self.tedad["users_count"]

        self.label_3.setText(str(self.tedad_employees))

        self.label_6.setText(str(self.tedad_users))

    def open_change_pass(self):
        
        self.change_password = ChangePass()
        self.change_password.exec()

    def send_my_edit_data(self):

        name = self.lineEdit.text()
        familyname = self.lineEdit_2.text()
        email_address = self.lineEdit_4.text()
        mobile = self.lineEdit_3.text()

        new_data = {
            "name": name,
            "familyname": familyname,
            "email_address": email_address,
            "mobile": mobile
        }

        result = edit_my_prof(new_data)

        if "Message" in result:

            QMessageBox.information(
                self,
                "موفقیت",
                result["Message"]
            )

        else:

            QMessageBox.warning(
                self,
                "عملیات ناموفق",
                result.get("detail", "خطایی رخ داد")
            )
    

    def update_datetime(self):
        now = jdatetime.datetime.now()
        
        day_name = days[now.strftime("%A")]

        month_name = months[now.month]

        current_time = now.strftime("%H:%M")

        current_date = f"{day_name} {now.day} {month_name} {now.year}"

        self.clock_label.setText(current_time)
        self.date_label.setText(current_date)

    def exit_program(self):
        QApplication.quit()
