from PySide6.QtCore import (QCoreApplication,QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QVBoxLayout)

class Ui_Main_Widget(object):
    def setupUi(self, Main_Widget):
        if not Main_Widget.objectName():
            Main_Widget.setObjectName(u"Main_Widget")
        Main_Widget.resize(325, 102)
        self.verticalLayout = QVBoxLayout(Main_Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.username_label = QLabel(Main_Widget)
        self.username_label.setObjectName(u"username_label")

        self.horizontalLayout.addWidget(self.username_label)

        self.username_line = QLineEdit(Main_Widget)
        self.username_line.setObjectName(u"username_line")

        self.horizontalLayout.addWidget(self.username_line)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.password_label = QLabel(Main_Widget)
        self.password_label.setObjectName(u"password_label")

        self.horizontalLayout_2.addWidget(self.password_label)

        self.password_line = QLineEdit(Main_Widget)
        self.password_line.setObjectName(u"password_line")

        self.horizontalLayout_2.addWidget(self.password_line)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.enter_butt = QPushButton(Main_Widget)
        self.enter_butt.setObjectName(u"enter_butt")

        self.verticalLayout.addWidget(self.enter_butt)


        self.retranslateUi(Main_Widget)

        QMetaObject.connectSlotsByName(Main_Widget)
    # setupUi

    def retranslateUi(self, Main_Widget):
        Main_Widget.setWindowTitle(QCoreApplication.translate("Main_Widget", u"Form", None))
        self.username_label.setText(QCoreApplication.translate("Main_Widget", u"username", None))
        self.password_label.setText(QCoreApplication.translate("Main_Widget", u"password", None))
        self.enter_butt.setText(QCoreApplication.translate("Main_Widget", u"\u0648\u0631\u0648\u062f", None))
    # retranslateUi

