# pyqt5
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,300,600,400)
        self.setWindowTitle("Hello PyQt window")
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=HelloWindow()
    sys.exit(app.exec())


