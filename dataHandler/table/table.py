from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QPoint
from PySide2.QtWidgets import QAbstractItemView, QAction

from dataHandler.sort.sort import sort


class Table(QtWidgets.QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.model_c = None

    def setModel(self, model_c):
        self.model_c = model_c

        row_count = self.model_c.row_count()
        column_count = self.model_c.column_count()

        self.setColumnCount(column_count)
        self.setRowCount(row_count)

        self.setHorizontalHeaderLabels(model_c.metadata_c.metadata["headers"])

        self.setSelectionBehavior(self.SelectRows)

        self.setContextMenuPolicy(Qt.CustomContextMenu)

        for i in range(0, row_count):
            model_c.set_table_row(self, i)

        self.itemChanged.connect(self.on_change)
        self.customContextMenuRequested.connect(self.option_menu)
        self.horizontalHeader().sectionClicked.connect(self.sort_by_header)

    def option_menu(self, pos):

        menu = QtWidgets.QMenu(self)

        delete_selected_rows = QAction('Delete', self)

        menu.addAction(delete_selected_rows)
        menu.exec_(self.viewport().mapToGlobal(pos))

        delete_selected_rows.triggered.connect(self.delete_selected_rows())

    def sort_by_header(self, header):
        ...
        '''self.model_c.temp_data = sort(self.model_c.data, self.model_c.metadata_c.metadata["headers"][header])
        self.clearContents()
        #print(self.model_c.temp_data)
        for i in range(0, len(self.model_c.temp_data)):
            self.model_c.set_temp_table_row(self, i)'''

    # TODO: Obrisati ako ne treba
    def get_title(self):
        return self.model_c.get_file_name()

    def on_change(self):
        changed_item = self.currentItem()
        self.parent().parent().parent().parent().setStatusTip("Izmena unesena")
        if not self.model_c.set_data(changed_item.row(), changed_item.column(), changed_item.text()):
            ...
            # TODO: pop up widow sa ispisiavnjem greske da tabla nije uspesno promenjna

    def delete_selected_rows(self):
        indexes = self.selectionModel().selectedRows()
        for index in sorted(indexes, reverse=True):
            del self.model_c.data[index.row()]
            self.removeRow(index.row())

    def save(self):
        self.model_c.write_data()

    def find(self, txt):
        print(txt)
        self.render_table(self.model_c.find(txt))

    def render_table(self, arr):
        for i in range(0, self.rowCount()):
            if i not in arr:
                self.hideRow(i)
