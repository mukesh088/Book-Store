# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import bk_store
import sqlite3
import main_prog
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 60, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 100, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 140, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.AddBook)
        
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 230, 181, 51))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 10, 101, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def AddBook(self):
        print((self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text()))
        if self.lineEdit.text()=="" or self.lineEdit_2.text()=="" or self.lineEdit_3.text()=="":
            self.textEdit.setText(" Enter Valid Details !! ")
        else:
            try:
                print((str(self.lineEdit.text()),str(self.lineEdit_2.text()),float(self.lineEdit_3.text())))
                tit=str(self.lineEdit.text())
                authr=str(self.lineEdit_2.text())
                pr=float(self.lineEdit_3.text())
                
                bk_store.insert(tit,authr,pr)
                
                self.textEdit.setText(" Succesfully Added !! ")
            except:
                self.textEdit.setText(" Error Occured !!")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Title"))
        self.label_2.setText(_translate("Form", "Author"))
        self.label_3.setText(_translate("Form", "Price"))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.label_4.setText(_translate("Form", "ADD BOOK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

