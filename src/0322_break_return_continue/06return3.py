#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
def test(s):
    i = 0
    try:
        i += 1
        i/0
        if s == 'python大星':
            print('是他，是他，就是他')
        return i
    except:
        print("系统故障！")
    finally:
        i += 1
        print("关注python大星，你值得拥有！")



print(test("python大星"))