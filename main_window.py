
from PySide2 import  QtWidgets, QtGui, QtCore
from workspaceWidget import WorkspaceWidget
from structure_dock import StructureDock


class MainWindow(QtWidgets.QMainWindow):
    #Glavni window

    def __init__(self):
        super().__init__()
        #self = QtWidgets.QMainWindow()
        self.resize(600,480)
        self.setWindowTitle("Editor generickih podataka")
        self.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))
        
        #TODO za Iliju: dodati main bar u svoju posebu klasu
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.file_menu = QtWidgets.QMenu("File",self.menu_bar)
        self.edit_menu = QtWidgets.QMenu("Edit",self.menu_bar)
        self.view_menu = QtWidgets.QMenu("View",self.menu_bar)
        self.help_menu = QtWidgets.QMenu("Help",self.menu_bar)

        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.edit_menu)
        self.menu_bar.addMenu(self.view_menu)
        self.menu_bar.addMenu(self.help_menu)
        


        # TODO za Iliju: dodati tool bar bar u svoju posebu klasu
        self.tool_bar = QtWidgets.QToolBar(self)

        self.central_widget = QtWidgets.QTabWidget(self)
        #text_edit = QtWidgets.QTextEdit(central_widget)
        #central_widget.addTab(text_edit, QtGui.QIcon("icons8-edit-file-64.png"), "Tekstualni editor")
        self.workspace = WorkspaceWidget(self.central_widget)
        self.central_widget.addTab(self.workspace, QtGui.QIcon("icons8-edit-file-64.png"), "Prikaz tabele")
        
        #TODO za Iliju: dodati structure dok u svoju posebu klasu
        #structure_dock = QtWidgets.QDockWidget("Structure dock", main_window)
        
        self.structure_dock = StructureDock("Structure dock", self)
        
        self.toggle_structure_dock_action = self.structure_dock.toggleViewAction()
        self.view_menu.addAction(self.toggle_structure_dock_action)
        
        self.structure_dock.clicked.connect(self.workspace.open_file)
        
        # TODO za Iliju: dodati stastus bar u svoju posebu klasu
        
        self.status_bar = QtWidgets.QStatusBar(self)
        self.status_bar.showMessage("Status bar je prikazan!")
    
        self.central_widget.setTabsClosable(True)

        self.addToolBar(self.tool_bar)
        
        self.setMenuBar(self.menu_bar)
        self._createMenuBar()
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea,self.structure_dock)
        self.setCentralWidget(self.central_widget)
        
        self.setStatusBar(self.status_bar)
        self.show()
        # menu_bar.setParent(main_window)
