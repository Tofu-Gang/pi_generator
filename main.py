__author__ = 'Tofu Gang'

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == "__main__":
    app = QApplication(argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    w.setWindowTitle('Hello World')
    w.show()
    exit(app.exec_())