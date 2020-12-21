
from PySide2 import  QtWidgets, QtGui, QtCore


class MenuBar(QtWidgets.QMenu):
    def __init__(self,parent):
        super().__init__()

        self.menu_bar = QtWidgets.QMenuBar(self)
        self.file_menu = QtWidgets.QMenu("File",self.menu_bar)
        self.edit_menu = QtWidgets.QMenu("Edit",self.menu_bar)
        self.view_menu = QtWidgets.QMenu("View",self.menu_bar)
        self.help_menu = QtWidgets.QMenu("Help",self.menu_bar)

        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.edit_menu)
        self.menu_bar.addMenu(self.view_menu)
        self.menu_bar.addMenu(self.help_menu)
