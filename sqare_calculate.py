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
import math

#第一个界面（正方形）的类：
class Ui_Form(object):
    """
    定义一个计算正方形面积的界面类
    """
    def setupUi(self, Form):
        """
        创建该界面，并创建以下的界面元素：
        pushButton 确认计算的按钮；
        label 该页面的标题显示；
        label_2 提示输入数据类型的显示；
        label_3 提示数据输出的显示；
        radioButton 选择计算单位为厘米；
        radioButton_2 选择计算单位为英寸；
        lineEdit 输入计算所需数据；
        lineEdit_3 输出计算结果；
        同时设置了该窗口的大小以及每个界面元素的大小尺寸        
        """
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
        """
        该函数为界面元素赋予新的命名显示
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "计算面积！"))
        self.label.setText(_translate("Form", "正方形面积计算器"))
        self.label_2.setText(_translate("Form", "边长（请输入正实数）："))
        self.label_3.setText(_translate("Form", "面积为(平方厘米)："))
        self.radioButton.setText(_translate("Form", "cm"))
        self.radioButton_2.setText(_translate("Form", "英寸"))

 # 第三个界面（圆形）的类：
class Ui_Form4(object):
    """
    定义一个计算正方形面积的窗口类
    """
    def setupUi(self, Form):
        """
        创建该界面，并创建以下的界面元素：
        pushButton 确认计算的按钮；
        label 该页面的标题显示；
        label_2 提示输入数据类型的显示；
        label_3 提示数据输出的显示；
        radioButton 选择计算单位为厘米；
        radioButton_2 选择计算单位为英寸；
        lineEdit 输入计算所需数据；
        lineEdit_3 输出计算结果；
        同时设置了该窗口的大小以及每个界面元素的大小尺寸；       
        """
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
        """
        该函数为界面元素赋予新的命名显示
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "计算面积！"))
        self.label.setText(_translate("Form", "圆形面积计算器"))
        self.label_2.setText(_translate("Form", "半径（请输入正实数）："))
        self.label_3.setText(_translate("Form", "面积为(平方厘米)："))
        self.radioButton.setText(_translate("Form", "cm"))
        self.radioButton_2.setText(_translate("Form", "英寸"))

#菜单页面的类
class Ui_Form2(object):
    """
    定义了一个初始菜单界面的类，用来显示需要选择哪个计算模式
    """
    def setupUi(self, Form):
        """
        创建该界面，并创建以下的界面元素：
        label 提示选择某种计算模式的标签；
        pushButton 选择计算正方形的面积；
        pushButton_1 选择计算长方形的面积；
        pushButton_2 选择计算圆形的面积；
        pushButton_3 选择计算三角形的面积；
        同时设置了该窗口的大小以及每个界面元素的大小尺寸
        """
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
            """
            该函数为界面元素赋予新的命名显示
            """
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.pushButton.setText(_translate("Form", "正方形"))
            self.pushButton_1.setText(_translate("Form", "长方形"))
            self.pushButton_2.setText(_translate("Form", "圆形"))
            self.pushButton_3.setText(_translate("Form", "三角形"))
            self.label.setText(_translate("Form", "请选择图形："))    #已修改

