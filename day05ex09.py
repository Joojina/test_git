# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day05ex09.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 160, 64, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 190, 64, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 220, 64, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 250, 64, 15))
        self.label_4.setObjectName("label_4")

        self.input_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_id.setGeometry(QtCore.QRect(210, 160, 113, 21))
        self.input_id.setObjectName("input_id")
        self.input_contact = QtWidgets.QLineEdit(self.centralwidget)
        self.input_contact.setGeometry(QtCore.QRect(210, 190, 113, 21))
        self.input_contact.setObjectName("input_contact")
        self.input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(210, 220, 113, 21))
        self.input_name.setObjectName("input_name")
        self.input_addr = QtWidgets.QLineEdit(self.centralwidget)
        self.input_addr.setGeometry(QtCore.QRect(210, 250, 113, 21))
        self.input_addr.setObjectName("input_addr")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(360, 160, 104, 87))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 300, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnHandler)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # end of setupUi
    def btnHandler(self):
        print("버튼 눌렀다!!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "아이디"))
        self.label_2.setText(_translate("MainWindow", "연락처"))
        self.label_3.setText(_translate("MainWindow", "성명"))
        self.label_4.setText(_translate("MainWindow", "주소"))
        self.pushButton.setText(_translate("MainWindow", "입력"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
