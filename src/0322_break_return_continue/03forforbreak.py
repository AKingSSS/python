#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
for i in range(2):
    print("i = ", i)
    for j in range(2, 5):
        if j == 3:
            print("退出第二个for循环")
            break
        print("j = ", j)
