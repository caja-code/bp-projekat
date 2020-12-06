from PySide2 import QtWidgets, QtGui, QtCore
from student import Student
from polozeni_predmet import PolozeniPredmet
from nepolozeni_predmet import NepolozeniPredmet
from student_model import StudentModel
from polozeni_predmet_model import PolozeniPredmetModel
from nepolozeni_predmet_model import NepolozeniPredmetModel

class WorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()

        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.student_model = self.create_dummy_model()
        self.table1.setModel(self.student_model)
        
        self.table1.clicked.connect(self.student_selected)
        self.table1.clicked.connect(self.show_tabs)

        self.subtable1 = QtWidgets.QTableView(self.tab_widget)
        self.subtable2 = QtWidgets.QTableView(self.tab_widget)  
    
        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def student_selected(self, index):
        model = self.table1.model()
        selected_student = model.get_element(index)

        polozeni_predmeti_model = PolozeniPredmetModel()
        polozeni_predmeti_model.polozeni_predmeti = selected_student.polozeni_predmeti

        nepolozeni_predmeti_model = NepolozeniPredmetModel()
        nepolozeni_predmeti_model.nepolozeni_predmeti =  selected_student.nepolozeni_predmeti

        self.subtable1.setModel(polozeni_predmeti_model)
        self.subtable2.setModel(nepolozeni_predmeti_model)
    
    def show_tabs(self):
        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmet")
        self.tab_widget.addTab(self.subtable2, QtGui.QIcon("icons8-edit-file-64.png"), "Nepolozeni predmet")
        
    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)
    


    def create_dummy_model(self):
        student_model = StudentModel()
        student_model.students = [
            Student("2018270000", "Marko Markovic", [
                PolozeniPredmet("OOP1", "", 7),
                PolozeniPredmet("SIMS", "", 8),
            ],
            [
                NepolozeniPredmet("BP", "", 3),
                NepolozeniPredmet("AR", "", 2)
            ]),
            Student("2018270001", "Petar Petrovic", [
                PolozeniPredmet("OOP1", "", 7),
                PolozeniPredmet("SIMS", "", 8),
            ],
            [
                NepolozeniPredmet("Analiza1", "", 2),
                NepolozeniPredmet("Diskretna Matematika", "", 2)
            ]),
            Student("2018270002", "Janko Jankovic", [
                PolozeniPredmet("OP", "", 7),
                PolozeniPredmet("BP", "", 8),
            ],
            [
                NepolozeniPredmet("Web dizajn", "", 1),
                NepolozeniPredmet("AR", "", 2)
            ]),
            Student("2018270003", "Stefan Stefanovic", [
                PolozeniPredmet("OOP1", "", 7),
                PolozeniPredmet("SIMS", "", 8),
            ],
            [
                NepolozeniPredmet("Web programiranje", "", 3),
                NepolozeniPredmet("OOP2", "", 2)
            ]),
            Student("2018270004", "Ivan Ivanovic", [
                PolozeniPredmet("OOP1", "", 7),
                PolozeniPredmet("SIMS", "", 8),
            ])
        ]

        return student_model

        
