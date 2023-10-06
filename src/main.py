from PyQt6.QtWidgets import QApplication
from forms import Main_Window
from math_module.qalgo import clusters_formation
import random

if __name__ == '__main__':
    app = QApplication([])
    window = Main_Window()
    app.exec()
    # print(clusters_formation([[random.randint(0, 255), random.randint(0, 255), None] for _ in range(25)], [1, 2]))