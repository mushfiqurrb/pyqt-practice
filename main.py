from PyQt5 import QtWidgets, QtGui, QtCore
import mainWindow1
import sys

from splashScreen import Ui_SplashSCreen


class SplashScreen(Ui_SplashSCreen):
    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent)


class HomePage(mainWindow1.Ui_MainWindow1):
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)
        self.number_goods = 10
        self.profit = 25
        self.loss = 12

        # self.weight_plus_button.clicked.connect(self.increaseWeight)
        # self.weight_minus_button.clicked.connect(self.decreaseWeight)

        # self.age_plus_button.clicked.connect(self.increaseAge)
        # self.age_minus_button.clicked.connect(self.decreaseAge)

        # self.horizontalSlider.valueChanged.connect(self.slidervalue)
        # self.Calc_button.clicked.connect(self.showResult)

        self.timer = QtCore.QTimer()
        self.timer.singleShot(3000, self.hide)

    def show(self):
        self.swindow = QtWidgets.QMainWindow()
        self.sscreen = SplashScreen(self.swindow)
        self.swindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.hide()
        self.swindow.show()

    def hide(self):
        self.swindow.close()
        MainWindow.show()

    # def showResult(self):
    #     self.resultWindow = QtWidgets.QMainWindow()
    #     self.number = self.Bmiformula()

    #     self.resultUi = Ui_ResultWindow(window=self.resultWindow, text=self.number)
    #     self.resultUi.pushButton.clicked.connect(self.resultuiPushButton)
    #     self.resultUi.analysis()
    #     self.resultWindow.setWindowIcon(QtGui.QIcon("img/icons.png"))
    #     MainWindow.show()
    #     self.resultWindow.show()

    # def resultuiPushButton(self):
    #     self.resultWindow.hide()
    #     MainWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("img/icons.png"))
    MainWindow = QtWidgets.QMainWindow()
    ui = HomePage(MainWindow)
    ui.show()
    sys.exit(app.exec_())
