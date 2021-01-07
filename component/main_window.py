from PySide2 import QtWidgets, QtGui, QtCore

from dataHandler.workspace.workspaceWidget import WorkspaceWidget

from component.structure_dock import StructureDock
from component.status_bar import StatusBar
from component.tool_bar import ToolBar
from component.menu_bar import MenuBar


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.resize(600, 480)
        self.setWindowTitle("Editor generickih podataka")
        self.setWindowIcon(QtGui.QIcon("../assets/img/icons8-edit-file-64.png"))

        self.workspace = WorkspaceWidget(self)

        # Dodat menu bar u svoju klasu i instanciran
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.structure_dock = StructureDock("Structure dock", self)

        self.toggle_structure_dock_action = self.structure_dock.toggleViewAction()
        self.menu_bar.view_menu.addAction(self.toggle_structure_dock_action)

        self.structure_dock.clicked.connect(self.workspace.open_file)

        # Dodat status bar u svoju klasu i instanciran
        self.status_bar = StatusBar()
        self.setStatusBar(self.status_bar)

        # Dodat tool bar u svoju klasu i  instanciran
        self.tool_bar = ToolBar()
        self.addToolBar(self.tool_bar)


        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.structure_dock)
        self.setCentralWidget(self.workspace)

        self.show()
