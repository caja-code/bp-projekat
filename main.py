import sys
from PySide2 import QtWidgets, QtGui, QtCore

from workspaceWidget import WorkspaceWidget
from structure_dock import StructureDock


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(640, 480)
    main_window.setWindowTitle("Editor generickih podataka")
    main_window.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))

    #TODO za Iliju: dodati main bar u svoju posebu klasu
    menu_bar = QtWidgets.QMenuBar(main_window)
    file_menu = QtWidgets.QMenu("File", menu_bar)
    edit_menu = QtWidgets.QMenu("Edit", menu_bar)
    view_menu = QtWidgets.QMenu("View", menu_bar)
    help_menu = QtWidgets.QMenu("Help", menu_bar)

    menu_bar.addMenu(file_menu)
    menu_bar.addMenu(edit_menu)
    menu_bar.addMenu(view_menu)
    menu_bar.addMenu(help_menu)

    # TODO za Iliju: dodati tool bar bar u svoju posebu klasu
    tool_bar = QtWidgets.QToolBar(main_window)

    central_widget = QtWidgets.QTabWidget(main_window)
    #text_edit = QtWidgets.QTextEdit(central_widget)
    #central_widget.addTab(text_edit, QtGui.QIcon("icons8-edit-file-64.png"), "Tekstualni editor")
    workspace = WorkspaceWidget(central_widget)
    central_widget.addTab(workspace, QtGui.QIcon("icons8-edit-file-64.png"), "Prikaz tabele")
    
    #TODO za Iliju: dodati structure dok u svoju posebu klasu
    #structure_dock = QtWidgets.QDockWidget("Structure dock", main_window)
    structure_dock = StructureDock("Structure dock", main_window)

    toggle_structure_dock_action = structure_dock.toggleViewAction()
    view_menu.addAction(toggle_structure_dock_action)
    structure_dock.clicked.connect(workspace.open_file)

    # TODO za Iliju: dodati stastus bar u svoju posebu klasu
    status_bar = QtWidgets.QStatusBar(main_window)
    status_bar.showMessage("Status bar je prikazan!")

    central_widget.setTabsClosable(True)

    main_window.setMenuBar(menu_bar)
    main_window.addToolBar(tool_bar)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, structure_dock)
    main_window.setCentralWidget(central_widget)
    main_window.setStatusBar(status_bar)
    main_window.show()
    # menu_bar.setParent(main_window)
    sys.exit(app.exec_())

