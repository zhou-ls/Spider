# -*- coding: utf-8 -*-
# @Time : 2020/8/8 21:23
# @Author : zls
# @File : taobao_test.py
# @Software: PyCharm
import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

brower = webdriver.Chrome(executable_path=r"D:\chrom\Chrome-bin\chromedriver.exe")
wait = WebDriverWait(brower, 10)

def getTaobaoCookies():
    # get login taobao cookies
    url = "http://drugs.medlive.cn/drugref/drugCateIndex.do"
    brower.get("http://www.medlive.cn/auth/login")
    while True:
        print("Please login in taobao.com!")
        time.sleep(3)
        # if login in successfully, url  jump to www.taobao.com
        while brower.current_url ==  url:
            tbCookies  = brower.get_cookies()
            brower.quit()
            cookies = {}
            for item in tbCookies:
                cookies[item['name']] = item['value']
            outputPath = open('taobaoCookies.pickle','wb')
            pickle.dump(cookies,outputPath)
            outputPath.close()
            return cookies


def readTaobaoCookies():
    # if hava cookies file ,use it
    # if not , getTaobaoCookies()
    if os.path.exists('taobaoCookies.pickle'):
        readPath = open('taobaoCookies.pickle','rb')
        tbCookies = pickle.load(readPath)
    else:
        tbCookies = getTaobaoCookies()
    return tbCookies

tbCookies = readTaobaoCookies()

brower.get("http://drugs.medlive.cn/drugref/drugCateIndex.do")
for cookie in tbCookies:
    brower.add_cookie({
        "domain":".taobao.com",
        "name":cookie,
        "value":tbCookies[cookie],
        "path":'/',
        "expires":None
    })
brower.get("http://drugs.medlive.cn/drugref/drugCateIndex.do")

