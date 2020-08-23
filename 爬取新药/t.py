# -*- coding: utf-8 -*-
# @Time : 2020/8/14 14:11
# @Author : zls
# @File : get_table.py
# @Software: PyCharm
from pyquery import PyQuery as pq

html = '''
<div class="margin15 prodetab_p">	
	<p class="ifolable">药品名称</p>
	<p>
        <br />通用名称：血复生胶囊
        <br />汉语拼音：XuefushengJiaonang
    </p>
    <p class="ifolable">成份<p>
    <p>炙黄芪、当归、白芍、熟地黄、川芎、女贞子、墨旱莲、茯苓、山药、天花粉、牡丹皮、泽泻、川牛膝、甘草、大黄（酒炙）、猪脾粉。</p>
</div>
		'''

doc = pq(html)
ins = doc('.margin15.prodetab_p')
print(ins.text())
print('-----------------------------------------------------------------------')
ins.find('p.ifolable').remove()
ins = ins.find('p').items()
for i in ins:
    print(i.text())
    print('===================================================================')
