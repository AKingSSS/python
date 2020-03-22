#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-

# 单分支只能用来处理指定的异常情况，如果未捕获到异常，则报错
try:
    a
except NameError as e:  # 我们可以使用except与as+变量名 搭配使用，打印变量名会直接输出报错信息
    print(e)  # name 'a' is not defined
