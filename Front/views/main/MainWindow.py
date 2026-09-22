# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
from resources import (
    main_window_back_rc,
    lock_image_rc,
    adam_abi_rc,
    exit_logo_main_rc,
    reports_logo_main_rc,
    user_logo_main_rc,
    search_logo_main_rc,
    employees_logo_main_rc,
    home_icon_rc,
    adam_logo_main_rc
)

class Ui_MainDashbord(object):
    def setupUi(self, MainDashbord):
        if not MainDashbord.objectName():
            MainDashbord.setObjectName(u"MainDashbord")
        MainDashbord.resize(1280, 893)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainDashbord.sizePolicy().hasHeightForWidth())
        MainDashbord.setSizePolicy(sizePolicy)
        MainDashbord.setMinimumSize(QSize(1280, 850))
        MainDashbord.setMaximumSize(QSize(1280, 893))
        MainDashbord.setStyleSheet(u"\n"
"QWidget#centralwidget {\n"
"    background-image: url(:/images/main_window_background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        MainDashbord.setAnimated(True)
        MainDashbord.setDocumentMode(False)
        MainDashbord.setDockNestingEnabled(False)
        MainDashbord.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainDashbord)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1280, 850))
        self.centralwidget.setMaximumSize(QSize(1280, 850))
        self.centralwidget.setStyleSheet(u"\n"
"QWidget#centralwidget {\n"
"    background-image: url(:/images/main_window_background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.horizontalLayout_main = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        self.stackedWidget_main = QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget_main.sizePolicy().hasHeightForWidth())
        self.stackedWidget_main.setSizePolicy(sizePolicy1)
        self.stackedWidget_main.setStyleSheet(u"QWidget#stackedWidget_main {\n"
"    background-color: rgba(255, 255, 255, 35);\n"
"    border: 1px solid rgba(255, 255, 255, 90);\n"
"    border-radius: 28px;\n"
"}")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.title_dash_widget = QWidget(self.dashboard_page)
        self.title_dash_widget.setObjectName(u"title_dash_widget")
        self.title_dash_widget.setGeometry(QRect(10, 30, 990, 130))
        sizePolicy.setHeightForWidth(self.title_dash_widget.sizePolicy().hasHeightForWidth())
        self.title_dash_widget.setSizePolicy(sizePolicy)
        self.title_dash_widget.setMinimumSize(QSize(990, 130))
        self.title_dash_widget.setMaximumSize(QSize(990, 130))
        self.title_dash_widget.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    border: 1px solid rgba(255, 255, 255, 110);\n"
"    border-radius: 28px;\n"
"}")
        self.horizontalLayoutWidget_2 = QWidget(self.title_dash_widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 972, 92))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.date_layout = QHBoxLayout()
        self.date_layout.setObjectName(u"date_layout")
        self.clock_label = QLabel(self.horizontalLayoutWidget_2)
        self.clock_label.setObjectName(u"clock_label")
        self.clock_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}")
        self.clock_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.date_layout.addWidget(self.clock_label)

        self.horizontalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.date_layout.addItem(self.horizontalSpacer)

        self.line_3 = QFrame(self.horizontalLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.date_layout.addWidget(self.line_3)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.date_layout.addItem(self.horizontalSpacer_2)

        self.date_label = QLabel(self.horizontalLayoutWidget_2)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")

        self.date_layout.addWidget(self.date_label)


        self.horizontalLayout_2.addLayout(self.date_layout)

        self.horizontalSpacer_3 = QSpacerItem(300, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.right_title_dash = QVBoxLayout()
        self.right_title_dash.setObjectName(u"right_title_dash")
        self.right_title_dash.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.modiriat_label = QLabel(self.horizontalLayoutWidget_2)
        self.modiriat_label.setObjectName(u"modiriat_label")
        sizePolicy.setHeightForWidth(self.modiriat_label.sizePolicy().hasHeightForWidth())
        self.modiriat_label.setSizePolicy(sizePolicy)
        self.modiriat_label.setMaximumSize(QSize(220, 100))
        self.modiriat_label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.modiriat_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 19px;\n"
"    font-weight: bold;\n"
"}")
        self.modiriat_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.right_title_dash.addWidget(self.modiriat_label)

        self.Modiriat_discrip_label = QLabel(self.horizontalLayoutWidget_2)
        self.Modiriat_discrip_label.setObjectName(u"Modiriat_discrip_label")
        sizePolicy.setHeightForWidth(self.Modiriat_discrip_label.sizePolicy().hasHeightForWidth())
        self.Modiriat_discrip_label.setSizePolicy(sizePolicy)
        self.Modiriat_discrip_label.setMaximumSize(QSize(300, 200))
        self.Modiriat_discrip_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}")
        self.Modiriat_discrip_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.right_title_dash.addWidget(self.Modiriat_discrip_label)


        self.horizontalLayout_2.addLayout(self.right_title_dash)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/images/c060a5ea-0698-4df2-bf98-bf5b92f713d1.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalLayoutWidget_3 = QWidget(self.dashboard_page)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 180, 981, 111))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.users_widget = QWidget(self.horizontalLayoutWidget_3)
        self.users_widget.setObjectName(u"users_widget")
        self.users_widget.setStyleSheet(u"QWidget#users_widget {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    border: 1px solid rgba(255, 255, 255, 110);\n"
"    border-radius: 28px;\n"
"}")
        self.label_5 = QLabel(self.users_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 10, 119, 40))
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}")
        self.label_6 = QLabel(self.users_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(360, 50, 42, 46))
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 19px;\n"
"    font-weight: bold;\n"
"}")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.users_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 20, 71, 71))
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(71, 71))
        self.label_7.setMaximumSize(QSize(71, 71))
        self.label_7.setStyleSheet(u"QLabel{\n"
"    border-image: url(:/images/9da65888-5452-42cc-99a5-c43c5d1c1e25.png);\n"
"    border-radius: 40px;\n"
"}")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_3.addWidget(self.users_widget)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.karmandan_widget = QWidget(self.horizontalLayoutWidget_3)
        self.karmandan_widget.setObjectName(u"karmandan_widget")
        self.karmandan_widget.setStyleSheet(u"QWidget#karmandan_widget {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    border: 1px solid rgba(255, 255, 255, 110);\n"
"    border-radius: 28px;\n"
"}")
        self.label_2 = QLabel(self.karmandan_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 10, 119, 40))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}")
        self.label_3 = QLabel(self.karmandan_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 50, 42, 46))
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 19px;\n"
"    font-weight: bold;\n"
"}")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.karmandan_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 20, 71, 71))
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(71, 71))
        self.label_4.setMaximumSize(QSize(71, 71))
        self.label_4.setStyleSheet(u"QLabel{\n"
"    border-image: url(:/images/b2e30a1c-78b2-484d-9e76-eeb775bf3efe.png);\n"
"    border-radius: 40px;\n"
"}")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_3.addWidget(self.karmandan_widget)

        self.portabel_widget = QWidget(self.dashboard_page)
        self.portabel_widget.setObjectName(u"portabel_widget")
        self.portabel_widget.setEnabled(True)
        self.portabel_widget.setGeometry(QRect(20, 310, 961, 461))
        self.portabel_widget.setStyleSheet(u"QWidget#portabel_widget {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    border: 1px solid rgba(255, 255, 255, 110);\n"
"    border-radius: 28px;\n"
"}")
        self.name_widget = QWidget(self.portabel_widget)
        self.name_widget.setObjectName(u"name_widget")
        self.name_widget.setGeometry(QRect(30, 50, 271, 351))
        self.name_widget.setStyleSheet(u"QWidget#name_widget {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    border: 1px solid rgba(255, 255, 255, 110);\n"
"    border-radius: 28px;\n"
"}")
        self.username_widget = QWidget(self.name_widget)
        self.username_widget.setObjectName(u"username_widget")
        self.username_widget.setGeometry(QRect(20, 200, 231, 61))
        self.username_widget.setStyleSheet(u"QWidget#username_widget {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    border: 1px solid rgba(255, 255, 255, 110);\n"
"    border-radius: 28px;\n"
"}")
        self.label_17 = QLabel(self.username_widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 10, 41, 41))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    border-image: url(:/images/c1bb0dc2-6c77-4b23-a630-8768d3a59f12.png);\n"
