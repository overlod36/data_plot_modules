from PyQt6.QtWidgets import QApplication
from forms import Main_Window

if __name__ == '__main__':
    app = QApplication([])
    window = Main_Window()
    app.exec()