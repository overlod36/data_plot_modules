from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, 
                             QMainWindow, QStyle, QVBoxLayout, QComboBox, 
                             QLineEdit, QHBoxLayout, QMessageBox, QScrollArea,
                             QLabel, QListWidget, QAbstractItemView)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPen, QColor, QBrush
import pyqtgraph as pg
import random
from data_module import data_handler
from math_module.qalgo import clusters_formation, eucl_dist

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()
    
    def initialize(self):
        self.input_data = data_handler.get_file_data()
        self.plot_data = []
        self.setWindowTitle('Кластеры')
        self.setFixedSize(QSize(500, 350))
        self.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))

        self.error_msgbox = QMessageBox()
        self.error_msgbox.setIcon(QMessageBox.Icon.Critical)
        self.error_msgbox.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxCritical))
        self.error_msgbox.setWindowTitle("Ошибка!")

        self.author_label = QLabel('Леонтьев Дмитрий Сергеевич')
        self.claster_count_input = QLineEdit()
        self.claster_count_input.setMaximumWidth(20)
        self.claster_count_label = QLabel('Число кластеров')
        self.signs_count_input = QLineEdit()
        self.signs_count_input.setMaximumWidth(20)
        self.signs_count_label = QLabel('Число признаков')
        self.x_choose_input = QLineEdit()
        self.x_choose_input.setMaximumWidth(20)
        self.y_choose_input = QLineEdit()
        self.y_choose_input.setMaximumWidth(20)
        self.x_choose_label = QLabel('Номер x')
        self.y_choose_label = QLabel('Номер y')
        self.headers_listwidget = QListWidget()
        self.headers_listwidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection) 
        for i, header in enumerate(self.input_data['headers']):  
            self.headers_listwidget.addItem(f'[{i}] {header}')
            
        self.headers_listwidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.headers_listwidget.setMinimumWidth(350)
        self.plot_button = QPushButton('Построение')
        self.plot_button.setFixedSize(100, 30)
        self.plot_button.setCheckable(True)
        self.plot_button.clicked.connect(self.plot_button_clicked)
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
    
    def plot_button_clicked(self):
        if self.claster_count_input.text() == '' or self.x_choose_input.text() == '' or self.y_choose_input.text() == '':
            self.error_msgbox.setText('Не все поля заполнены!')
            self.error_msgbox.exec()
        else:
            # проверка на число
            # и проверка на диапозон значений кол-ва признаков
            self.plot_data = []
            self.graphwidget.clear()
            cluster_count = int(self.claster_count_input.text())
            # signs_count = int(self.signs_count_input.text())
            x_sign = int(self.x_choose_input.text())
            y_sign = int(self.y_choose_input.text())
            self.graphwidget.setLabel('left', self.input_data['headers'][y_sign], units ='y')
            self.graphwidget.setLabel('bottom', self.input_data['headers'][x_sign], units ='x')
            
            for data_element in self.input_data['table_data']:
                if data_element[x_sign] and data_element[y_sign]:
                    self.plot_data.append([data_element[x_sign], data_element[y_sign], None])

            self.central_points = [random.randint(0, len(self.plot_data)-1) for _ in range(cluster_count)]
            self.result_central_points = [[point, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))] for point in clusters_formation(self.plot_data, self.central_points)]

            for point in self.plot_data:
                distations = [eucl_dist(self.plot_data[c_point[0]], point) for c_point in self.result_central_points]
                color = self.result_central_points[distations.index(min(distations))][1]
                sc = pg.ScatterPlotItem()
                sc.addPoints(x=[point[0]],y=[point[1]], pen=pg.mkPen(color=color, width=1), brush=pg.mkBrush(color=color))
                self.graphwidget.addItem(sc)
