# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sqare_calculate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets

#第一个界面（正方形）的类：
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 545)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 250, 241, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 90, 181, 101))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 241, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 200, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 340, 121, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 340, 261, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(380, 200, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(510, 200, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "计算面积！"))
        self.label.setText(_translate("Form", "正方形面积计算器"))
        self.label_2.setText(_translate("Form", "边长（请输入实数）："))
        self.label_3.setText(_translate("Form", "面积为(平方厘米)："))
        self.radioButton.setText(_translate("Form", "cm"))
        self.radioButton_2.setText(_translate("Form", "英寸"))

#菜单页面的类
class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 545)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 250, 241, 28))
        self.pushButton.setObjectName("pushButton")


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 90, 181, 101))
        self.label.setObjectName("label")

        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(230, 300, 241, 28))
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 250, 241, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 300, 241, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.pushButton.setText(_translate("Form", "正方形"))
            self.pushButton_1.setText(_translate("Form", "长方形"))
            self.pushButton_2.setText(_translate("Form", "圆形"))
            self.pushButton_3.setText(_translate("Form", "三角形"))
            self.label.setText(_translate("Form", "请选择图形："))    #已修改

#正方形的处理函数
def convert(ui):
    input_1 = ui.lineEdit.text()  #这个地方出来问题，不能读入数据了.唯一的可能就在与存在两个窗口出现了问题。
    if input_1=='':
        result="请输入数据！"
    elif ui.radioButton.isChecked()==True:
        result = float(input_1)
        result=1*result*result
    elif ui.radioButton_2.isChecked()==True:
        result = float(input_1)
        result=2.54*2.54*result*result
    else:
        result='请选择单位！'
    ui.lineEdit_3.setText(str(result))

#主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 菜单界面
    MenuWindow = QMainWindow()
    ui0 = Ui_Form2()
    ui0.setupUi(MenuWindow)
    MenuWindow.show()

    #第一个界面
    MainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(partial(convert, ui))

    #第二个界面
    SecWindow = QMainWindow()
    ui2 = Ui_Form()
    ui2.setupUi(SecWindow)
    ui2.pushButton.clicked.connect(partial(convert, ui2))

    #翻页操作
    ui0.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui0.pushButton_1.clicked.connect(partial(SecWindow.show, ))

    # 因为这个是退出，所以必须把代码放在这个之前。不然就会显示出无效的提示。
    sys.exit(app.exec_())