# 定义基类 Shape （私有属性 area ，封装计算面积的私有方法 calc_area ）
# 子类 Circle / Rectangle 继承 Shape ，重写面积计算逻辑（多态体现）
# 类变量记录所有图形的创建数量，实例变量存储各自尺寸
# 要求：通过实例调用公开方法获取面积，禁止直接访问私有属性
import math


class Shape:
    count = 0  # 记录所有图形数量的类变量

    def __init__(self):
        self.__area = 0.0  # 私有属性
        Shape.count += 1

    def __calc_area(self):
        """装计算面积的私有方法"""
        pass

    def _set_area(self, value):
        """受保护接口，供子类修改父类私有成员"""
        self.__area = value

    def get_area(self):
        """公开接口"""
        return self.__area


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()
        self.__calc_area()

    def __calc_area(self):
        area = self.length * self.width
        self._set_area(area)


class Circle(Shape):
    def __init__(self, R):
        self.R = R
        super().__init__()
        self.__calc_area()

    def __calc_area(self):
        area = math.pi * (self.R ** 2)
        self._set_area(area)

# 测试
shapes = [Circle(3), Rectangle(4, 5)]
print(f"总图形数量：{shapes[0].count}")
for s in shapes:
    print(f"面积: {s.get_area():.2f}")