from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QPoint
from PySide2.QtWidgets import QAbstractItemView, QAction


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
        self.customContextMenuRequested.connect(self.displayMenu)

    def displayMenu(self, pos):

        popMenu = QtWidgets.QMenu(self)

        delete_selected_rows = QAction('Delete', self)

        popMenu.addAction(delete_selected_rows)
        popMenu.exec_(self.viewport().mapToGlobal(pos))

        delete_selected_rows.triggered.connect(self.delete_selected_rows())

    # TODO: Obrisati ako ne treba
    def get_title(self):
        return self.model_c.get_file_name()

    def on_change(self):
        changed_item = self.currentItem()

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
        self.model_c.find(txt)
        self.render_table()

    def render_table(self):
        for i in range(0, self.rowCount()):
            if i not in self.model_c.temp_data:
                self.hideRow(i)