"    border-radius: 40px;\n"
"}")
        self.layoutWidget_3 = QWidget(self.username_widget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(70, 10, 157, 42))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.layoutWidget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.label_8 = QLabel(self.layoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.name_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 130, 250, 60))
        self.label_9.setMinimumSize(QSize(250, 60))
        self.label_9.setMaximumSize(QSize(250, 60))
        self.label_9.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 19px;\n"
"    font-weight: bold;\n"
"}")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_label_2 = QLabel(self.name_widget)
        self.logo_label_2.setObjectName(u"logo_label_2")
        self.logo_label_2.setGeometry(QRect(80, 20, 110, 110))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logo_label_2.sizePolicy().hasHeightForWidth())
        self.logo_label_2.setSizePolicy(sizePolicy2)
        self.logo_label_2.setMinimumSize(QSize(110, 110))
        self.logo_label_2.setMaximumSize(QSize(110, 110))
        self.logo_label_2.setStyleSheet(u"QLabel{\n"
"    border-image: url(:/images/Adamak_main.png);\n"
"    border-radius: 40px;\n"
"}")
        self.logo_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.changes_but = QPushButton(self.name_widget)
        self.changes_but.setObjectName(u"changes_but")
        self.changes_but.setEnabled(True)
        self.changes_but.setGeometry(QRect(70, 280, 121, 41))
        self.changes_but.setStyleSheet(u"QPushButton#changes_but {\n"
"    border-radius: 15px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \u062d\u0627\u0644\u062a \u063a\u06cc\u0631\u0641\u0639\u0627\u0644 */\n"
"QPushButton#changes_but:disabled {\n"
"    background-color: rgba(120,120,120,120);\n"
"    color: rgba(255,255,255,170);\n"
"    border: 1px solid rgba(255,255,255,80);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"/* \u062d\u0627\u0644\u062a \u0641\u0639\u0627\u0644 */\n"
"QPushButton#changes_but:enabled {\n"
"    background-color: rgba(40,130,255,170);\n"
"    color: white;\n"
"    border: 1px solid rgba(150,210,255,180);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"/* \u0647\u0627\u0648\u0631 */\n"
"QPushButton#changes_but:enabled:hover {\n"
"    background-color: rgba(40,130,255,220);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"/* \u06a9\u0644\u06cc\u06a9 */\n"
"QPushButton#changes_but:enabled:pressed {\n"
"    background-color: rgba(20,90,220,220);\n"
"    border-radius: 15px;\n"
"}")
        self.info_widget = QWidget(self.portabel_widget)
        self.info_widget.setObjectName(u"info_widget")
        self.info_widget.setGeometry(QRect(350, 50, 581, 381))
        self.info_widget.setStyleSheet(u"QWidget#info_widget {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    border: 1px solid rgba(255, 255, 255, 110);\n"
"    border-radius: 28px;\n"
"}")
        self.passchanger_widget = QWidget(self.info_widget)
        self.passchanger_widget.setObjectName(u"passchanger_widget")
        self.passchanger_widget.setGeometry(QRect(20, 260, 541, 91))
        self.passchanger_widget.setStyleSheet(u"QWidget#passchanger_widget {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    border: 1px solid rgba(255, 255, 255, 110);\n"
"    border-radius: 28px;\n"
"}")
        self.layoutWidget_4 = QWidget(self.passchanger_widget)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(43, 10, 471, 61))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel {\n"
"    border-image: url(:/images/5cbcbe07-a8d4-4510-a98b-a5757c3c89dd.png);\n"
"    border-radius: 40px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.label_14 = QLabel(self.layoutWidget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel {\n"
"    color: #64748B;\n"
"}")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_14)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.btn_change_password = QPushButton(self.layoutWidget_4)
        self.btn_change_password.setObjectName(u"btn_change_password")
        self.btn_change_password.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_change_password.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    color: #1E293B;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    border-radius: 14px;\n"
