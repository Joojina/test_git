import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget


class LayoutExample2(QMainWindow):
    def __init__(self):
        super().__init__()


        # 위젯 생성

        lbl1=QLabel("My country name is")
        lbl2=QLabel("Korea~")
        okBtn=QPushButton("OK")
        cancelBtn=QPushButton("Cancel")

        # 레이아웃 생성
        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okBtn)
        hbox.addLayout(cancelBtn)

        vbox=QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(lbl2)
        vbox.addWidget(hbox)

        win=QWidget()
        win.setLayout(vbox)
        self.setCentralWidget(win)

        self.setGeometry(100,100,300,150)
        self.setWindowTitle("Layout example2")
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=LayoutExample2()
    sys.exit(app.exec())