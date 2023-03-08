from PyQt6.QtCore import QObject, QEvent
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


class DropEventFilter(QObject):
    def eventFilter(self, obj, event):
        print("📢[eventFilter.py:6]: ", event)
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
                    # self.setItem(event.row(), event.column(), item)
                return True
        return super().eventFilter(obj, event)
