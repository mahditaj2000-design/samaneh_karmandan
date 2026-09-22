# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from resources import back_ground_image_rc, adam_logo_image_rc


class Ui_login_page(object):
    def setupUi(self, login_page):
        if not login_page.objectName():
            login_page.setObjectName(u"login_page")
        login_page.resize(1200, 800)
        login_page.setMinimumSize(QSize(1200, 800))
        login_page.setMaximumSize(QSize(1200, 800))
        self.verticalLayout = QVBoxLayout(login_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_widget = QWidget(login_page)
        self.background_widget.setObjectName(u"background_widget")
        self.background_widget.setMinimumSize(QSize(1200, 800))
        self.background_widget.setMaximumSize(QSize(1200, 800))
        font = QFont()
        font.setBold(True)
        self.background_widget.setFont(font)
        self.background_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.background_widget.setStyleSheet(u"#background_widget {\n"
"    background-image: url(:/images/back.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.background_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(400, 0, 0, 6)
        self.login_card = QWidget(self.background_widget)
        self.login_card.setObjectName(u"login_card")
        self.login_card.setMinimumSize(QSize(400, 400))
        self.login_card.setMaximumSize(QSize(300, 300))
        self.login_card.setStyleSheet(u"#login_card {\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"    border-radius: 20px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.login_card)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(50, 50, 50, 50)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, 50)
        self.label = QLabel(self.login_card)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 120))
        self.label.setMaximumSize(QSize(90, 90))
        self.label.setStyleSheet(u"QLabel {\n"
"    border-radius: 40px;\n"
"    background-color: transparent;\n"
"}")
        self.label.setPixmap(QPixmap(u":/images/Adamak.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.username_lineedit = QLineEdit(self.login_card)
        self.username_lineedit.setObjectName(u"username_lineedit")
        self.username_lineedit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"    background-color: rgba(255,255,255,120);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #60A5FA;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3B82F6;\n"
"}")
        self.username_lineedit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.username_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.username_lineedit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.password_lineedit = QLineEdit(self.login_card)
        self.password_lineedit.setObjectName(u"password_lineedit")
        self.password_lineedit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.password_lineedit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"    background-color: rgba(255,255,255,120);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #60A5FA;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3B82F6;\n"
"}")
        self.password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.password_lineedit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.login_button = QPushButton(self.login_card)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setMinimumSize(QSize(40, 40))
        self.login_button.setMaximumSize(QSize(80, 80))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.login_button.setFont(font1)
        self.login_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.login_button.setAutoFillBackground(False)
        self.login_button.setStyleSheet(u"QPushButton#login_button {\n"
"    background-color: #3B82F6;\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton#login_button:hover {\n"
"    background-color: #2563EB;\n"
"}\n"
"\n"
"QPushButton#login_button:pressed {\n"
"    background-color: #1D4ED8;\n"
"}")
        self.login_button.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.login_button.setIconSize(QSize(16, 15))
        self.login_button.setAutoDefault(False)
        self.login_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.login_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.login_card)


        self.verticalLayout.addWidget(self.background_widget)


        self.retranslateUi(login_page)

        self.login_button.setDefault(False)


        QMetaObject.connectSlotsByName(login_page)
    # setupUi

    def retranslateUi(self, login_page):
        login_page.setWindowTitle(QCoreApplication.translate("login_page", u"Form", None))
        self.label.setText("")
        self.username_lineedit.setText("")
        self.username_lineedit.setPlaceholderText(QCoreApplication.translate("login_page", u"Username", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc"))
        self.password_lineedit.setText("")
        self.password_lineedit.setPlaceholderText(QCoreApplication.translate("login_page", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("login_page", u"LOGIN", None))
    # retranslateUi

