# -*- coding: utf-8 -*-
# @Time : 2020/8/14 14:24
# @Author : zls
# @File : t1.py
# @Software: PyCharm
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.wrap')
# print(wrap.text())
wrap.find('p').remove()
print(wrap.text())
