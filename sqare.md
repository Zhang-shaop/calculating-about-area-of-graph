Help on module sqare_calculate:

NAME
    sqare_calculate - # -*- coding: utf-8 -*-

CLASSES
    builtins.object
        Ui_Form
        Ui_Form2
        Ui_Form3
        Ui_Form4
        Ui_Form5
    
    class Ui_Form(builtins.object)
     |  定义一个计算正方形面积的界面类
     |  
     |  Methods defined here:
     |  
     |  retranslateUi(self, Form)
     |      该函数为界面元素赋予新的命名显示
     |  
     |  setupUi(self, Form)
     |      创建该界面，并创建以下的界面元素：
     |      pushButton 确认计算的按钮；
     |      label 该页面的标题显示；
     |      label_2 提示输入数据类型的显示；
     |      label_3 提示数据输出的显示；
     |      radioButton 选择计算单位为厘米；
     |      radioButton_2 选择计算单位为英寸；
     |      lineEdit 输入计算所需数据；
     |      lineEdit_3 输出计算结果；
     |      同时设置了该窗口的大小以及每个界面元素的大小尺寸
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Ui_Form2(builtins.object)
     |  定义了一个初始菜单界面的类，用来显示需要选择哪个计算模式
     |  
     |  Methods defined here:
     |  
     |  retranslateUi(self, Form)
     |      该函数为界面元素赋予新的命名显示
     |  
     |  setupUi(self, Form)
     |      创建该界面，并创建以下的界面元素：
     |      label 提示选择某种计算模式的标签；
     |      pushButton 选择计算正方形的面积；
     |      pushButton_1 选择计算长方形的面积；
     |      pushButton_2 选择计算圆形的面积；
     |      pushButton_3 选择计算三角形的面积；
     |      同时设置了该窗口的大小以及每个界面元素的大小尺寸
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Ui_Form3(builtins.object)
     |  定义一个计算长方形面积的窗口类
     |  
     |  Methods defined here:
     |  
     |  retranslateUi(self, Form)
     |      该函数为界面元素赋予新的命名显示
     |  
     |  setupUi(self, Form)
     |      创建该界面，并创建以下的界面元素：
     |      pushButton 确认计算的按钮；
     |      label 该页面的标题显示；
     |      label_2 提示输入长方形长边长度的显示；
     |      label_3 提示数据输出的显示；
     |      label_4 提示输入长方形宽边长度的显示；
     |      radioButton 选择计算单位为厘米；
     |      radioButton_2 选择计算单位为英寸；
     |      lineEdit 输入计算所需数据；
     |      lineEdit_2 输入计算所需数据；
     |      lineEdit_3 输出计算结果；
     |      同时设置了该窗口的大小以及每个界面元素的大小尺寸；
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Ui_Form4(builtins.object)
     |  定义一个计算正方形面积的窗口类
     |  
     |  Methods defined here:
     |  
     |  retranslateUi(self, Form)
     |      该函数为界面元素赋予新的命名显示
     |  
     |  setupUi(self, Form)
     |      创建该界面，并创建以下的界面元素：
     |      pushButton 确认计算的按钮；
     |      label 该页面的标题显示；
     |      label_2 提示输入数据类型的显示；
     |      label_3 提示数据输出的显示；
     |      radioButton 选择计算单位为厘米；
     |      radioButton_2 选择计算单位为英寸；
     |      lineEdit 输入计算所需数据；
     |      lineEdit_3 输出计算结果；
     |      同时设置了该窗口的大小以及每个界面元素的大小尺寸；
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Ui_Form5(builtins.object)
     |  定义一个计算三角形面积的窗口类
     |  
     |  Methods defined here:
     |  
     |  retranslateUi(self, Form)
     |      该函数为界面元素赋予新的命名显示
     |  
     |  setupUi(self, Form)
     |      创建该界面，并创建以下的界面元素：
     |      pushButton 确认计算的按钮；
     |      label 该页面的标题显示；
     |      label_2 提示输入三角形第三条边的显示；
     |      label_3 提示输入三角形第二条边的显示；
     |      label_4 提示输入三角形第一条边的显示；
     |      label_5 提示数据输出的显示；
     |      radioButton 选择计算单位为厘米；
     |      radioButton_2 选择计算单位为英寸；
     |      lineEdit 输入计算所需数据；
     |      lineEdit_2 输入计算所需数据；
     |      lineEdit_3 输出计算结果；
     |      lineEdit_4 输入计算所需数据；
     |      同时设置了该窗口的大小以及每个界面元素的大小尺寸；
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    Circle_convert(ui)
        该函数主要判定参数输入是否合理，如果没有输入规定的数据或没有选择单位,
        则输出提示；如果选择数据均正确,则计算圆形面积,并将结果显示到lineEdit_3中
    
    Square_convert(ui)
        该函数主要判定参数输入是否合理，如果没有输入规定的数据或没有选择单位,
        则输出提示；如果选择数据均正确,则计算正方形面积,并将结果显示到lineEdit_3中
    
    Tri_comvert(ui)
        该函数主要判定参数输入是否合理，如果没有输入规定的数据或没有选择单位,
        则输出提示；如果选择数据均正确,则计算三角形面积,并将结果显示到lineEdit_3中
    
    is_number(s)
        判断输出的数是否为正数，如果不是则弹出提示
    
    rectangle_convert(ui)
        该函数主要判定参数输入是否合理，如果没有输入规定的数据或没有选择单位,
        则输出提示；如果选择数据均正确,则计算正方形面积,并将结果显示到lineEdit_3中

FILE
    d:\code_2022\calculating-about-area-of-graph\sqare_calculate.py


