
import sys

from PySide2 import  QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QWidget,QMainWindow, QVBoxLayout, QApplication,QPushButton,QDialog,QApplication, QLabel, QGroupBox,QLineEdit,QDialogButtonBox
from PySide2.QtGui import QIcon,QFont
from status_bar import StatusBar
from PySide2.QtCore import Qt

from workspaceWidget import WorkspaceWidget

class ExtraWindow(QtWidgets.QDialog):
    def __init__(self,parent):
        super().__init__(parent)

        self.setWindowTitle("customer - Table")
        self.setGeometry(300,200,500,400)
        
        self.edit = QLineEdit("Under Construction pleas wait until the next update!")
    
        self.buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    

        self.buttonBox = QDialogButtonBox(self.buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        
        self.show()
       
  
    