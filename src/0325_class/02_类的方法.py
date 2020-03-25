#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-

# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    # 类的方法
    def speak(self):
        print("{} 说: 我 {} 岁。".format( self.name, self.age))


if __name__ == '__main__':
    # 实例化类
    p = People('runoob', 10, 30)
    p.speak()
    print("p.age = {}".format(p.age))
    print("People.age = {}".format(People.age))
