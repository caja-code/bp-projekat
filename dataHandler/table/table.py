from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QAbstractItemView


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

    def displayMenu(self):
        ...#QMenu mini_menu(self)

    # TODO: Obrisati ako ne treba
    def get_title(self):
        return self.model_c.get_file_name()

    def on_change(self):
        changed_item = self.currentItem()

        if not self.model_c.set_data(changed_item.row(), changed_item.column(), changed_item.text()):
            ...
            # TODO: pop up widow sa ispisiavnjem greske da tabla nije uspesno promenjna

    def delete_row(self):
        row = self.currentRow()
        self.removeRow(row)

    def save(self):

        self.model_c.write_data()
