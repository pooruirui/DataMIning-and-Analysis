# -*- coding = utf-8 -*-
# @Time : 2023/2/3 9:02
# @Author : 彭睿
# @File : contrl_test.py
# @Software : PyCharm
import csv
from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://search.jd.com/')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)


driver.find_element(By.ID, 'keyword').send_keys('冰箱')#输入搜索内容
confirm_btn = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'body > div.searchbox > form > input.input_submit')   # 定位按钮位置
    )
)
confirm_btn.click()    # 点击操作

#进入到每一个商品页面进行内容爬取
for i in range(1,60):
    confirm_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#J_goodsList > ul > li:nth-child(i) > div > div.p-img > a > img')  # 定位按钮位置
        )
    )
    confirm_btn.click()
lis = driver.find_elements()
#driver.back() 返回上一页
