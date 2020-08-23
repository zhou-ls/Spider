# -*- coding: utf-8 -*-
# @Time : 2020/8/17 16:16
# @Author : zls
# @File : baike.py
# @Software: PyCharm
from pyquery import PyQuery as pq
import requests

f = open('疾病名称.txt', 'w', encoding='utf-8')

# 维持会话
session = requests.Session()
session.keep_alive = False


def get_html(url):
    response = session.get(url)
    # 解决中文乱码
    response.encoding = response.apparent_encoding
    html = response.text
    return html


def first():
    html = get_html('https://www.baikemy.com/disease/list/0/0?diseaseContentType=A')
    doc = pq(html)
    first_urls = doc('.w_1200 .w_1200 .w_760 .w_756 .scrrenType_head .scrrenType_List .scrrenType_Li a').items()
    first_dic = {}
    for first_url in first_urls:
        if first_url.text() != '全部':
            first_dic[first_url.text()] = 'https://www.baikemy.com' + first_url.attr('href')
    print(first_dic)
    return first_dic


def second(n, url):
    html = get_html(url)
    doc = pq(html)
    second_urls = doc('.w_1200 .w_1200 .w_760 .w_756 .scrrenType_head .scrrenType_SecondList ul li a').items()
    second_dic = {}
    for second_url in second_urls:
        # 从眼科开始没有二级科室
        if n < 8:
            if second_url.text() != '全部':
                second_dic[second_url.text()] = 'https://www.baikemy.com' + second_url.attr('href')
        else:
            second_dic[second_url.text()] = 'https://www.baikemy.com' + second_url.attr('href')
    # print(second_dic)
    return second_dic


def third(url):
    html = get_html(url)
    doc = pq(html)
    third_dic = {}
    drug_names = doc('.typeInfo .typeInfo_List ul .typeInfo_Li a').items()
    for drug_name in drug_names:
        if drug_name.text() != '更多':
            third_dic[drug_name.text()] = 'https://www.baikemy.com' + drug_name.attr('href')
    return third_dic


if __name__ == '__main__':
    first_dic = first()
    n = 0
    for k1, v1 in first_dic.items():
        n += 1
        # 从眼科开始没有二级科室
        second_dic = second(n, v1)
        print(k1)
        for k2, v2 in second_dic.items():
            third_dic = third(v2)
            for k3, v3 in third_dic.items():
                f.write(k1 + '\t' + k2 + '\t' + k3 + '\n')