#第二个界面（长方形）的类：（form是3）
class Ui_Form3(object):
    """
    定义一个计算长方形面积的窗口类
    """
    def setupUi(self, Form):
        """
        创建该界面，并创建以下的界面元素：
        pushButton 确认计算的按钮；
        label 该页面的标题显示；
        label_2 提示输入长方形长边长度的显示；
        label_3 提示数据输出的显示；
        label_4 提示输入长方形宽边长度的显示；
        radioButton 选择计算单位为厘米；
        radioButton_2 选择计算单位为英寸；
        lineEdit 输入计算所需数据；
        lineEdit_2 输入计算所需数据；
        lineEdit_3 输出计算结果；
        同时设置了该窗口的大小以及每个界面元素的大小尺寸；       
        """
        Form.setObjectName("Form")
        Form.resize(721, 545)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 250, 241, 28))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 50, 181, 101))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 241, 31))
        self.label_2.setObjectName("label_2")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 241, 31))
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 200, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 150, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit")

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
        """
        该函数为界面元素赋予新的命名显示
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "计算面积！"))
        self.label.setText(_translate("Form", "长方形面积计算器"))
        self.label_2.setText(_translate("Form", "长为（请输入正实数）："))
        self.label_4.setText(_translate("Form", "宽为（请输入正实数）："))
        self.label_3.setText(_translate("Form", "面积为(平方厘米)："))
        self.radioButton.setText(_translate("Form", "cm"))
        self.radioButton_2.setText(_translate("Form", "英寸"))

#第四个界面（三角形）的类：
class Ui_Form5(object):
    """
    定义一个计算三角形面积的窗口类
    """
    def setupUi(self, Form):
        """
        创建该界面，并创建以下的界面元素：
        pushButton 确认计算的按钮；
        label 该页面的标题显示；
        label_2 提示输入三角形第三条边的显示；
        label_3 提示输入三角形第二条边的显示；
        label_4 提示输入三角形第一条边的显示；
        label_5 提示数据输出的显示；
        radioButton 选择计算单位为厘米；
        radioButton_2 选择计算单位为英寸；
        lineEdit 输入计算所需数据；
        lineEdit_2 输入计算所需数据；
        lineEdit_3 输出计算结果；
        lineEdit_4 输入计算所需数据；
        同时设置了该窗口的大小以及每个界面元素的大小尺寸；       
        """
        Form.setObjectName("Form")
        Form.resize(721, 545)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 250, 241, 28))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 30, 181, 101))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 241, 31))
        self.label_2.setObjectName("label_2")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 241, 31))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 100, 241, 31))
        self.label_5.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 200, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 150, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit")

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 100, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit")

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
        """
        该函数为界面元素赋予新的命名显示
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "计算面积！"))
        self.label.setText(_translate("Form", "三角形面积计算器"))
        self.label_2.setText(_translate("Form", "第三条边（请输入正实数）："))
        self.label_4.setText(_translate("Form", "第二条边（请输入正实数）："))
        self.label_5.setText(_translate("Form", "第一条边（请输入正实数）："))
        self.label_3.setText(_translate("Form", "面积为(平方厘米)："))
        self.radioButton.setText(_translate("Form", "cm"))
        self.radioButton_2.setText(_translate("Form", "英寸"))

#正方形的处理函数
def Square_convert(ui):
    """
    该函数主要判定参数输入是否合理，如果没有输入规定的数据或没有选择单位,
    则输出提示；如果选择数据均正确,则计算正方形面积,并将结果显示到lineEdit_3中
    """
    input_1 = ui.lineEdit.text()  #这个地方出来问题，不能读入数据了.唯一的可能就在与存在两个窗口出现了问题。
    if input_1==''or is_number(input_1)==0 or float(input_1)<0:
        result="请输入合理数据！"
    elif ui.radioButton.isChecked()==True:
        result = float(input_1)
        result=format(1*result*result,'.3f')
    elif ui.radioButton_2.isChecked()==True:
        result = float(input_1)
        result=format(2.54*2.54*result*result,'.3f')
    else:
        result='请选择单位！'
    ui.lineEdit_3.setText(str(result))

#长方形处理函数
def rectangle_convert(ui):
    """
    该函数主要判定参数输入是否合理，如果没有输入规定的数据或没有选择单位,
    则输出提示；如果选择数据均正确,则计算正方形面积,并将结果显示到lineEdit_3中
    """
    input_1=ui.lineEdit.text()
    input_2=ui.lineEdit_2.text()
    if input_1==''and input_2=='':
        result='请输入长和宽！'
    elif input_1==''and input_2!='':
        result="请输入长！"
    elif input_2==''and input_1!='':
        result="请输入宽！"
    elif is_number(input_1) == 0 or float(input_1) < 0 or is_number(input_2) == 0 or float(input_2) < 0:
            result = "请输入合理数据！"
    else:
        if ui.radioButton.isChecked()==True:
            input_1=float(input_1)
            input_2=float(input_2)
            result=format(1*input_2*input_1,'.3f')
        elif ui.radioButton_2.isChecked()==True:
            input_1 = float(input_1)
            input_2 = float(input_2)
            result = format(2.54*2.54 * input_2 * input_1,'.3f')
        else:
            result = '请选择单位！'
    ui.lineEdit_3.setText(str(result))

