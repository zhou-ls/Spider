# -*- coding: utf-8 -*-
# @Time : 2020/7/9 23:05
# @Author : zls
# @File : get_drug_name_from_web.py
# @Software: PyCharm
import re
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from openpyxl import Workbook, load_workbook
from random import randint

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数,隐藏selenium防一定程度的反爬
# chrome_options.add_argument('headless')
# browser = webdriver.Chrome("D:\chrom\Chrome-bin\chromedriver.exe", chrome_options=chrome_options)
browser = webdriver.Chrome(executable_path=r"D:\chrom\Chrome-bin\chromedriver.exe")
wait = WebDriverWait(browser, 10)

# 打开excel文档追加爬取
# wb = load_workbook("药品说明书(全).xlsx")
# currentSheet = wb["Sheet1"]

f = open('疾病名称.txt', 'w', encoding='utf-8')


def search():
    browser.get('https://www.baikemy.com/disease/list/0/0?diseaseContentType=A')
    html = browser.page_source
    doc = pq(html)
    drug_name = doc('.typeInfo .typeInfo_List a').text()
    drug_name = drug_name.strip().split()
    print('drug_name:', len(drug_name))
    for name in drug_name:
        print(name)
        f.write(name + '\n')
    # drug_urls = doc('.info-left .content-list').items()
    # for url in drug_urls:
    #     paths = url.find('a').items()
    #     for path in paths:
    #         # print(path.attr('href'))
    #         browser.get('https://www.baikemy.com' + path.attr('href'))
    #         html = browser.page_source
    #         doc = pq(html)
    #         # 当前爬取的药品名称
    #         detail_name = doc('.main_wrap .content_wrap .content_left .detail_name_wrap .detail_name').text()
    #         print(detail_name)
    #         print('--------------')
    #         # 当前爬取的药品通用名
    #         name_info = doc('.main_wrap .content_wrap .content_left .name_info').text()
    #         print(name_info)
    #         print('--------------')
    #         # 当前爬取的药品目录
    #         content_nav = doc('.main_wrap .content_wrap .content_left .content_nav_wrap .content_nav').text()
    #         print(content_nav)
    #         print('--------------')
    #         content = doc('.main_wrap .content_wrap .content_left .content .directory_flag').items()
    #         for con in content:
    #             # p = con.find('p').items()
    #             title = con.text()
    #             print(title)
    #             print('--------------')
    #             title_content = con.siblings().text()
    #             print(title_content)
    #             print('--------------')


if __name__ == '__main__':
    search()


