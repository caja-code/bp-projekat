from PySide2 import QtWidgets
from dataHandler.dataExtras.file import File
from dataHandler.dataExtras.path import Path
from dataHandler.workspace.table.table import Table


class SequentialEditor(QtWidgets.QTabWidget):
    def __init__(self, parent, file_c, set_model=False):
        self.model_c = file_c
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout()                 # postavljanje main lyouta koji

        self.foreign_table_tabs = QtWidgets.QTabWidget(self)      # pravljenje widgeta koji sadrzi child tabele

        self.main_table = Table(self, file_c, set_model)            # glavan tabela
        self.main_table.itemClicked.connect(self.row_selected)

        for foreign_table_path in self.model_c.metadata_c.metadata["seq"]["foreign_tables"]:
            foreign_file_c = File(Path(foreign_table_path))
            self.foreign_table_tabs.addTab(Table(self.foreign_table_tabs, foreign_file_c, set_model), foreign_file_c.get_file_name())

        self.main_layout.addWidget(self.main_table)
        self.main_layout.addWidget(self.foreign_table_tabs)

        self.setLayout(self.main_layout)

    def set_model(self, file_c=False):
        if file_c:
            self.model_c = file_c

        self.main_table.setModel(self.model_c)

        for i in range(0, len(self.model_c.metadata_c.metadata["seq"]["foreign_tables"])):
            self.foreign_table_tabs.widget(i).setModel()

    def check_path(self, file_path):
        return self.model_c.path_c.path == file_path

    def save(self):
        self.main_table.save()

        for i in range(0, self.foreign_table_tabs.count()):
            self.foreign_table_tabs.widget(i).save()

    def find(self, txt):
        self.main_table.find(txt)

        for i in range(0, self.foreign_table_tabs.count()):
            self.foreign_table_tabs.widget(i).find(txt)

    def row_selected(self, item):
        pos = self.model_c.metadata_c.metadata["headers"].index(self.model_c.metadata_c.metadata["seq"]["foreign_key_pos"])
        object_id = self.main_table.item(item.row(), pos).text()
        self.filter_foreign_tables(object_id)

    def filter_foreign_tables(self, object_id):
        for i in range(0, self.foreign_table_tabs.count()):
            self.foreign_table_tabs.widget(i).find(object_id, self.model_c.metadata_c.metadata["seq"]["foreign_key_pos"])

    def reset_tables(self):
        self.main_table.find('')

        for i in range(0, self.foreign_table_tabs.count()):
            self.foreign_table_tabs.widget(i).find('')
