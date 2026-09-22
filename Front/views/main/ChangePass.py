# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangePass.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(500, 400))
        Dialog.setMaximumSize(QSize(500, 400))
        Dialog.setStyleSheet(u"QDialog {\n"
"    background-color: #080B12;\n"
"    border-radius: 20px;\n"
"}")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(181, 114, 150, 40))
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(150, 27))
        self.lineEdit.setMaximumSize(QSize(150, 40))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(40, 120, 220, 70);\n"
"    border: 1px solid rgba(80, 170, 255, 160);\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-size: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #4DA6FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
"    background-color: rgba(40, 120, 220, 100);\n"
"}")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(181, 164, 150, 40))
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(150, 31))
        self.lineEdit_2.setMaximumSize(QSize(133, 40))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(40, 120, 220, 70);\n"
"    border: 1px solid rgba(80, 170, 255, 160);\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-size: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #4DA6FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
"    background-color: rgba(40, 120, 220, 100);\n"
"}")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(181, 214, 150, 40))
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QSize(150, 31))
        self.lineEdit_3.setMaximumSize(QSize(133, 40))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(40, 120, 220, 70);\n"
"    border: 1px solid rgba(80, 170, 255, 160);\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-size: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #4DA6FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;\n"
"    background-color: rgba(40, 120, 220, 100);\n"
"}")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(217, 280, 75, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(220, 40, 40, 120);\n"
"    border: 1px solid rgba(255, 80, 80, 180);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    padding: 8px 20px;\n"
"    font-size: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 50, 50, 170);\n"
"    border: 1px solid rgba(255, 120, 120, 220);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(180, 20, 20, 200);\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 30, 51, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631 \u0642\u0628\u0644\u06cc", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631 \u062c\u062f\u06cc\u062f", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Dialog", u"\u062a\u06a9\u0631\u0627\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631 \u062c\u062f\u06cc\u062f", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u062a\u0627\u06cc\u06cc\u062f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

