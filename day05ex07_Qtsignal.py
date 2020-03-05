import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyQtSignalExam(QMainWindow):
    # 데이터가 없는 시그날 한계 생성

    closeApp=pyqtSignal()

    def __init__(self):
        super().__init__()
        self.closeApp.connect(self.close)

        self.setGeometry(100,100,290,150)
        self.setWindowTitle("email 시그널")
        self.show()

    #마우스를 누르면 closeApp 이벤트 발생
    def mousePressEvent(self, event):
        self.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyQtSignalExam()
    sys.exit(app.exec())