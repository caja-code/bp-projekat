import csv
from datetime import datetime

import PySide2
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont, QIcon

from cache.cache import write_log_data
from dataHandler.dataExtras.metadata import MetaData

from PySide2 import QtWidgets


BOLD = QFont()
BOLD.setBold(True)
PRIMARY_KEY_ICON = 'assets/img/primary-key.png'
FOREIGN_KEY_ICON = 'assets/img/foreign-key.png'
PRIMARY_FOREIGN_KEY = 'assets/img/primary_foreign_key.png'


# TODO: naprvit QtCore.QAbstractTableModel

class File:
    def __init__(self, path_c):  # path_c = Path 'Class'(path of file
        super().__init__()
        self.metadata_c = MetaData(path_c.get_metadata_path(), path_c)
        self.path_c = path_c
        self.data = []
        self.temp_data = []
        self.changes = {
            "is_saved": True,
            "changes_unsaved": 0,
            "changes_committed": [],
            "auto_save_on": 999
        }
        self.parse_data()

    def __getitem__(self, index):
        return self.data[0]

    def get_file_name(self):
        return self.path_c.get_file_name()

    def parse_data(self):
        try:
            data_file = open(self.path_c.path, 'r')

            reader = csv.DictReader(data_file,
                                    delimiter=self.metadata_c.metadata["dialect"]["delimiter"],
                                    fieldnames=self.metadata_c.get_headers_names(),
                                    quoting=self.metadata_c.metadata["dialect"]["quoting"])

            if self.metadata_c.metadata["dialect"]["skip_first_line"]:
                next(reader)

            for row in reader:
                self.data.append(row)

            data_file.close()
            del reader
        except:
            pass  # TODO: error slucaj ako dataExtras file ne postoji

    def write_data(self):
        if self.changes["is_saved"]:
            return
        # TODO: error
        with open(self.path_c.path, 'w') as file:
            # creating a csv writer object
            writer = csv.DictWriter(file,
                                    fieldnames=self.metadata_c.get_headers_names(),
                                    delimiter=self.metadata_c.metadata["dialect"]["delimiter"],
                                    quoting=self.metadata_c.metadata["dialect"]["quoting"])

            # writing the headersa
            # writer.writeheader()
            # writing the dataExtras rows
            writer.writerows(self.data)

        write_log_data(f'{datetime.now()} --- '
                       f'User **** saved file -'
                       f' changes saved : {self.changes["changes_unsaved"]} -'
                       f' file : {self.path_c.path} - '
                       f'changes saved: {self.create_change_log()}')

        self.changes["is_saved"] = True
        self.changes["changes_unsaved"] = 0

    def create_change_log(self):
        return ""

    # TODO  : pisanje podataka na kraju izvrsanja programa

    def get_element(self, index):
        return self.data[0]

    def row_count(self, parent: PySide2.QtCore.QModelIndex = None):
        return len(self.data)

    def column_count(self, parent: PySide2.QtCore.QModelIndex = None):
        return len(self.metadata_c.metadata["headers"])

    def horizontal_header_item(self, col):

        if col < 0 or col >= self.column_count():
            return False

        header_data = self.metadata_c.metadata['headers'][col]
        header = header_data["name"]

        header_item = QtWidgets.QTableWidgetItem(str(header))

        if header_data["is_primary"]:
            header_item.setIcon(QIcon(PRIMARY_KEY_ICON))
            header_item.setFlags(Qt.ItemIsSelectable)

        if header_data["is_foreign_key"]:
            header_item.setIcon(QIcon(FOREIGN_KEY_ICON))

        if header_data["is_primary"] and header_data["is_foreign_key"]:
            header_item.setIcon(QIcon(PRIMARY_FOREIGN_KEY))

        if header_data["not_null"]:
            header_item.setFont(BOLD)

        return header_item

    def set_data(self, row, col, value):
        if 0 > row or row >= self.row_count() or 0 > col or col >= self.column_count() and value != "":
            return False

        data_row = self.data[row]   # dobavljamo row za promenu
        header = self.metadata_c.metadata['headers'][col]["name"]

        changed_value = data_row[header]
        data_row[header] = value

        self.changes["is_saved"] = False
        self.changes["changes_unsaved"] = self.changes["changes_unsaved"] + 1
        change_txt = (f"{datetime.now()} ---  "
                      f" User changed file : {self.path_c.path} -"
                      f" for data at row  : {row} - "
                      f" changed ({header}) from '{changed_value}' to '{value}' -"
                      f" change saved : false")

        write_log_data(change_txt)
        self.changes["changes_committed"].append(change_txt)

        return True

    def delete(self, index):
        if not self.check_for_delete(index):  # provera da li je brisnje rowa moguce
            # TODO : ispisati korisniku da brisanje nije moguce
            return

        # dodavan je izmena u changes podatke
        self.changes["is_saved"] = False
        self.changes["changes_unsaved"] = self.changes["changes_unsaved"] + 1
        change_txt = (f"{datetime.now()} ---  "
                      f" User changed file : {self.path_c.path} -"
                      f" row [ {index} ] [{self.data[index]}] deleted - "
                      f" change saved : false")

        write_log_data(change_txt)
        self.changes["changes_committed"].append(change_txt)

        del self.data[index]  # brisnje rowa

    def check_for_delete(self, index):
        if not self.metadata_c.metadata["sequential_info"]["is_sequential"]:  # ako je podata serijski ne postoji razlog zasto bi zabranili brisanje
            return True

    def set_table_row(self, table, row):
        row_objet = self.data[row]
        headers = self.metadata_c.get_headers_names()

        for col in range(0, self.column_count()):
            value = row_objet[headers[col]]
            table.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))

    def find(self, txt):
        if type(txt) is not list:
            return self._find_txt(txt)
        else:
            return self._filter_foreign_key(txt)

    def _find_txt(self, txt):
        matches = []

        for index, value in enumerate(self.data):
            if txt in str(value):
                matches.append(index)

        return matches

    def _filter_foreign_key(self, relation_on_arr):
        # relation_on_arr izgleda
        # {
        #    "value_to_find": 1a,
        #     "find_in_col_name": "Ustanova"
        # }
        # {
        #    "value_to_find": 15,
        #     "find_in_col_name": Niov
        # }
        
        matches = []
        
        for index, row in enumerate(self.data):
            match = 0
            for relation in relation_on_arr:
                if row[relation["find_in_col_name"]] == relation["value_to_find"]:
                    match += 1

            if match == len(relation_on_arr):
                matches.append(index)

        # for index, row in enumerate(self.data):
        #     def inner():
        #         for relation in relation_on_arr:
        #             if row[relation["find_in_col_name"]] != relation["value_to_find"]:
        #                 return
        #         matches.append(index)
        #    inner()'''

        return matches

    def get_min(self, header_name):
        if len(self.data) <= 0:
            return False

        min_v = self.data[0][header_name]

        for row in self.data:
            if row[header_name] < min_v:
                min_v = row[header_name]

        return int(min_v)

    def get_max(self, header_name):
        if len(self.data) <= 0:
            return False

        max_v = self.data[0][header_name]

        for row in self.data:
            if row[header_name] > max_v:
                max_v = row[header_name]

        return int(max_v)

