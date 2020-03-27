#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-

# 父类定义
class Parent:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))
