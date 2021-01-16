
from PySide2.QtWidgets import QStyledItemDelegate

#klasa koja blokira pristup tabele u svakom pokusaju prekine i izbaci komentar
class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self,parent,option,index):
        print("cant change table content")
        return

    