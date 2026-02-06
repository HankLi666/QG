# 定义基类 Shape （私有属性 area ，封装计算面积的私有方法 calc_area ）
# 子类 Circle / Rectangle 继承 Shape ，重写面积计算逻辑（多态体现）
# 类变量记录所有图形的创建数量，实例变量存储各自尺寸
# 要求：通过实例调用公开方法获取面积，禁止直接访问私有属性

import math

class Shape :
    count = 0
    def __init__(self):
        self.__area = 0.0
        Shape.count += 1


class Circle (Shape) :
    def __init__(self , lenth , width):
        self.lenth = lenth
        self.width = width
        super().__init__()
        self.calculate()
    
    def calculate(self):
        area = self.lenth * self.width


class Rectangle (Shape) :
    def __init__(self , R):
        self.R = R
        super().__init__()
        self.calculate() 
    def calculate(self):
        area = math.pi * (self.R ** 2)