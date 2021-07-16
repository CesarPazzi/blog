# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def CreateNewHugoPost(self):
        inputText = self.TextEdit.text()
        PostName = inputText.replace(" ","-")
        PostNameIndex = "hugo new posts/" + PostName + "/index.md"

        #print(PostNameIndex)
        runHugo = os.system(PostNameIndex)
        e = "%d" % runHugo
        #print (e)
        if e == "0":
            self.label_2.setText("New post was created!")
        elif e == "-1":
            self.label_2.setText("ERROR, There's a post with the same name!")
        else:
            self.label_2.setText("Unknown error! Error code: " + e)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(296, 147)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.TextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TextEdit.setGeometry(QtCore.QRect(10, 30, 271, 20))
        self.TextEdit.setObjectName("TextEdit")
        self.TextEdit.returnPressed.connect(self.CreateNewHugoPost)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.CreateNewHugoPost)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 271, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create new Hugo post"))
        self.pushButton.setText(_translate("MainWindow", "Create Post"))
        self.label.setText(_translate("MainWindow", "Enter the name of your Hugo post:"))
        self.label_2.setText(_translate("MainWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
