#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
import re

if __name__ == '__main__':
    s = '给给123werB#'
    pattern = re.compile(r'[^A-Za-z0-9]')
    s = re.sub(pattern, "A", s)
    print(s)
