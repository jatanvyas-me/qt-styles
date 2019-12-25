# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'styles.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("*{\n"
"background-color: rgb(44, 44, 44);\n"
"font: italic 12pt \"Monospace\";\n"
"}\n"
"\n"
".QPushButton {\n"
"background-color: rgb(190, 0, 0);\n"
"border-width:2px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton {\n"
"    background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
".QPushButton::hover {\n"
"background-color: rgb(85, 255, 255);\n"
"}\n"
"\n"
".QPushButton::pressed {\n"
"background-color: rgb(0, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 20, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 20, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Button 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Button 2"))
        self.pushButton_3.setText(_translate("MainWindow", "Button 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

