from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem


class FileListTable(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QTableWidget.DragDropMode.InternalMove)

        # Set event filter to handle drop events
        # self.installEventFilter(DropEventFilter())

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            for url in urls:
                filename = url.toLocalFile()
                row_count = self.rowCount()
                self.insertRow(row_count)
                self.setItem(row_count, 0, QTableWidgetItem(filename))
