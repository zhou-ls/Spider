# -*- coding: utf-8 -*-
# 2-1 国产药品
import re
from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions
from pyquery import PyQuery as pq
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


option = ChromeOptions()  # 实例化一个ChromeOptions对象
# chrome_options = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数
browser = webdriver.Chrome(options=option, executable_path=r"D:\chrom\Chrome-bin\chromedriver.exe")
wait = WebDriverWait(browser, 10)


def search():
    try:
        url_1 = 'http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=36&tableName=TABLE36&title=%BD%F8%BF%DA%D2%A9%C6%B7&bcId=152904858822343032639340277073'
        browser.get(url_1)
        html = browser.page_source
        doc = pq(html)
        num = doc('html body center table tbody tr td table tbody tr td table tbody tr td table tbody tr td div#content div table tbody tr td p a').items()
        for i in num:
            # print(i)
            Id = re.findall('.*Id=(.*)&quot.*', str(i))
            # print(Id)
            url_2 = 'http://app1.nmpa.gov.cn/data_nmpa/face3/content.jsp?tableId=36&tableName=TABLE36&tableView=进口药品&Id=' + ''.join(Id)
            print(url_2)

        # browser.close()

    except Exception as e:
        print(e)
        time.sleep(5)


def next_page():
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > table:nth-child(4) > tbody > tr > td:nth-child(4) > img')))
    submit.click()


if __name__ == '__main__':
    search()
