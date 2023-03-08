from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt6.QtCore import Qt, QMimeData, QByteArray, QDataStream, QIODevice, QEvent
from PyQt6.QtGui import QDrag
import sys

class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRowCount(3)
        self.setColumnCount(3)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.populate()
        self.installEventFilter(self)

    def populate(self):
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                item = QTableWidgetItem(f"Item {i}, {j}")
                self.setItem(i, j, item)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.DragEnter:
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
                return True
        elif event.type() == QEvent.Type.DragMove:
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
                return True
        elif event.type() == QEvent.Type.Drop:
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
                for url in event.mimeData().urls():
                    item = QTableWidgetItem(url.fileName())
                    self.setItem(event.row(), event.column(), item)
                return True
        return super().eventFilter(source, event)

    def startDrag(self, supportedActions):
        indexes = self.selectedIndexes()
        if len(indexes) > 0:
            data = QByteArray()
            stream = QDataStream(data, QIODevice.OpenMode.WriteOnly)
            for index in indexes:
                stream.writeInt32(index.row())
                stream.writeInt32(index.column())
                stream.writeInt32(index.data(Qt.ItemDataRole.DisplayRole))
            mimeData = QMimeData()
            mimeData.setData("application/x-qabstractitemmodeldatalist", data)
            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.exec(supportedActions)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = TableWidget()
    table.show()
    sys.exit(app.exec())