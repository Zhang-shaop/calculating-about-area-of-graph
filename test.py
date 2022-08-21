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


if __name__ == '__main__':
    unittest.main()
