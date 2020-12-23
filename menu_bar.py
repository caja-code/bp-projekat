import sys
from PySide2 import  QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QMainWindow, QAction, QApplication,QPushButton, QMessageBox
from PySide2.QtGui import QIcon



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

        
        #file menu
        #new
        self.newAct = QAction(QIcon('slike/new.png'), '&New', self)
        self.newAct.setStatusTip('Under Construction')
        
        self.file_menu.addAction(self.newAct)

        #open
        self.openAct = QAction(QIcon('slike/open.png'), '&Open', self)
        self.openAct.setStatusTip('Under Construction')

        self.file_menu.addAction(self.openAct)

        #save
        
        self.saveAct = QAction(QIcon('slike/save.jpg'), '&Save', self)
        self.saveAct.setStatusTip('Saving application')
        self.saveAct.triggered.connect(self.saving_current_application)
        self.file_menu.addAction(self.saveAct)
    
        #save all
        self.saveAllAct = QAction(QIcon('slike/save.jpg'), '&Save All', self)
        self.saveAllAct.setStatusTip('Saving application')
        self.saveAllAct.triggered.connect(self.saving_all_application)
        self.file_menu.addAction(self.saveAllAct)

        #Gasenje aplikacije
        self.exitAct = QAction(QIcon('slike/exit.jpg'), '&Exit', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(self.close_application)

        self.file_menu.addAction(self.exitAct)

        #Edit menu
        #copy
        self.copyAct = QAction(QIcon('slike/copy.png'), '&Copy', self)
        self.copyAct.setStatusTip('Under Construction')

        self.edit_menu.addAction(self.copyAct)
        #past
        self.pasteAct = QAction(QIcon('slike/paste.png'), '&Paste', self)
        self.pasteAct.setStatusTip('Under Construction')

        self.edit_menu.addAction(self.pasteAct)
        #cut
        self.cutAct = QAction(QIcon('slike/cut.jpg'), '&Cut', self)
        self.cutAct.setStatusTip('Under Construction')

        self.edit_menu.addAction(self.cutAct)
        #help menu
        #about
        self.aboutAct = QAction(QIcon('slike/about.jpg'), '&About', self)
        self.aboutAct.setStatusTip('Under Construction')

        self.help_menu.addAction(self.aboutAct)

        
    

        #pitanje da li zeli user da zatvori aplikaciju
        #Todo igor saving
    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self,'Closing menu', 'Do you want to exit the application?',QtWidgets .QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets .QMessageBox.Yes:
            print("Closing the application.")
            sys.exit()
        else:
            pass

    