#圆形的处理函数
def Circle_convert(ui):
    """
    该函数主要判定参数输入是否合理，如果没有输入规定的数据或没有选择单位,
    则输出提示；如果选择数据均正确,则计算圆形面积,并将结果显示到lineEdit_3中
    """
    input_1 = ui.lineEdit.text()  #这个地方出来问题，不能读入数据了.唯一的可能就在与存在两个窗口出现了问题。
    if input_1==''or is_number(input_1)==0 or float(input_1)<0:
        result="请输入合理数据！"
    elif ui.radioButton.isChecked()==True:
        result = float(input_1)
        result=format(1*result*result*math.pi,'.3f')
    elif ui.radioButton_2.isChecked()==True:
        result = float(input_1)
        result=format(2.54*2.54*result*result*math.pi,'.3f')
    else:
        result='请选择单位！'
    ui.lineEdit_3.setText(str(result))

#三角型处理函数
def Tri_comvert(ui):
    """
    该函数主要判定参数输入是否合理，如果没有输入规定的数据或没有选择单位,
    则输出提示；如果选择数据均正确,则计算三角形面积,并将结果显示到lineEdit_3中
    """
    input_1 = ui.lineEdit.text()
    input_2 = ui.lineEdit_2.text()
    input_4 = ui.lineEdit_4.text()
    # 计算面积
    if input_1!=''and input_2!=''and input_4!=''and is_number(input_1)==1 and is_number(input_2)==1 and is_number(input_4)==1 and float(input_1)>=0 and float(input_2)>=0 and float(input_4)>=0:
        a = float(input_1)
        b = float(input_2)
        c = float(input_4)
        s = (a + b + c) / 2
        if a+b > c and a+c > b and b+c > a:
            result = math.sqrt(s * (s - a) * (s - b) * (s - c))
            if ui.radioButton.isChecked() == True:
               result = format(1 * result , '.3f')
            if ui.radioButton_2.isChecked() == True:
               result = format(2.54 * 2.54 * result  , '.3f')
        else:
            result='输入不构成三角形，重新输入！'
    else:
        result='请输入完整合理数据！'
    ui.lineEdit_3.setText(str(result))

#辨别是否为正数
def is_number(s):
    """
    判断输出的数是否为正数，如果不是则弹出提示
    """
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError,ValueError):
        pass
    return False


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
    ui.pushButton.clicked.connect(partial(Square_convert, ui))

    #第二个界面
    SecWindow = QMainWindow()
    ui2 = Ui_Form3()
    ui2.setupUi(SecWindow)
    ui2.pushButton.clicked.connect(partial(rectangle_convert, ui2))

    #第三个界面(圆形）
    ThWindow=QMainWindow()
    ui3 = Ui_Form4()
    ui3.setupUi(ThWindow)
    ui3.pushButton.clicked.connect(partial(Circle_convert, ui3))

    # 第四个界面(三角形）
    FoWindow = QMainWindow()
    ui4 = Ui_Form5()
    ui4.setupUi(FoWindow)
    ui4.pushButton.clicked.connect(partial(Tri_comvert, ui4))

    #翻页操作
    ui0.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui0.pushButton_1.clicked.connect(partial(SecWindow.show, ))
    ui0.pushButton_2.clicked.connect(partial(ThWindow.show, ))
    ui0.pushButton_3.clicked.connect(partial(FoWindow.show, ))

    # 因为这个是退出，所以必须把代码放在这个之前。不然就会显示出无效的提示。
    sys.exit(app.exec_())