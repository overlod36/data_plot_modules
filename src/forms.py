from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, 
                             QMainWindow, QStyle, QVBoxLayout, QComboBox, 
                             QLineEdit, QHBoxLayout, QMessageBox, QScrollArea,
                             QLabel, QListWidget, QAbstractItemView)
from PyQt6.QtCore import QSize, Qt
import pyqtgraph as pg
from data_module import data_handler

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()
    
    def initialize(self):
        self.plot_data = data_handler.get_file_data()
        self.setWindowTitle('Кластеры')
        self.setFixedSize(QSize(500, 250))
        self.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))

        self.author_label = QLabel('Леонтьев Дмитрий Сергеевич')
        self.claster_count_input = QLineEdit()
        self.claster_count_input.setMaximumWidth(25)
        self.claster_count_label = QLabel('Число кластеров')
        self.signs_count_input = QLineEdit()
        self.signs_count_input.setMaximumWidth(25)
        self.signs_count_label = QLabel('Число признаков')
        self.x_choose_input = QLineEdit()
        self.x_choose_input.setMaximumWidth(20)
        self.y_choose_input = QLineEdit()
        self.y_choose_input.setMaximumWidth(20)
        self.x_choose_label = QLabel('Номер x')
        self.y_choose_label = QLabel('Номер y')
        self.headers_listwidget = QListWidget()
        self.headers_listwidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection) 
        for i, header in enumerate(self.plot_data['headers']):    
            self.headers_listwidget.addItem(f'[{i}] {header}')
        self.headers_listwidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.headers_listwidget.setMinimumWidth(350)
        self.plot_button = QPushButton('Построение')
        self.plot_button.setFixedSize(100, 30)
        self.graphwidget = pg.PlotWidget()
        self.graphwidget.setBackground('w')
        self.graphwidget.plot([i for i in range(1, 10)], [i for i in range(1, 10)], pen=pg.mkPen(color=(255, 0, 0)))

        self.name_layout = QHBoxLayout()
        self.name_layout.addWidget(self.author_label, alignment=Qt.AlignmentFlag.AlignRight)
        self.name_layout.setContentsMargins(0, 5, 5, 0)

        self.claster_count_input_layout = QHBoxLayout()
        self.claster_count_input_layout.addStretch()
        self.claster_count_input_layout.addWidget(self.claster_count_label)
        self.claster_count_input_layout.addWidget(self.claster_count_input)

        self.signs_count_input_layout = QHBoxLayout()
        self.signs_count_input_layout.addStretch()
        self.signs_count_input_layout.addWidget(self.signs_count_label)
        self.signs_count_input_layout.addWidget(self.signs_count_input)

        self.x_choose_input_layout = QHBoxLayout()
        self.x_choose_input_layout.addStretch()
        self.x_choose_input_layout.addWidget(self.x_choose_label)
        self.x_choose_input_layout.addWidget(self.x_choose_input)

        self.y_choose_input_layout = QHBoxLayout()
        self.y_choose_input_layout.addStretch()
        self.y_choose_input_layout.addWidget(self.y_choose_label)
        self.y_choose_input_layout.addWidget(self.y_choose_input)

        self.inputs_layout = QVBoxLayout()
        self.inputs_layout.setContentsMargins(0, 15, 10, 0)
        self.inputs_layout.addLayout(self.signs_count_input_layout)
        self.inputs_layout.addLayout(self.claster_count_input_layout)
        self.inputs_layout.addLayout(self.x_choose_input_layout)
        self.inputs_layout.addLayout(self.y_choose_input_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(0, 15, 10, 0)
        self.buttons_layout.addWidget(self.plot_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.control_layout = QVBoxLayout()
        self.control_layout.addLayout(self.name_layout)
        self.control_layout.addLayout(self.inputs_layout)
        self.control_layout.addLayout(self.buttons_layout)
        self.control_layout.addStretch()

        self.graph_layout = QHBoxLayout()
        self.graph_layout.addWidget(self.graphwidget)
        self.selection_layout = QHBoxLayout()
        self.selection_layout.addWidget(self.headers_listwidget)

        self.data_layout = QVBoxLayout()
        self.data_layout.addLayout(self.graph_layout)
        self.data_layout.addLayout(self.selection_layout)

        self.main_layout= QHBoxLayout()
        self.main_layout.addLayout(self.data_layout)
        self.main_layout.addLayout(self.control_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        self.show()