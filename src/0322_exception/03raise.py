#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
if __name__ == '__main__':
    try:
        raise TypeError('类型错误')
    except Exception as e:
        print(e)
