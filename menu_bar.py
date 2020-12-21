
from PySide2 import  QtWidgets, QtGui, QtCore


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self):
        super().__init__()


        self.file_menu = QtWidgets.QMenu("File",self)
        self.edit_menu = QtWidgets.QMenu("Edit",self)
        self.view_menu = QtWidgets.QMenu("View",self)
        self.help_menu = QtWidgets.QMenu("Help",self)

        self.addMenu(self.file_menu)
        self.addMenu(self.edit_menu)
        self.addMenu(self.view_menu)
        self.addMenu(self.help_menu)
