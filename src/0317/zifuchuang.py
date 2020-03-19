#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    s = 'Hello Python'
    # 打印第一个字符e
    print(s[1])
    # 打印最后一个字符n
    print(s[-1])
    """
    可以采用[N: M]格式获取字符串的子串，这个操作被形象地称为切片。
    [N: M]获取字符串中从N到M（但不包含M）间连续的子字符串。
    """
    # 打印 llo P
    print(s[2:7])
    # 打印 llo Pyth
    print(s[2:-2])
    # 打印字符串的长度(一个中文字符和西文字符的长度都记为1) 12
    print(len(s))
    print(-3%10)#答案是1个数字,答对入群
