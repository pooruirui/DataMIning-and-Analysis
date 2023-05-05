# -*- coding = utf-8 -*-
# @Time : 2023/2/26 17:20
# @Author : 彭睿
# @File : item_pinpai_pa.py
# @Software : PyCharm

import random
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree

driver = webdriver.Chrome()
driver.get('https://search.jd.com/')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')
driver.implicitly_wait(1)

driver.find_element(By.ID, 'keyword').send_keys('洗衣机')#可变
Note=open('品牌\洗衣机.txt',mode='w',encoding='utf-8')#可变

driver.find_element(By.CSS_SELECTOR,'body > div.searchbox > form > input.input_submit').click()
driver.find_element(By.CSS_SELECTOR,'#J_selector > div.J_selectorLine.s-brand > div > div.sl-ext > a.sl-e-more.J_extMore').click()
dom = etree.HTML(driver.page_source)

a=dom.xpath('/html/body/div[5]/div[2]/div[1]/div[1]/div/div[2]/div[2]/ul/li[*]/a/@title')
print(a)
item = []
print(a[0].find('（',))

for i in a :
    if i.find('（') != -1:
        x = i[0:i.find('（')]
        item.append(x)
        y = i[i.find('（')+1:i.find('）')]
        item.append(y)
    else :
        item.append(i)

for i in item:
    Note.write(i+'\n')



