import sys

from PySide2 import QtWidgets

from component.main_window import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
