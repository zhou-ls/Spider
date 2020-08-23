#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/20 10:26
# @Author : zls
# @Site : 
# @File : check.py
# @Software: PyCharm
f = open(r'.\result_data\实体对+句子+三分类.txt', 'r', encoding='utf-8')
f1 = open(r'.\result_data\check.txt', 'w', encoding='utf-8')
a = 0
b = 0
c = 0
while True:
    content = f.readline()

    if content == '' or a == 100:
        break
    words = content.strip().split()
    if words[:-1][2] == "相互作用机制":
        a = a + 1
        f1.write(content)
while True:
    content = f.readline()

    if content == '' or b == 100:
        break
    words = content.strip().split()
    if words[:-1][2] == "相互作用结果":
        b = b + 1
        f1.write(content)
while True:
    content = f.readline()

    if content == '' or c == 100:
        break
    words = content.strip().split()
    if words[:-1][2] == "临床建议":
        c = c + 1
        f1.write(content)