"    padding: 10px 18px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btn_change_password:hover {\n"
"    background-color: rgba(255, 255, 255, 70);\n"
"    border: 1px solid rgba(255, 120, 120, 160);\n"
"}\n"
"\n"
"QPushButton#btn_change_password:pressed {\n"
"    background-color: rgba(255, 100, 100, 80);\n"
"    border: 1px solid rgba(255, 140, 140, 200);\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_change_password)

        self.layoutWidget_5 = QWidget(self.info_widget)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(80, 20, 461, 39))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(True)
        self.label_11.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.horizontalSpacer_8 = QSpacerItem(210, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.label_10 = QLabel(self.layoutWidget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.layoutWidget_6 = QWidget(self.info_widget)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(120, 130, 405, 39))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.horizontalSpacer_9 = QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.label_12 = QLabel(self.layoutWidget_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2a005b;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.layoutWidget_1 = QWidget(self.info_widget)
        self.layoutWidget_1.setObjectName(u"layoutWidget_1")
        self.layoutWidget_1.setGeometry(QRect(0, 170, 561, 43))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.layoutWidget_1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QSize(0, 0))
        self.lineEdit_4.setMaximumSize(QSize(190, 16777215))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    color: #1E293B;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    border-radius: 12px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(255, 255, 255, 70);\n"
"    border: 1px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgba(255, 255, 255, 90);\n"
"    border: 1px solid rgba(80, 160, 255, 180);\n"
"}")

        self.horizontalLayout_7.addWidget(self.lineEdit_4)

        self.horizontalSpacer_10 = QSpacerItem(180, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.lineEdit_3 = QLineEdit(self.layoutWidget_1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    color: #1E293B;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    border-radius: 12px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(255, 255, 255, 70);\n"
"    border: 1px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgba(255, 255, 255, 90);\n"
"    border: 1px solid rgba(80, 160, 255, 180);\n"
"}")
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lineEdit_3)

        self.layoutWidget_2 = QWidget(self.info_widget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 60, 521, 43))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    color: #1E293B;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    border-radius: 12px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(255, 255, 255, 70);\n"
