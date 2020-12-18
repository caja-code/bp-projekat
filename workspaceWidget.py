from PySide2 import QtWidgets

from dataHandler.file import File
from dataHandler.path import Path


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

    def create_new_serial_file_workspace(self, file_c):
        title = file_c.get_file_name()
        row_count = file_c.rowCount()
        column_count = file_c.columnCount()

        table = QtWidgets.QTableWidget(row_count, column_count, self.main_tab_widget)
        self.main_tab_widget.addTab(table, title)

        table.setHorizontalHeaderLabels(file_c.metadata_c.metadata["headers"])

        for i in range(0, row_count):
            file_c.set_table_row(table, i)

    def create_new_sequential_file_workspace(self, file_c):
        table = QtWidgets.QTableView(self.main_tab_widget)

        table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.main_tab_widget.addTab(table, file_c.get_file_name())

        table.setModel(file_c)

    def delete_tab(self, index):
        self.main_tab_widget.removeTab(index)

    def open_file(self, file_path):

        path_c = Path(file_path)

        if path_c.get_extension() != "csv":
            # TODO: prekinuti program sa pop out window i obavestiti korisnika da moze da otvori samo csv fajl
            return

        file_c = File(path_c)

        if file_c.metadata_c.metadata["is_sequential"]:
            self.create_new_sequential_file_workspace(file_c)
        else:
            self.create_new_serial_file_workspace(file_c)