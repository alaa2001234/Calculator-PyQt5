from PyQt5 import QtCore, QtGui, QtWidgets
from Main import Ui_MainWindow

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
cheek = True
ans = None


def zero ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "0")
    if not cheek : 
          ui.lineEdit.setText("0")
    cheek=True

def one ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "1")
    if not cheek : 
          ui.lineEdit.setText("1")
    cheek=True


def two ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "2")
    if not cheek : 
          ui.lineEdit.setText("2")
    cheek=True

def three ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "3")
    if not cheek : 
          ui.lineEdit.setText("3")
    cheek=True

def four ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "4")
    if not cheek : 
          ui.lineEdit.setText("4")
    cheek=True

def five ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "5")
    if not cheek : 
          ui.lineEdit.setText("5")
    cheek=True

def six ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "6")
    if not cheek : 
          ui.lineEdit.setText("6")
    cheek=True

def seven ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "7")
    if not cheek : 
          ui.lineEdit.setText("7")
    cheek=True

def eight ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "8")
    if not cheek : 
          ui.lineEdit.setText("8")
    cheek=True

def nine ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "9")
    if not cheek : 
          ui.lineEdit.setText("9")
    cheek=True

def left_bracket ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + "(")
    if not cheek : 
          ui.lineEdit.setText("(")
    cheek=True

def right_bracket ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + ")")
    if not cheek : 
          ui.lineEdit.setText(")")
    cheek=True

def plus ():
    global cheek
    ui.lineEdit.setText(ui.lineEdit.text() + "+")
    cheek=True


def minus ():
    global cheek
    ui.lineEdit.setText(ui.lineEdit.text() + "-")
    cheek=True


def multiply ():
    global cheek
    ui.lineEdit.setText(ui.lineEdit.text() + "*")
    cheek=True

def divide ():
    global cheek
    ui.lineEdit.setText(ui.lineEdit.text() + "/")
    cheek=True

def dot ():
    global cheek
    if cheek : 
        ui.lineEdit.setText(ui.lineEdit.text() + ".")
    if not cheek : 
        ui.lineEdit.setText(".")
    cheek=True

def clear ():
    global cheek
    ui.lineEdit.clear()
    cheek = True

def delate ():
    global cheek
    ui.lineEdit.setText(ui.lineEdit.text()[0:-1])
    cheek = True
    
def ans1 ():
    if ans is not None:
        ui.lineEdit.setText(ui.lineEdit.text()+str(ans))
    else:
        pass
  
    

def equal ():
    global cheek
    global ans
    try:
         ui.lineEdit.setText(str(eval(ui.lineEdit.text())))
         ans =ui.lineEdit.text()
    except ZeroDivisionError : 
         ui.lineEdit.setText("Can not by division zero")
    except SyntaxError  : 
         ui.lineEdit.setText("Invalid Syntax")
    except  : 
         ui.lineEdit.setText("Error")

    cheek = False


ui.pushButton_23.clicked.connect(right_bracket)
ui.pushButton_22.clicked.connect(left_bracket)
ui.pushButton_21.clicked.connect(clear)
ui.pushButton_20.clicked.connect(delate)
ui.pushButton_17.clicked.connect(equal)
ui.pushButton_12.clicked.connect(dot)
ui.pushButton_13.clicked.connect(ans1)
ui.pushButton_11.clicked.connect(zero)
ui.pushButton_2.clicked.connect(one)
ui.pushButton_3.clicked.connect(two)
ui.pushButton_4.clicked.connect(three)
ui.pushButton_7.clicked.connect(four)
ui.pushButton_5.clicked.connect(five)
ui.pushButton_6.clicked.connect(six)
ui.pushButton_10.clicked.connect(seven)
ui.pushButton_8.clicked.connect(eight)
ui.pushButton_9.clicked.connect(nine)
ui.pushButton_18.clicked.connect(multiply)
ui.pushButton_19.clicked.connect(divide)
ui.pushButton_16.clicked.connect(plus)
ui.pushButton_15.clicked.connect(minus)






sys.exit(app.exec_())
