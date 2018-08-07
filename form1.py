# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import bk_store
import sqlite3
import main_prog
import os
from form2 import Ui_Form

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 353)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 80, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.t1.setObjectName("t1")
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setGeometry(QtCore.QRect(110, 200, 113, 20))
        self.t2.setObjectName("t2")
        #my add
        self.t2.setValidator(QtGui.QIntValidator())
        
        self.f_book = QtWidgets.QPushButton(Form)
        self.f_book.setGeometry(QtCore.QRect(240, 80, 75, 23))
        self.f_book.setObjectName("f_book")

        self.f_book.clicked.connect(self.findbook)
        
        self.f_total = QtWidgets.QPushButton(Form)
        self.f_total.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.f_total.setObjectName("f_total")

        self.f_total.clicked.connect(self.Total_Amt)
        
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(120, 10, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.details = QtWidgets.QTextEdit(Form)
        self.details.setGeometry(QtCore.QRect(110, 120, 201, 31))
        self.details.setObjectName("details")
        self.b_price = QtWidgets.QTextEdit(Form)
        self.b_price.setGeometry(QtCore.QRect(110, 160, 104, 31))
        self.b_price.setObjectName("b_price")
        self.t_price = QtWidgets.QTextEdit(Form)
        self.t_price.setGeometry(QtCore.QRect(110, 240, 104, 31))
        self.t_price.setObjectName("t_price")

        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setGeometry(QtCore.QRect(240, 300, 75, 23))
        self.quit.setObjectName("quit")

        self.quit.clicked.connect(self.bclicked)
        
        self.insert = QtWidgets.QPushButton(Form)
        self.insert.setGeometry(QtCore.QRect(110, 300, 75, 23))
        self.insert.setObjectName("insert")
        
        self.insert.clicked.connect(self.openWindow)

        self.price=0.0
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def bclicked(self):
        os.system(cmd)
        QtCore.QCoreApplication.instance().quit()

    def findbook(self):
        if self.t1.text()=="":
            self.details.setText(str(" Enter The Title of a Book !!!"))
        else:
            #print(self.t1.text()) 
            try:
                Book=main_prog.search(self.t1.text())
                #print(price)
                res=0
                auth=""
                titl=""
                prc=0.0
                for each in Book:
                    print(each)
                    res+=1
                    if res==1:
                        titl=each
                    elif res==2:
                        auth=each
                    else:
                        prc=each
                        self.price=prc
                self.details.setText(str("Title : {} ,Author : {} ".format(titl,auth)))
                self.b_price.setText(str("Rs. {}".format(prc)))
            except:
                self.details.setText(str("NOT AVAILABLE AT BOOK STORE !!!"))
                self.b_price.setText(str(" NA "))

    def Total_Amt(self):
           #print("lkxjvc")
           if self.t2.text()=="":
               self.t_price.setText("Please Enter Valid Quantity !!!")
           else:
               if self.b_price==" NA ":
                   self.t_price.setText("Total is : 0 ")
               else:
                   tot=float(self.t2.text())*float(self.price)
                   self.t_price.setText("Total is : {}".format(tot))
    def openWindow(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
            

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Book Title :"))
        self.label_2.setText(_translate("Form", "Price:"))
        self.f_book.setText(_translate("Form", "Find Book"))
        self.f_total.setText(_translate("Form", "Find Total"))
        self.label_4.setText(_translate("Form", "Quantity:"))
        self.label_5.setText(_translate("Form", "BOOK STORE"))
        self.label_6.setText(_translate("Form", "Price:"))
        self.quit.setText(_translate("Form", "Quit"))
        self.insert.setText(_translate("Form", "Add Book "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

