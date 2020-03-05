import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QTextEdit, QPushButton, QGridLayout, QWidget
from PyQt5.QtWidgets.QGridLayout import setSpacing


class GridLayoutExam(QMainWindow):
    def __init__(self):
        super().__init__()


        # 위젯 생성
        title=QLabel("title")
        writer=QLabel("Writer")
        comment=QLabel("Coments")
        titleEdit=QLineEdit()
        writerEdit=QLineEdit()
        commentEdit=QTextEdit()

        confirm=QPushButton('Confirm')

        # 레이아웃
        grid=QGridLayout()
        grid=setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(writerEdit, 2, 0)
        grid.addWidget(title, 2, 1)

        grid.addWidget(comment, 3, 0)
        grid.addWidget(commentEdit, 3,1,4,1)
        grid.addWidget(confirm, 6, 0)



        # 레이아웃 붙이기
        win=QWidget()
        win.setLayout(grid)
        self.setCentralWidget(win)

        self.setGeometry(100,100,250,300)
        self.setWindowTitle("Review")
        self.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridLayoutExam()
    sys.exit(app.exec())