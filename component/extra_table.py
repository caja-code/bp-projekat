from PySide2 import QtWidgets,QtGui
from PySide2.QtCore import Qt, QPoint
from PySide2.QtWidgets import QAbstractItemView, QAction,QTableWidgetItem,QComboBox,QMessageBox,QFileDialog,QCheckBox
from PySide2.QtCore import QCoreApplication
from component.read_only_delegate import ReadOnlyDelegate

#prosledimo path


#Prozor koji menja podatke i kreira, TableMetaEditor
class ExtraTable(QtWidgets.QTableWidget):
    def __init__(self,parent):
        super().__init__(parent)
        

            #self.path_c = f'podaci{os.path.sep}__' tu treba da bude ono sto je korisnik nazvao tabelu,podaci\studenti
            # napraviti funkciju koja proverava da li su dve putanje iste is_save postoji
            #napraviti funkciju koja prolazi kroz odabrani folder(podaci) hard cod i za svaki file u njemu proverava 
            # da li je isti kao fajl koji smo kreirali



        #delegate blokira column po rendom index da se ne moze pristupi pronemi vrednosti tabele
       

        delegate = ReadOnlyDelegate(self)
       

        self.setItemDelegateForColumn(0, delegate)
        self.setItemDelegateForColumn(1, delegate)
        self.setItemDelegateForColumn(2, delegate)
        self.setItemDelegateForColumn(3, delegate)
        self.setItemDelegateForColumn(4, delegate)
        self.setItemDelegateForColumn(5, delegate)

        
      
        #self.ID = self.extra_table.item(row, column)
       

        if (self.columnCount() < 6):
            self.setColumnCount(6)


        __qtablewidgetitem = QTableWidgetItem()
        self.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.setHorizontalHeaderItem(5, __qtablewidgetitem5)
    

        self.setGeometry(0, 40, 661, 201)
        self.setColumnWidth(2,85)
        self.setColumnWidth(3,85)
        self.setColumnWidth(4,85)
        
       
        
        self.setSelectionBehavior(self.SelectRows)

        #self.load_data("podaci\naziv_tabele.json")

        self.headersi()
 

        
        
    def headersi(self):
        
        ___qtablewidgetitem = self.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ExtraWindow", u"Column Name", None))
        ___qtablewidgetitem1 = self.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ExtraWindow", u"Data Type", None))
        ___qtablewidgetitem2 = self.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ExtraWindow", u"Primary key", None))
        ___qtablewidgetitem3 = self.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ExtraWindow", u"Foreign key", None))
        ___qtablewidgetitem4 = self.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ExtraWindow", u"Not Null", None))
        ___qtablewidgetitem5 = self.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ExtraWindow", u"Default", None))

        
        
    
# moram da ucitam blanko podatke koji su prazni nemaju nista,
# preko putanje hard kodovati prilikom sava 