#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
from Parent import Parent

# 单继承示例
class Son(Parent):

    def __init__(self, name, age, weight, grade):
        # 调用父类的实例化方法
        Parent.__init__(self, name, age, weight)
        self.grade = grade

    # 重写父类的speak方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

s = Son('ken', 10, 30, 3)
s.speak()