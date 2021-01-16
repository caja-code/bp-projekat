from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QHBoxLayout, QLineEdit, QDialogButtonBox,QWidget,QPushButton,QCheckBox,QLabel,QTableWidget, \
    QTableWidgetItem,QFrame,QTableView,QFileDialog,QMessageBox
from PySide2.QtCore import QCoreApplication
from component.extra_table import ExtraTable 
from dataHandler.dataExtras.metadata_r import _make_blank_metadata,MetaDataR
from dataHandler.dataExtras.path import Path
import os
import PySide2


class ExtraWindow(QtWidgets.QDialog):
    def __init__(self, parent,edit=False,path_c= None):
        super().__init__(parent)
        self.meta = None
        if edit:
            self.path_c = path_c
            self.meta = MetaDataR(self.path_c.get_metadata_path())
        else:
            self.path_c = None
            self.meta = _make_blank_metadata()

        #self.path_c = f'podaci{os.path.sep}__podaci\saimenom.csv
        
        #self.load_data("podaci\naziv_tabele.json")

        #print(self.meta)
        #print(self.path_c)


            #self.path_c = f'podaci{os.path.sep}__' tu treba da bude ono sto je korisnik nazvao tabelu,podaci\studenti
            # napraviti funkciju koja proverava da li su dve putanje iste is_save postoji
            #napraviti funkciju koja prolazi kroz odabrani folder(podaci) hard cod i za svaki file u njemu proverava 
            # da li je isti kao fajl koji smo kreirali
   

        self.extra_table = ExtraTable(self)
    

        #self.extra_table.cellClicked.connect(self.extra_table.current_column_name)


        self.setWindowTitle("customer - Table")
        self.setWindowIcon(QtGui.QIcon("assets/img/icons8-edit-file-64.png"))
        
        self.resize(662, 438)

        self.save_table_changes = QPushButton("Save table changes",self)
        self.save_table_changes.setGeometry(390, 290, 251, 31)
        

        self.add_table_main = QPushButton("Add Column ",self)
        self.add_table_main.setGeometry(390, 260, 251, 28)
        self.add_table_main.clicked.connect(self.add_column)
        

        self.delet_table_column = QPushButton("Delet table column",self)
        self.delet_table_column.setGeometry(390, 330, 251, 31)
        self.delet_table_column.clicked.connect(self.remove_row)

        self.not_null_box = QCheckBox("Not Null",self)
        self.not_null_box.setGeometry(220, 330, 81, 61)

        self.colm_name_label = QLabel("Column Name:",self)
        self.colm_name_label.setGeometry(10, 250, 111, 41)
        
        self.table_name_label_2 = QLabel("Table Name",self)
        self.table_name_label_2.setGeometry(10, 10, 91, 21)
        

        self.comn_name_line_edit = QLineEdit(self)
        self.comn_name_line_edit.setGeometry(110, 260, 151, 22)
        #self.comn_name_line_edit.clicked.connect(self.extra_table.current_column_name)
        
        self.data_type_label = QLabel("Data Type",self)
        self.data_type_label.setGeometry(10, 300, 61, 16)

        self.data_type_line_edit = QLineEdit(self)
        self.data_type_line_edit.setGeometry(110, 300, 151, 22)

        self.table_name_line_edit = QLineEdit(self)
        self.table_name_line_edit.setGeometry(110, 10, 391, 22)

        self.foreign_key_box = QCheckBox("Foreign Key",self)
        self.foreign_key_box.setGeometry(120, 330, 91, 61)

        self.primary_key_box = QCheckBox("Primary Key",self)
        self.primary_key_box.setGeometry(20, 330, 111, 61)

        self.frame = QFrame(self)
        self.frame.setGeometry(0, 390, 661, 51)
        self.frame.setStyleSheet(u"background-color: rgb(45,45,45);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.cancel_button = QPushButton("Cancel button",self.frame)
        self.cancel_button.setGeometry(550, 10, 111, 28)
        
        self.cancel_button.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.add_table_button = QPushButton("Add table",self.frame)

        self.add_table_button.setGeometry(442, 10, 101, 28)
        self.add_table_button.setStyleSheet(u"background-color: rgb(255,255,255);")
     
        
        #self.tables()
    
        
        
        self.show()


    def add_column_infomation(self):
        self.meta["headers"].append({
            "name": self.comn_name_line_edit.text(),
            "is_primary": self.primary_key_box.isChecked(),
            "is_foreign_key": self.foreign_key_box.isChecked(),
            "data_type": self.data_type_line_edit.text(),
            "predefined_values": "nesta",
            "not_null": self.not_null_box.isChecked(),
            })
            #iz tabele treba da se poziva row sa tim podacima
   
    

    def current_row(self):
        return self.extra_table.currentRow()
    
   

    #save column changes
 

    
    #kada korisnik kilkne na kolonu koja vec postoji nje podaci treba da se otvore u 
    # input poljima ako je korisnik stavio neku izmjenu u tim poljima u tabeli treba da se sacuvaju te izmene

   
        #funkcija koja ce za objekat iz metaheadersa da ubacuje u tabelu


    def add_column(self):
        self.add_column_infomation()
       
        #headers = self.get_headers_names()
            
        row = self.extra_table.rowCount()
        self.extra_table.insertRow(row)
        #print(headers)
     
        self.extra_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(self.meta["headers"][row]["name"])))
        self.extra_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.meta["headers"][row]["data_type"])))
        self.extra_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.meta["headers"][row]["is_primary"])))
        self.extra_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.meta["headers"][row]["is_foreign_key"])))
        self.extra_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(self.meta["headers"][row]["not_null"])))
        self.extra_table.setItem(row, 5, QtWidgets.QTableWidgetItem(str(self.meta["headers"][row]["predefined_values"])))
     
        
        
         #proveri da li su sve vrednosti stavljenje name i type
         # moram da ucitam blanko podatke koji su prazni nemaju nista,
        # preko putanje hard kodovati prilikom sava 

    def remove_row(self):
        indexes = self.extra_table.selectionModel().selectedRows()
        if len(indexes) != 1:   
            self.show_popup()
            return
        self.extra_table.removeRow(indexes[0].row())



    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Fatal Error")
        msg.setText("Post Error! error code = 503")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Pleas select a row you want to delet!")
     

        msg.buttonClicked.connect(self.popup_button)
        execute = msg.exec_()

    def popup_button(self, i):
        print(i.text())

    
   