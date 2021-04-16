from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashSCreen(object):
    def __init__(self,window):
        super(Ui_SplashSCreen, self).__init__()
        self.setupUi(window)


    def setupUi(self, SplashSCreen):
        SplashSCreen.setObjectName("SplashSCreen")
        SplashSCreen.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(SplashSCreen)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setGeometry(QtCore.QRect(0, 0, 681, 401))
        self.dropShadowFrame.setStyleSheet("QFrame{\n"
"color: rgb(10, 66, 127);\n"
"background-color:rgb(162, 155, 255);\n"
"border-radius:20px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.main_label = QtWidgets.QLabel(self.dropShadowFrame)
        self.main_label.setGeometry(QtCore.QRect(16, 70, 651, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(40)
        self.main_label.setFont(font)
        self.main_label.setStyleSheet("background-color: rgb(216, 255, 221);")
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(100, 260, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(13)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(173, 167, 255);\n"
"    \n"
"    color: rgb(0, 0, 127);\n"
"border-radius:20px;\n"
"text-align:centre;\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius:20px;\n"
"    background-color: rgb(67, 170, 150);\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.loading_label = QtWidgets.QLabel(self.dropShadowFrame)
        self.loading_label.setGeometry(QtCore.QRect(6, 290, 671, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        font.setStrikeOut(False)
        self.loading_label.setFont(font)
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_label.setWordWrap(True)
        self.loading_label.setObjectName("loading_label")
        self.createdby_label = QtWidgets.QLabel(self.dropShadowFrame)
        self.createdby_label.setGeometry(QtCore.QRect(20, 350, 651, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.createdby_label.setFont(font)
        self.createdby_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.createdby_label.setWordWrap(True)
        self.createdby_label.setObjectName("createdby_label")
        SplashSCreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashSCreen)
        QtCore.QMetaObject.connectSlotsByName(SplashSCreen)

    def retranslateUi(self, SplashSCreen):
        _translate = QtCore.QCoreApplication.translate
        SplashSCreen.setWindowTitle(_translate("SplashSCreen", "MainWindow"))
        self.main_label.setText(_translate("SplashSCreen", "Practice Py-QT"))
        self.loading_label.setText(_translate("SplashSCreen", "<html><head/><body><p>Loading</p></body></html>"))
        self.createdby_label.setText(_translate("SplashSCreen", "<html><head/><body><p><span style=\" font-weight:600;\">Created by: Mushfiq</span></p></body></html>"))



