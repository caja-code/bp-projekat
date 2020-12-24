import sys
from PySide2 import  QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QMainWindow, QAction, QApplication,QPushButton, QMessageBox
from PySide2.QtGui import QIcon



class MenuBar(QtWidgets.QMenuBar):
    def __init__(self,parent):
        super().__init__(parent)


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
        self.newAct.triggered.connect(self.show_popup)
        self.file_menu.addAction(self.newAct)

        #open
        self.openAct = QAction(QIcon('slike/open.png'), '&Open', self)
        self.openAct.setStatusTip('Open file')
        #self.openAct.triggered.connect(self.parent().workspace.open_file)
        self.openAct.triggered.connect(self.show_popup)
        self.file_menu.addAction(self.openAct)

        #save
        self.saveAct = QAction(QIcon('slike/save.jpg'), '&Save', self)
        self.saveAct.setShortcut('Ctrl+S')
        self.saveAct.setStatusTip('Saving application')
        self.saveAct.triggered.connect(self.parent().workspace.save)
        self.file_menu.addAction(self.saveAct)

        
        #save all
        self.saveAllAct = QAction(QIcon('slike/save.jpg'), '&Save All', self)
        self.saveAllAct.setStatusTip('Saving application')
        self.saveAllAct.triggered.connect(self.parent().workspace.save_all)
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
        self.copyAct.triggered.connect(self.show_popup)
        self.copyAct.setStatusTip('Under Construction')

        self.edit_menu.addAction(self.copyAct)
        #past
        self.pasteAct = QAction(QIcon('slike/paste.png'), '&Paste', self)
        self.pasteAct.triggered.connect(self.show_popup)
        self.pasteAct.setStatusTip('Under Construction')

        self.edit_menu.addAction(self.pasteAct)
        #cut
        self.cutAct = QAction(QIcon('slike/cut.jpg'), '&Cut', self)
        self.cutAct.triggered.connect(self.show_popup)
        self.cutAct.setStatusTip('Under Construction')

        self.edit_menu.addAction(self.cutAct)
        #find
        self.findAct = QAction(QIcon('slike/find.jpg'), '&Find', self)
        self.findAct.setStatusTip('Quick search')

        self.edit_menu.addAction(self.findAct)
        #back
        self.backAct = QAction(QIcon('slike/back.png'), '&Back', self)
        self.backAct.triggered.connect(self.show_popup)
        self.backAct.setStatusTip('Go one step back')

        self.edit_menu.addAction(self.backAct)
        #forward 
        self.forwardAct = QAction(QIcon('slike/forward.png'), '&Forward', self)
        self.forwardAct.triggered.connect(self.show_popup)
        self.forwardAct.setStatusTip('Go one step forward')

        self.edit_menu.addAction(self.forwardAct)

        #help menu
        #about
        self.aboutAct = QAction(QIcon('slike/about.jpg'), '&About', self)
        self.aboutAct.setStatusTip('Under Construction')
        self.aboutAct.triggered.connect(self.show_popup)

        self.help_menu.addAction(self.aboutAct)

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self,'Closing menu', 'Do you want to exit the application?',QtWidgets .QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets .QMessageBox.Yes:
            print("Closing the application.")
            sys.exit()
        else:
            pass

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Fatal Error")
        msg.setText("Post Error! error code = 503")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Under Contructions!")
        msg.setDetailedText("This command isnt currently working pleas stand by untill we finish the contructions")

        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def popup_button(self,i):
        print(i.text())