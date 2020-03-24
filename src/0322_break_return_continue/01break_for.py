#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
for i in range(1, 11):
    if i % 2 == 0:
        break
    # 到第一个符合条件的情况下就停止。不输出符合条件的语句，并停止。
    print("i = ", i)
