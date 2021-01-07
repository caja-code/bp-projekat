from PySide2 import QtWidgets
from dataHandler.dataExtras.file import File
from dataHandler.dataExtras.path import Path
from dataHandler.workspace.table.table import Table
from dataHandler.workspace.sequental_editor import SequentialEditor


class WorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_tab_widget = None

        self.create_main_tab_widget()

        self.main_layout.addWidget(self.main_tab_widget)

        self.setLayout(self.main_layout)

    def create_main_tab_widget(self):
        self.main_tab_widget = QtWidgets.QTabWidget(self)
        self.main_tab_widget.setTabsClosable(True)
        self.main_tab_widget.tabCloseRequested.connect(self.delete_tab)
        # self.show_tabs()

    def delete_tab(self, index):
        self.main_tab_widget.removeTab(index)

    def save(self):
        # TODO: popo up error ako nema otvorernih fajlova
        if self.main_tab_widget.count() > 0:
            self.main_tab_widget.currentWidget().save()
            self.parent().setStatusTip("Fajl je sacuavn")

    def find(self, parm):
        txt, _ = parm
        if self.main_tab_widget.count() > 0:
            self.main_tab_widget.currentWidget().find(txt)
            self.parent().setStatusTip("Nadjena su pogadjana")

    def reset_tables(self):
        if self.main_tab_widget.count() > 0:
            self.main_tab_widget.currentWidget().find('')

    def save_all(self, close=False):
        for i in range(0, self.main_tab_widget.count()):  # prolazimo kroz sve glavne tabove fajlova
            self.main_tab_widget.widget(i).save()

            if close:
                self.main_tab_widget.removeTab(i)

    def is_file_open(self, file_path):
        for i in range(0, self.main_tab_widget.count()):  # prolazimo kroz sve glavne tabove fajlova
            if self.main_tab_widget.widget(i).check_path(file_path):
                self.main_tab_widget.setCurrentWidget(self.main_tab_widget.widget(i))
                return True

    def open_file(self, file_path):
        if self.is_file_open(file_path):
            return
        path_c = Path(file_path)
        # TODO otvoriti dodatni window za path

        if path_c.get_extension() != "csv":
            # TODO: prekinuti program sa pop out window i obavestiti korisnika da moze da otvori samo csv fajl
            return

        file_c = File(path_c)

        if file_c.metadata_c.metadata["is_sequential"]:
            self.main_tab_widget.addTab(SequentialEditor(self, file_c, True), file_c.path_c.get_file_name_R())
        else:
            self.main_tab_widget.addTab(Table(self, file_c, True), file_c.path_c.get_file_name_R())
