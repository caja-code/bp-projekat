from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QAction, QPushButton, QToolButton

from dataHandler.dataExtras.file import File
from dataHandler.dataExtras.path import Path
from dataHandler.workspace.table.table import Table


class SequentialEditor(QtWidgets.QTabWidget):
    def __init__(self, parent, file_c, set_model=False):
        super().__init__(parent)
        self.model_c = file_c
        self.tool_bar = self.parent().parent().tool_bar.editor_tool_bar

        self.main_layout = QtWidgets.QVBoxLayout()  # postavljanje main lyouta koji

        self.foreign_table_tabs = QtWidgets.QTabWidget(self)  # pravljenje widgeta koji sadrzi child tabele

        self.main_table = Table(self, file_c, set_model)  # glavan tabela
        self.main_table.itemClicked.connect(self.find_relation)

        for foreign_table_path in self.model_c.metadata_c.metadata["sequential_info"]["child_relation"]:
            foreign_file_c = File(Path(foreign_table_path["path_of_child_table"]))
            self.foreign_table_tabs.addTab(Table(self.foreign_table_tabs, foreign_file_c, set_model),
                                           foreign_file_c.get_file_name())

        self.main_layout.addWidget(self.main_table)
        self.main_layout.addWidget(self.foreign_table_tabs)

        self.setLayout(self.main_layout)

        #self.create_my_tool_bar()

    def set_model(self, file_c=False):
        if file_c:
            self.model_c = file_c

        self.main_table.setModel(self.model_c)

        for i in range(0, len(self.model_c.metadata_c.metadata["sequential_info"]["child_relation"])):
            self.foreign_table_tabs.widget(i).setModel()

    def check_path(self, file_path):
        return self.model_c.path_c.is_same(file_path)


    def save(self):
        self.main_table.save()

        for i in range(0, self.foreign_table_tabs.count()):
            self.foreign_table_tabs.widget(i).save()

    def find(self, txt=None):
        if txt is None:
            print("nema txt :((((")
            # TODO: open input widget
        self.main_table.find(txt)

        for i in range(0, self.foreign_table_tabs.count()):
            self.foreign_table_tabs.widget(i).find(txt)

    def find_relation(self, item):  # item je selekrovani row koji sadrzi index

        for i in range(0, self.foreign_table_tabs.count()):
            relation_info = self.model_c.metadata_c.metadata["sequential_info"]["child_relation"][i]
            # relation_info sada izgleda u py dict formatu
            # {
            #                 "name_of_relation": "Studiranje",
            #                 "name_of_child_table": "studenti.csv",
            #                 "path_of_child_table": "data/studenti.csv",
            #                 "relation_on": [
            #                     {
            #                         "this_table_key": "Student iz ustanove",
            #                         "child_table_key": "Ustanova"
            #                     },
            #                     {
            #                         "this_table_key": "Struka",
            #                         "child_table_key": "Struka"
            #                     },
            #                     {
            #                         "this_table_key": "Broj indexa",
            #                         "child_table_key": "Broj indexa"
            #                     }
            #                 ]
            #             }

            relations = []

            for relation in relation_info["relation_on"]:
                relations.append({
                    "value_to_find": self.main_table.get_value(item.row(), relation["this_table_key"]),
                    "find_in_col_name": relation["child_table_key"]
                })

            self.foreign_table_tabs.widget(i).find(relations)

    def reset_tables(self):
        self.main_table.find('')

        for i in range(0, self.foreign_table_tabs.count()):
            self.foreign_table_tabs.widget(i).find('')

    def print_my(self, txt):
        print(txt.text)

    def open_child(self, path=None):
        #print(type(self.parent().parent().parent()))
        self.parent().parent().parent().open_file(path)

    def open_parent(self, path):
        self.parent().parent().parent().open_file(path)

    def create_my_tool_bar(self):
        self.tool_bar.reset({
            "title": self.model_c.path_c,
            "visible": True,
            "tools": {
                "options": [
                    {
                        "name": "",
                        "icon": "assets/img/save.jpg",
                        "callback": self.save,
                        "status_tip": f'Save changes on file {self.model_c.path_c.get_file_name()} .'
                    }
                ],
                "child": {
                    "child_relations": self.model_c.metadata_c.metadata["sequential_info"]["child_relation"],
                    "callback": self.open_child
                },
                "parent": {
                    "parent_relations": self.model_c.metadata_c.metadata["sequential_info"]["parent_relation"],
                    "callback": self.open_parent
                },
            }
        })
