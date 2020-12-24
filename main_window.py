
from PySide2 import  QtWidgets, QtGui, QtCore
from workspaceWidget import WorkspaceWidget
from structure_dock import StructureDock

from status_bar import StatusBar
from tool_bar import ToolBar
from menu_bar import MenuBar


class MainWindow(QtWidgets.QMainWindow):
    #Glavni window

    def __init__(self):
        super().__init__()
        #self = QtWidgets.QMainWindow()
        self.resize(600, 480)
        self.setWindowTitle("Editor generickih podataka")
        self.setWindowIcon(QtGui.QIcon("slike/icons8-edit-file-64.png"))
       
    
        self.central_widget = QtWidgets.QTabWidget(self)
       
        self.workspace = WorkspaceWidget(self.central_widget)
        self.central_widget.addTab(self.workspace, QtGui.QIcon("slike/icons8-edit-file-64.png"), "Prikaz tabele")
        
        # Dodat menu bar u svoju klasu i instanciran
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        
        #structure_dock = QtWidgets.QDockWidget("Structure dock", main_window)
        
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


        self.central_widget.setTabsClosable(True)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.structure_dock)
        self.setCentralWidget(self.central_widget)

        
        self.show()
        

