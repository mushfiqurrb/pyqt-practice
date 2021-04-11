import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

import first_window_ui
import second_window_ui


class Runn(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.firstwindow = first_window_ui.firstWindow()
        self.secondwindow = second_window_ui.secondWindow()
        self.firstwindow.ui.pushButton.clicked.connect(self.passingInformation)

    def passingInformation(self):
        # self.secondwindow = second.SecondWindow()
        self.secondwindow.ui.textEdit.setText(self.firstwindow.ui.textEdit.toPlainText())
        self.secondwindow.show_window()


if __name__ == '__main__':
    app = QApplication([])
    abc = Runn()
    abc.firstwindow.show_window()
    abc.secondwindow.show_window()
    sys.exit(app.exec_())
