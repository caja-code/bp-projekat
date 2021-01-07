import csv

import PySide2
from PySide2 import QtCore
from dataHandler.dataExtras.metadata import MetaData
from PySide2 import QtWidgets


# TODO: naprvit QtCore.QAbstractTableModel

class File:
    def __init__(self, path_c):  # path_c = Path 'Class'(path of file
        super().__init__()
        self.metadata_c = MetaData(path_c.get_metadata_path(), path_c)
        self.path_c = path_c
        self.data = []
        self.temp_data = []
        self.parse_data()

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
            pass  # TODO: error slucaj ako dataExtras file ne postoji

    def write_data(self):
        # TODO: error
        with open(self.path_c.path, 'w') as file:
            # creating a csv writer object
            writer = csv.DictWriter(file,
                                    fieldnames=self.metadata_c.metadata["headers"],
                                    delimiter=self.metadata_c.metadata["delimiter"],
                                    quoting=self.metadata_c.metadata["quoting"])

            # writing the headersa
            writer.writeheader()

            # writing the dataExtras rows
            writer.writerows(self.data)

    # TODO  : pisanje podataka na kraju izvrsanja programa

    def get_element(self, index):
        return self.data[0]

    def row_count(self, parent: PySide2.QtCore.QModelIndex = None):
        return len(self.data)

    def column_count(self, parent: PySide2.QtCore.QModelIndex = None):
        return self.metadata_c.metadata["headers_count"]

    def set_data(self, row, col, value):
        if 0 > row or row >= self.row_count() or 0 > col or col >= self.column_count() and value != "":
            return False

        data_row = self.data[row]
        headers = self.metadata_c.metadata["headers"]

        data_row[headers[col]] = value

        return True

    def set_table_row(self, table, i):
        row_objet = self.data[i]
        headers = self.metadata_c.metadata["headers"]

        for j in range(0, self.column_count()):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(row_objet[headers[j]])))

    def find(self, txt, foreign_key_pos=None):
        if foreign_key_pos is None:
            return self._find_txt(txt)
        else:
            return self._filter_foreign_key(txt, foreign_key_pos)

    def _find_txt(self, txt):
        matches = []

        for index, value in enumerate(self.data):
            if txt in str(value):
                matches.append(index)

        return matches

    def _filter_foreign_key(self, foreign_id, foreign_key_pos):
        matches = []
        foreign_id = int(foreign_id)

        for index, value in enumerate(self.data):
            if foreign_id == int(value[foreign_key_pos]):
                matches.append(index)

        return matches
