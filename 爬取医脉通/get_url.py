# -*- coding: utf-8 -*-
# @Time : 2020/8/10 11:35
# @Author : zls
# @File : get_url.py
# @Software: PyCharm
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq


browser = webdriver.Chrome(executable_path=r"D:\chrom\Chrome-bin\chromedriver.exe")
wait = WebDriverWait(browser, 10)
browser.get('http://www.medlive.cn/auth/login')
submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'body > div.large-box.login-box > div.page-main > div > div.main-right > div.login-rightTab.clearfix.qr-goTab > div.rightTab-L')))
submit.click()
input1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
# 医脉通的用户名
input1.send_keys('18707117829')
input2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
# 当前用户名的密码
input2.send_keys('u8gbv6')
submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginsubmit')))
submit.click()

# 直接爬取所有药品
browser.get('http://drugs.medlive.cn/drugref/drugCate.do?treeCode=Z03')
html = browser.page_source
doc = pq(html)
# print(html)
urls = doc('.four-table .table-three .table_new table tbody .first_line th a').items()
for url in urls:
    print('http://drugs.medlive.cn/' + url.attr('href'))
