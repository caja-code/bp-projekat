import sys

from PySide2 import  QtWidgets, QtGui, QtCore

from main_window import MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()

    sys.exit(app.exec_())   