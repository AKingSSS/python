#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-

class Student:
    """
    # 以下是错误的用法
    # 类将它内部的变量和方法封装起来，阻止外部的直接访问
    print(classroom)
    print(address)
    print_age()
    """
    classroom = '106'
    address = 'beijing'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print('%s: %s' % (self.name, self.age))
