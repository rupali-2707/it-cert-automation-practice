import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from TRY111 import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win=QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.ui.pushButton.clicked.connect(self.showLogin)



    def show(self):
        self.main_win.show()

    def showLogin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