"    border: 1px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgba(255, 255, 255, 90);\n"
"    border: 1px solid rgba(80, 160, 255, 180);\n"
"}")

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.horizontalSpacer_11 = QSpacerItem(145, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.lineEdit = QLineEdit(self.layoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    color: #1E293B;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    border-radius: 12px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(255, 255, 255, 70);\n"
"    border: 1px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgba(255, 255, 255, 90);\n"
"    border: 1px solid rgba(80, 160, 255, 180);\n"
"}")

        self.horizontalLayout_8.addWidget(self.lineEdit)

        self.stackedWidget_main.addWidget(self.dashboard_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_main.addWidget(self.page_2)

        self.horizontalLayout_main.addWidget(self.stackedWidget_main)

        self.sidebar_widget = QWidget(self.centralwidget)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sidebar_widget.sizePolicy().hasHeightForWidth())
        self.sidebar_widget.setSizePolicy(sizePolicy3)
        self.sidebar_widget.setMinimumSize(QSize(250, 0))
        self.sidebar_widget.setMaximumSize(QSize(250, 16777215))
        self.sidebar_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.sidebar_widget.setStyleSheet(u"QWidget#sidebar_widget {\n"
"    background-color: rgba(255, 255, 255, 45);\n"
"    border: 1px solid rgba(255, 255, 255, 110);\n"
"    border-radius: 28px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_label = QLabel(self.sidebar_widget)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy2.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy2)
        self.logo_label.setMaximumSize(QSize(90, 90))
        self.logo_label.setStyleSheet(u"QLabel#logo_label {\n"
"    border-image: url(:/images/Adamak_main.png);\n"
"    border-radius: 40px;\n"
"}")
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.logo_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.user_name = QLabel(self.sidebar_widget)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setMaximumSize(QSize(16777215, 50))
        self.user_name.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 80, 80, 70);\n"
"    border: 1px solid rgba(255, 120, 120, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(220, 60, 60, 100);\n"
"    border: 1px solid rgba(255, 100, 100, 130);\n"
"}")
        self.user_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.user_name)

        self.line_2 = QFrame(self.sidebar_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.verticalSpacer = QSpacerItem(0, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.dashbord_but = QPushButton(self.sidebar_widget)
        self.dashbord_but.setObjectName(u"dashbord_but")
        sizePolicy.setHeightForWidth(self.dashbord_but.sizePolicy().hasHeightForWidth())
        self.dashbord_but.setSizePolicy(sizePolicy)
        self.dashbord_but.setMaximumSize(QSize(300, 60))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.dashbord_but.setFont(font)
        self.dashbord_but.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.dashbord_but.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 19px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/c060a5ea-0698-4df2-bf98-bf5b92f713d1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashbord_but.setIcon(icon)
        self.dashbord_but.setIconSize(QSize(50, 50))
        self.dashbord_but.setCheckable(True)
        self.dashbord_but.setChecked(False)

        self.verticalLayout.addWidget(self.dashbord_but)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.employees_but = QPushButton(self.sidebar_widget)
        self.employees_but.setObjectName(u"employees_but")
        self.employees_but.setEnabled(True)
        sizePolicy.setHeightForWidth(self.employees_but.sizePolicy().hasHeightForWidth())
        self.employees_but.setSizePolicy(sizePolicy)
        self.employees_but.setMaximumSize(QSize(300, 60))
        self.employees_but.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.employees_but.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 19px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/b2e30a1c-78b2-484d-9e76-eeb775bf3efe.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.employees_but.setIcon(icon1)
        self.employees_but.setIconSize(QSize(40, 40))
        self.employees_but.setCheckable(True)

        self.verticalLayout.addWidget(self.employees_but)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.users_but = QPushButton(self.sidebar_widget)
        self.users_but.setObjectName(u"users_but")
        sizePolicy.setHeightForWidth(self.users_but.sizePolicy().hasHeightForWidth())
        self.users_but.setSizePolicy(sizePolicy)
        self.users_but.setMaximumSize(QSize(300, 60))
        self.users_but.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.users_but.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 19px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/images/9da65888-5452-42cc-99a5-c43c5d1c1e25.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.users_but.setIcon(icon2)
        self.users_but.setIconSize(QSize(40, 40))
        self.users_but.setCheckable(True)

        self.verticalLayout.addWidget(self.users_but)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.search_but = QPushButton(self.sidebar_widget)
        self.search_but.setObjectName(u"search_but")
        sizePolicy.setHeightForWidth(self.search_but.sizePolicy().hasHeightForWidth())
        self.search_but.setSizePolicy(sizePolicy)
        self.search_but.setMaximumSize(QSize(300, 60))
        self.search_but.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.search_but.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 19px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/774e6bc4-0dbc-4e70-8131-c78affd14da3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_but.setIcon(icon3)
        self.search_but.setIconSize(QSize(40, 40))
        self.search_but.setCheckable(True)

        self.verticalLayout.addWidget(self.search_but)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.report_but = QPushButton(self.sidebar_widget)
        self.report_but.setObjectName(u"report_but")
        sizePolicy.setHeightForWidth(self.report_but.sizePolicy().hasHeightForWidth())
        self.report_but.setSizePolicy(sizePolicy)
        self.report_but.setMaximumSize(QSize(300, 60))
        self.report_but.setFont(font)
        self.report_but.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.report_but.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 19px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(80, 160, 255, 120);\n"
"    border: 1px solid rgba(120, 200, 255, 150);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/934b5a52-04b2-4a9a-8704-d8186cc9c592.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.report_but.setIcon(icon4)
        self.report_but.setIconSize(QSize(40, 40))
        self.report_but.setCheckable(True)

        self.verticalLayout.addWidget(self.report_but)

        self.verticalSpacer_6 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.line = QFrame(self.sidebar_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.exit_but = QPushButton(self.sidebar_widget)
        self.exit_but.setObjectName(u"exit_but")
        self.exit_but.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.exit_but.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 80, 80, 70);\n"
"    border: 1px solid rgba(255, 120, 120, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(220, 60, 60, 100);\n"
"    border: 1px solid rgba(255, 100, 100, 130);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/473d8bb0-c378-493d-99e6-c0e32c6497c6.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_but.setIcon(icon5)
        self.exit_but.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.exit_but)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_main.addWidget(self.sidebar_widget)

        MainDashbord.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainDashbord)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 22))
        MainDashbord.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainDashbord)
        self.statusbar.setObjectName(u"statusbar")
        MainDashbord.setStatusBar(self.statusbar)

        self.retranslateUi(MainDashbord)

        self.stackedWidget_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainDashbord)
    # setupUi

    def retranslateUi(self, MainDashbord):
        MainDashbord.setWindowTitle(QCoreApplication.translate("MainDashbord", u"MainWindow", None))
        self.clock_label.setText(QCoreApplication.translate("MainDashbord", u"8:52", None))
        self.date_label.setText(QCoreApplication.translate("MainDashbord", u"\u0686\u0647\u0627\u0631\u0634\u0646\u0628\u0647 25 \u0634\u0647\u0631\u06cc\u0648\u0631 1405", None))
        self.modiriat_label.setText(QCoreApplication.translate("MainDashbord", u"\u0633\u0627\u0645\u0627\u0646\u0647 \u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0645\u0646\u062f\u0627\u0646", None))
        self.Modiriat_discrip_label.setText(QCoreApplication.translate("MainDashbord", u"\u0645\u0634\u0627\u0647\u062f\u0647\u060c \u062c\u0633\u062a\u062c\u0648 \u0648 \u0645\u062f\u06cc\u0631\u06cc\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u0627\u0631\u06a9\u0646\u0627\u0646 \u0633\u0627\u0632\u0645\u0627\u0646", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainDashbord", u"\u062a\u0639\u062f\u0627\u062f \u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.label_6.setText(QCoreApplication.translate("MainDashbord", u"3", None))
        self.label_7.setText("")
        self.label_2.setText(QCoreApplication.translate("MainDashbord", u"\u062a\u0639\u062f\u0627\u062f \u06a9\u0627\u0631\u0645\u0646\u062f\u0627\u0646", None))
        self.label_3.setText(QCoreApplication.translate("MainDashbord", u"56", None))
        self.label_4.setText("")
        self.label_17.setText("")
        self.label_16.setText(QCoreApplication.translate("MainDashbord", u"Mahdi", None))
        self.label_8.setText(QCoreApplication.translate("MainDashbord", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc:", None))
        self.label_9.setText(QCoreApplication.translate("MainDashbord", u"\u0645\u0647\u062f\u06cc \u062a\u0627\u062c \u0622\u0628\u0627\u062f\u06cc", None))
        self.logo_label_2.setText("")
        self.changes_but.setText(QCoreApplication.translate("MainDashbord", u"\u0630\u062e\u06cc\u0631\u0647 \u062a\u063a\u06cc\u06cc\u0631\u0627\u062a", None))
        self.label_15.setText("")
        self.label_14.setText(QCoreApplication.translate("MainDashbord", u"\u0628\u0631\u0627\u06cc \u0627\u0641\u0632\u0627\u06cc\u0634 \u0627\u0645\u0646\u06cc\u062a \u062d\u0633\u0627\u0628 \u062e\u0648\u062f\u060c \u0631\u0645\u0632 \u0639\u0628\u0648\u0631\n"
"\u0631\u0627 \u0628\u0647\u200c\u0635\u0648\u0631\u062a \u062f\u0648\u0631\u0647\u200c\u0627\u06cc \u062a\u063a\u06cc\u06cc\u0631 \u062f\u0647\u06cc\u062f.", None))
        self.btn_change_password.setText(QCoreApplication.translate("MainDashbord", u" \u062a\u063a\u06cc\u06cc\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631  ", None))
        self.label_11.setText(QCoreApplication.translate("MainDashbord", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc", None))
        self.label_10.setText(QCoreApplication.translate("MainDashbord", u"\u0646\u0627\u0645", None))
        self.label_13.setText(QCoreApplication.translate("MainDashbord", u"\u0627\u06cc\u0645\u06cc\u0644", None))
        self.label_12.setText(QCoreApplication.translate("MainDashbord", u"\u062a\u0644\u0641\u0646 \u0647\u0645\u0631\u0627\u0647", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainDashbord", u"mahditaj2000@gmail.com", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainDashbord", u"09129596597", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainDashbord", u"\u062a\u0627\u062c \u0622\u0628\u0627\u062f\u06cc", None))
        self.lineEdit.setText(QCoreApplication.translate("MainDashbord", u"\u0645\u0647\u062f\u06cc", None))
        self.logo_label.setText("")
        self.user_name.setText(QCoreApplication.translate("MainDashbord", u"\u062a\u0627\u062c \u0622\u0628\u0627\u062f\u06cc", None))
        self.dashbord_but.setText(QCoreApplication.translate("MainDashbord", u"\u062f\u0627\u0634\u0628\u0648\u0631\u062f", None))
        self.employees_but.setText(QCoreApplication.translate("MainDashbord", u"\u06a9\u0627\u0631\u0645\u0646\u062f\u0627\u0646 ", None))
        self.users_but.setText(QCoreApplication.translate("MainDashbord", u"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646 ", None))
        self.search_but.setText(QCoreApplication.translate("MainDashbord", u"\u062c\u0633\u062a\u062c\u0648  ", None))
        self.report_but.setText(QCoreApplication.translate("MainDashbord", u"\u062a\u0646\u0638\u06cc\u0645\u0627\u062a", None))
        self.exit_but.setText(QCoreApplication.translate("MainDashbord", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0633\u0627\u0645\u0627\u0646\u0647", None))
    # retranslateUi

