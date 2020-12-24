from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QMainWindow, QAction, QApplication, QPushButton, QMessageBox
from dataHandler.file import File
from dataHandler.path import Path
from dataHandler.table.table import Table


class SerialEditor(QtWidgets.QTabWidget):
    def __init__(self, parent, file_c):
        super().__init__(parent)
        table = Table(self)

        self.addTab(table, file_c.get_file_name())
        parent.main_tab_widget.addTab(self, file_c.path_c.get_file_name_R())

        table.setModel(file_c)

    def saveX(self):
        print("save sam")
