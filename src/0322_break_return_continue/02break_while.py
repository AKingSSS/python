#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-

var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("猜一个10以内的数字："))
    if num == 5:
        print("猜对了")
        break
    print("猜错了，继续...")

print("Good bye!")
