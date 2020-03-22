#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-

# for - else 正常结束
for i in range(10):
    print(i)
else:
    print("循环执行结束")


# for - else 非正常结束
for i in range(10):
    print(i)
    if i == 3:
        break
else:
    print("循环执行结束")
