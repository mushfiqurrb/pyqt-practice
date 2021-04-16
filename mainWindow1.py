from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def __init__(self,window):
        super(Ui_MainWindow1, self).__init__()
        self.setupUi(window)


    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(800, 600)
        MainWindow1.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"border-color: rgb(192, 255, 250);")
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 100, 781, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.datetime_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(22)
        self.datetime_label.setFont(font)
        self.datetime_label.setStyleSheet("background-color: rgb(152, 143, 255);\n"
"color: rgb(255, 248, 162);")
        self.datetime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.datetime_label.setObjectName("datetime_label")
        self.verticalLayout.addWidget(self.datetime_label)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setStyleSheet("background-color: rgb(167, 255, 112);\n"
"border-color: rgb(255, 255, 127);\n"
"gridline-color: rgb(0, 170, 0);\n"
"selection-color: rgb(170, 170, 0);\n"
"color: rgb(0, 0, 127);")
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout.addWidget(self.dateTimeEdit)
        self.soldgoods_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(22)
        self.soldgoods_label.setFont(font)
        self.soldgoods_label.setStyleSheet("background-color: rgb(152, 143, 255);\n"
"color: rgb(255, 248, 162);")
        self.soldgoods_label.setAlignment(QtCore.Qt.AlignCenter)
        self.soldgoods_label.setObjectName("soldgoods_label")
        self.verticalLayout.addWidget(self.soldgoods_label)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setStyleSheet("background-color: rgb(167, 255, 112);\n"
"border-color: rgb(255, 255, 127);\n"
"gridline-color: rgb(0, 170, 0);\n"
"selection-color: rgb(170, 170, 0);\n"
"color: rgb(0, 0, 127);")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 80, 781, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(10, 10, 151, 71))
        self.dial.setObjectName("dial")
        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(176, 20, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(28)
        self.Header.setFont(font)
        self.Header.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Header.setStyleSheet("alternate-background-color: rgb(85, 85, 255);\n"
"color: rgb(170, 255, 127);\n"
"background-color: rgb(85, 85, 255);")
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setWordWrap(True)
        self.Header.setObjectName("Header")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(79, 330, 671, 161))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.profit_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        self.profit_label.setFont(font)
        self.profit_label.setStyleSheet("background-color: rgb(152, 143, 255);\n"
"color: rgb(255, 248, 162);")
        self.profit_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.profit_label.setObjectName("profit_label")
        self.horizontalLayout.addWidget(self.profit_label)
        self.loss_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loss_spinBox.sizePolicy().hasHeightForWidth())
        self.loss_spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(20)
        self.loss_spinBox.setFont(font)
        self.loss_spinBox.setStyleSheet("background-color: rgb(167, 255, 112);\n"
"border-color: rgb(255, 255, 127);\n"
"gridline-color: rgb(0, 170, 0);\n"
"selection-color: rgb(170, 170, 0);\n"
"color: rgb(0, 0, 127);\n"
"")
        self.loss_spinBox.setWrapping(True)
        self.loss_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.loss_spinBox.setObjectName("loss_spinBox")
        self.horizontalLayout.addWidget(self.loss_spinBox)
        self.loss_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        self.loss_label.setFont(font)
        self.loss_label.setStyleSheet("background-color: rgb(152, 143, 255);\n"
"color: rgb(255, 248, 162);")
        self.loss_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.loss_label.setObjectName("loss_label")
        self.horizontalLayout.addWidget(self.loss_label)
        self.profit_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profit_spinBox.sizePolicy().hasHeightForWidth())
        self.profit_spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.profit_spinBox.setFont(font)
        self.profit_spinBox.setStyleSheet("background-color: rgb(167, 255, 112);\n"
"border-color: rgb(255, 255, 127);\n"
"gridline-color: rgb(0, 170, 0);\n"
"selection-color: rgb(170, 170, 0);\n"
"color: rgb(0, 0, 127);")
        self.profit_spinBox.setWrapping(True)
        self.profit_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.profit_spinBox.setObjectName("profit_spinBox")
        self.horizontalLayout.addWidget(self.profit_spinBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(154, 500, 511, 51))
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"gridline-color: rgb(255, 255, 127);\n"
"font: 63 26pt \"Yu Gothic UI Semibold\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow"))
        self.datetime_label.setText(_translate("MainWindow1", "Current Date and Time"))
        self.soldgoods_label.setText(_translate("MainWindow1", "What is Your number of sold goods"))
        self.Header.setText(_translate("MainWindow1", "<html><head/><body><p>Provide Your Information</p></body></html>"))
        self.profit_label.setText(_translate("MainWindow1", "PROFIT = "))
        self.loss_label.setText(_translate("MainWindow1", "LOSS = "))
        self.pushButton.setText(_translate("MainWindow1", "PushButton"))



