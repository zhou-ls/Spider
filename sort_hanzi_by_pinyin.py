# # -*- coding: utf-8 -*-
# # @Time : 2020/4/3 20:42
# # @Author : zls
# # @File : sort_hanzi_by_pinyin.py
# # @Software: PyCharm
"""

两种排序方法

"""


"""使用gbk编码对汉字进行排序(此方法较好)"""
f = open(r'.\origin_data\all_drug_name.txt', 'r', encoding='utf-8')
all_name = []
while True:
    name = f.readline()
    if name == '':
        break
    all_name.append(name.replace(' ', '')[:-1])
all_name = list(set(all_name))
f = open(r'.\origin_data\all_drug_name.txt', 'w', encoding='utf-8')
g_all = []
n_all = []
for i in all_name:
    try:
        # 能gbk编码
        test = i.encode('gbk')
        g_all.append(i)
    except:
        # 不能gbk编码
        n_all.append(i)
out = sorted(g_all, key=lambda x: x.encode('gbk'))
for i in out:
    f.write(i + '\n')
for i in n_all:
    f.write(i + '\n')
f.close()


"""
使用pypinyin库对汉字按首字母排序
"""
# import pypinyin
#
#
# # 根据汉字首字母拼音排序
# def hanzi_to_pinyin(first_word):
#     results = pypinyin.pinyin(first_word, style=pypinyin.NORMAL)
#     return ''.join(result[0][0] for result in results if len(results) > 0)
#
#
# f = open(r'.\origin_data\all_drug_name.txt', 'r', encoding='utf-8')
# all_name = []
# while True:
#     name = f.readline()
#     if name == '':
#         break
#     all_name.append(name.replace(' ', '')[:-1])
# all_name.sort(key=lambda x: hanzi_to_pinyin(x[0]))
# f.close()
# f = open(r'.\origin_data\all_drug_name.txt', 'w', encoding='utf-8')
# for i in all_name:
#     f.write(i + '\n')
# f.close()
