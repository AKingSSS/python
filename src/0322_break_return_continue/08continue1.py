#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-

for i in range(2):
    print("i = ", i)
    for j in range(2, 5):
        if j == 3:
            print("继续第二个for循环")
            continue
        print("j = ", j)