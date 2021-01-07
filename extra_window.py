from PySide2 import  QtWidgets
from PySide2.QtWidgets import QVBoxLayout, QLineEdit,QDialogButtonBox


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
       
  
    