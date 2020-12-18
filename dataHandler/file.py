import csv

import PySide2
from PySide2 import QtCore
from dataHandler.metadata import MetaData
from PySide2 import QtWidgets


# from dataHandler.path import Path


class File(QtCore.QAbstractTableModel):
    def __init__(self, path_c):  # metadata={}, data={}):
        # path_c = Path 'Class'(path of file
        super().__init__()
        self.metadata_c = MetaData(path_c.get_metadata_path(), path_c)
        self.path_c = path_c
        self.data = []
        self.parse_data()
        # print(self.data)

    def __getitem__(self, index):
        return self.data[0]

    def get_file_name(self):
        return self.path_c.get_file_name()

    def parse_data(self):
        try:
            data_file = open(self.path_c.path, 'r')

            reader = csv.DictReader(data_file,
                                    # dialect=self.metadata_c.metadata['dialect']
                                    delimiter=self.metadata_c.metadata['delimiter'],
                                    fieldnames=self.metadata_c.metadata["headers"],
                                    quoting=self.metadata_c.metadata["quoting"])

            if self.metadata_c.metadata["skip_first_line"]:
                next(reader)

            for row in reader:
                self.data.append(row)

            data_file.close()
            del reader
        except:
            pass  # TODO: error slucaj ako data file ne postoji

    def get_element(self, index):
        return self.data[0]

    def rowCount(self, parent: PySide2.QtCore.QModelIndex = None):
        return len(self.data)

    def columnCount(self, parent: PySide2.QtCore.QModelIndex = None):
        return self.metadata_c.metadata["headers_count"]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        # TODO: dodati obradu uloga (role)
        data_row = self.data[index]  # self[index]
        headers = self.metadata_c.metadata["headers"]

        if 0 <= index < self.columnCount and role == QtCore.Qt.DisplayRole:
            return data_row.headers[index]

        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if 0 <= section < self.columnCount() and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.metadata_c.metadata["headers"][section]
        return None

    # metode za editable model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        data_row = self.data[index]
        headers = self.metadata_c.metadata["headers"]

        if 0 >= index < self.columnCount and value != "":
            data_row[headers[index]] = value
            return True

        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable  # ili nad bitovima

    def set_table_row(self, table, i):
        row_objet = self.data[i]
        headers = self.metadata_c.metadata["headers"]
        for j in range(0, self.columnCount()):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(row_objet[headers[j]])))
