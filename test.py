import unittest

import math
from sqare_calculate import is_number

# 关于正方形函数的重载
def Square_convert(ui, radioButton_isChecked, radioButton_2_isChecked):
    input_1 = ui
    if input_1 == '' or is_number(input_1) == 0 or float(input_1) < 0:
        result = "请输入合理数据！"
    elif radioButton_isChecked == True:
        result = float(input_1)
        result = format(1 * result * result, '.3f')
    elif radioButton_2_isChecked == True:
        result = float(input_1)
        result = format(2.54 * 2.54 * result * result, '.3f')
    else:
        result = '请选择单位！'
    return str(result)


# 关于长方形函数的重载
def rectangle_convert(ui1, ui2, radioButton_isChecked, radioButton_2_isChecked):
    input_1 = ui1
    input_2 = ui2
    if input_1 == '' and input_2 == '':
        result = '请输入长和宽！'
    elif input_1 == '' and input_2 != '':
        result = "请输入长！"
    elif input_2 == '' and input_1 != '':
        result = "请输入宽！"
    elif is_number(input_1) == 0 or float(input_1) < 0 or is_number(input_2) == 0 or float(input_2) < 0:
        result = "请输入合理数据！"
    else:
        if radioButton_isChecked == True:
            input_1 = float(input_1)
            input_2 = float(input_2)
            result = format(1 * input_2 * input_1, '.3f')
        elif radioButton_2_isChecked == True:
            input_1 = float(input_1)
            input_2 = float(input_2)
            result = format(2.54 * 2.54 * input_2 * input_1, '.3f')
        else:
            result = '请选择单位！'
    return str(result)

#关于球型函数的重载
def Circle_convert(ui,radioButton_isChecked,radioButton_2_isChecked):
    input_1 = ui  #这个地方出来问题，不能读入数据了.唯一的可能就在与存在两个窗口出现了问题。
    if input_1==''or is_number(input_1)==0 or float(input_1)<0:
        result="请输入合理数据！"
    elif radioButton_isChecked==True:
        result = float(input_1)
        result=format(1*result*result*math.pi,'.3f')
    elif radioButton_2_isChecked==True:
        result = float(input_1)
        result=format(2.54*2.54*result*result*math.pi,'.3f')
    else:
        result='请选择单位！'
    return str(result)

#关于三角函数的重载
def Tri_convert(ui1,ui2,ui3,radioButton_isChecked,radioButton_2_isChecked):
    input_1 = ui1
    input_2 = ui2
    input_4 = ui3
    # 计算面积
    if input_1!=''and input_2!=''and input_4!=''and is_number(input_1)==1 and is_number(input_2)==1 and is_number(input_4)==1 and float(input_1)>=0 and float(input_2)>=0 and float(input_4)>=0:
        a = float(input_1)
        b = float(input_2)
        c = float(input_4)
        s = (a + b + c) / 2
        if a+b > c and a+c > b and b+c > a:
            result = math.sqrt(s * (s - a) * (s - b) * (s - c))
            if radioButton_isChecked == True:
               result = format(1 * result , '.3f')
            if radioButton_2_isChecked == True:
               result = format(2.54 * 2.54 * result  , '.3f')
        else:
            result='输入不构成三角形，重新输入！'
    else:
        result='请输入完整合理数据！'
    return str(result)




class MyTestCase(unittest.TestCase):
    # 测试正方形的计算函数
    def test_Square_convert1(self):
        self.assertEqual(Square_convert(3, 1, 0), str(format(9, '.3f')))

    def test_Square_convert2(self):
        self.assertEqual(Square_convert(3, 0, 1), str(format(58.064, '.3f')))

    def test_Square_convert3(self):
        self.assertEqual(Square_convert(3, 0, 0), '请选择单位！')

    def test_Square_convert4(self):
        self.assertEqual(Square_convert('e', 1, 0), '请输入合理数据！')

        # 测试长方形的计算函数
    def test_rectangle_convert1(self):
        self.assertEqual(rectangle_convert('', 1,1, 0), '请输入长！')
    def test_rectangle_convert2(self):
        self.assertEqual(rectangle_convert(1, '',1, 0), '请输入宽！')
    def test_rectangle_convert3(self):
        self.assertEqual(rectangle_convert('', '', 1, 0), '请输入长和宽！')
    def test_rectangle_convert4(self):
        self.assertEqual(rectangle_convert(1, 1, 0, 0), '请选择单位！')
    def test_rectangle_convert5(self):
        self.assertEqual(rectangle_convert('e', 1, 0, 0), '请输入合理数据！')
    def test_rectangle_convert6(self):
        self.assertEqual(rectangle_convert(-1, 1, 0, 0), '请输入合理数据！')
    def test_rectangle_convert7(self):
        self.assertEqual(rectangle_convert(1, 2, 1, 0),str(format(2, '.3f')) )
    def test_rectangle_convert8(self):
        self.assertEqual(rectangle_convert(1, 2, 0, 1),str(format(12.903, '.3f')) )

        #测试球形的计算函数
    def test_Circle_convert1(self):
        self.assertEqual(Circle_convert(3, 1, 0), str(format(28.274, '.3f')))

    def test_Circle_convert2(self):
        self.assertEqual(Circle_convert(3, 0, 1), str(format(182.415, '.3f')))

    def test_Circle_convert3(self):
        self.assertEqual(Circle_convert(3, 0, 0), '请选择单位！')

    def test_Circle_convert4(self):
        self.assertEqual(Circle_convert('e', 1, 0), '请输入合理数据！')

        #三角形的计算函数
    def test_Tri_comvert1(self):
        self.assertEqual(Tri_convert('e', 1,2,1, 0), '请输入完整合理数据！')
    def test_Tri_comvert2(self):
        self.assertEqual(Tri_convert('',1, 1, 0,1), '请输入完整合理数据！')
    def test_Tri_comvert3(self):
        self.assertEqual(Tri_convert(1,-1, 1,1, 0), '请输入完整合理数据！')
    def test_Tri_comvert4(self):
        self.assertEqual(Tri_convert(1,3, 1, 0,1),'输入不构成三角形，重新输入！' )
    def test_Tri_comvert5(self):
         self.assertEqual(Tri_convert(3,4,5, 1, 0),str(format(6, '.3f')) )
    def test_Tri_comvert6(self):
        self.assertEqual(Tri_convert(3, 4, 5, 0, 1), str(format(38.710, '.3f')))


if __name__ == '__main__':
    unittest.main()
