from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtGui import QFont


WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450
FONT_SIZE_TITLE = 22

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Subtitle Translator")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # Add GUI elements here
        title_label = QLabel("Subtitle Translator", self)
        # title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", FONT_SIZE_TITLE))
        title_label.setGeometry(0, 0, WINDOW_WIDTH, 30)

        file_table = QTableWidget(self)
        file_table.setGeometry(0, 30, WINDOW_WIDTH, 300)
        file_table.setColumnCount(2)
        file_table.setHorizontalHeaderLabels(["Filename", "Status"])
        file_table.setShowGrid(True)

        def add_file_to_list(filename):
            row_position = file_table.rowCount()
            file_table.insertRow(row_position)
            file_table.setItem(row_position, 0, QTableWidgetItem(filename))
            file_table.setItem(row_position, 1, QTableWidgetItem("untranslated"))
        
        file_table.viewport().installEventFilter(self)

        file_list_widget.dropEvent = lambda event: handle_file_drop([url.toLocalFile() for url in event.mimeData().urls()])
        file_list_widget.setAcceptDrops(True)

        def handle_file_drop(file_paths):
            print("Files dropped:", file_paths)
            for file_path in file_paths:
                add_file_to_list(file_path)
        
        def eventFilter(source, event):
            if (event.type() == QEvent.DragEnter or
                event.type() == QEvent.Drop) and event.mimeData().hasUrls():
                event.acceptProposedAction()
                if event.type() == QEvent.Drop:
                    for url in event.mimeData().urls():
                        add_file_to_list(url.toLocalFile())
            else:
                event.ignore()
            return True
        
        def start_translation(self):
            for row in range(file_table.rowCount()):
                filename = file_table.item(row, 0).text()
                # Translate the file here
                file_table.setItem(row, 1, QTableWidgetItem("translated"))

        start_button = QPushButton("Start", self)
        start_button.setGeometry(0, 330, WINDOW_WIDTH, 30)
        start_button.clicked.connect(start_translation)
        
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()



