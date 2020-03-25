#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
class Student():
    # age,name是类变量
    age = 0
    name = 'stu'

    def __init__(self, age, name):
        # 访问实例变量(用self.age  self.name)
        self.age = age
        self.name = name

s = Student(18, 'hello')
print(s.name)  # 打印实例变量，输出 hello

print(Student.name)  # 打印类变量，输出 stu
