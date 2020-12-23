from PySide2 import QtWidgets,QtGui, QtCore
from PySide2.QtWidgets import QMainWindow, QAction, QApplication,QPushButton, QMessageBox
from dataHandler.file import File
from dataHandler.path import Path
from dataHandler.table.table import Table


class WorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_tab_widget = None
        self.tabEditor = None

        self.create_main_tab_widget()

        self.main_layout.addWidget(self.main_tab_widget)

        self.setLayout(self.main_layout)

    def create_main_tab_widget(self):
        self.main_tab_widget = QtWidgets.QTabWidget(self)
        self.main_tab_widget.setTabsClosable(True)
        self.main_tab_widget.tabCloseRequested.connect(self.delete_tab)
        # self.show_tabs()

    def create_new_sequential_file_workspace(self, file_c):
        title = file_c.get_file_name()
        row_count = file_c.row_count()
        column_count = file_c.column_count()

        table = QtWidgets.QTableWidget(row_count, column_count, self.main_tab_widget)
        self.main_tab_widget.addTab(table, title)

        table.setHorizontalHeaderLabels(file_c.metadata_c.metadata["headers"])

        for i in range(0, row_count):
            file_c.set_table_row(table, i)

    def create_new_serial_file_workspace(self, file_c):
        tab = QtWidgets.QTabWidget(self)
        table = Table(tab)

        tab.addTab(table, file_c.get_file_name())
        self.main_tab_widget.addTab(tab, file_c.path_c.get_file_name_R())

        table.setModel(file_c)

    def delete_tab(self, index):
        self.main_tab_widget.removeTab(index)

    def save(self):
        print("Kliknuo sam sav!!!!!")#self.main_tab_widget.currentWidget().currentWidget().table.save()

    def save_all(self, close=False):
        print("Kliknuo sam sav!!!!!")
        for i in range(0, self.main_tab_widget.count()):  # prolazimo kroz sve glavne tabove fajlova
            self.main_tab_widget.setCurrentIndex(i)
            current_tab = self.main_tab_widget.currentWidget()

            for j in range(0, current_tab.count()):  # prolazimo korz sve table fajlova(serijaka ima samo 1)
                current_tab.setCurrentIndex(j)
                current_tab.currentWidget().save()

            if close:
                self.main_tab_widget.removeTab(i)

    def open_file(self, file_path):

        path_c = Path(file_path)
        #TODO otvoriti dodatni window za path
        if path_c.get_extension() != "csv":
            # TODO: prekinuti program sa pop out window i obavestiti korisnika da moze da otvori samo csv fajl
            
            
            return

        file_c = File(path_c)

        if file_c.metadata_c.metadata["is_sequential"]:
            self.create_new_sequential_file_workspace(file_c)
        else:
            self.create_new_serial_file_workspace(file_c)


#self.button.clicked.connect(showpop)
