#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
if __name__ == '__main__':
    try:
        1 / 0
    except ZeroDivisionError as e:  # 我们可以使用except与as+变量名 搭配使用，打印变量名会直接输出报错信息
        print('ZeroDivisionError', e)  # division by zero
    except Exception as e:
        print('Exception', e)
    finally:
        print("finally 执行")
