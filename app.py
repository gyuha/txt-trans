import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDropEvent
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
from FileListTable import FileListTable


class SubtitleTranslator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Subtitle Translator")
        self.setGeometry(100, 100, 450, 450)

        # Title Label
        lb_title = QLabel(self)
        lb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lb_title.setStyleSheet("font-size: 22px;")
        lb_title.setText("Subtitle Translator")

        # File List Table
        self.tb_list = FileListTable(self)
        self.tb_list.setColumnCount(2)
        self.tb_list.setHorizontalHeaderLabels(["Filename", "Status"])
        self.tb_list.setStyleSheet("border: 1px solid black;")

        # Table Header
        self.hbox_header = QHBoxLayout()
        self.hbox_header.addWidget(self.tb_list)

        # Start Button
        self.btn_start = QPushButton(self)
        self.btn_start.setStyleSheet("background-color: lightblue; font-size: 22px;")
        self.btn_start.setText("Start")

        # Button Layout
        self.hbox_btn = QHBoxLayout()
        self.hbox_btn.addStretch()
        self.hbox_btn.addWidget(self.btn_start)

        # Main Layout
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(lb_title)
        self.vbox.addLayout(self.hbox_header)
        self.vbox.addLayout(self.hbox_btn)

        # Set main layout
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.vbox)
        self.setCentralWidget(self.central_widget)

        # Connect drag-and-drop events
        self.tb_list.setDragEnabled(True)
        self.tb_list.setAcceptDrops(True)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SubtitleTranslator()
    sys.exit(app.exec())