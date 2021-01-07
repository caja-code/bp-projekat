from PySide2 import QtWidgets, QtCore


class StatusBar(QtWidgets.QStatusBar):
    def __init__(self):
        super().__init__()
        self.showMessage("Status bar je prikazan!")
