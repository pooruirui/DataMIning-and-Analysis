# -*- coding = utf-8 -*-
# @Time : 2023/2/5 9:19
# @Author : 彭睿
# @File : def_test.py
# @Software : PyCharm
import random
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome()
driver.get('https://search.jd.com/')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')
driver.implicitly_wait(1)

driver.find_element(By.ID, 'keyword').send_keys('手机')
driver.find_element(By.CSS_SELECTOR,'body > div.searchbox > form > input.input_submit').click()

f = open(f'一级手机'f'.csv',mode='a',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
    '商品标题',
    '商品价格',
    '评论量',
    '标签',
    '商品详情页',
])#爬取存入dic中然后用csv库办法以键相对应写入csv
csv_writer.writeheader()

def scroll():
    js = "window.scrollTo(0,docume" \
         "" \
         "nt.body.scrollHeight)"
    driver.execute_script(js)

def drop_down():
    """执行页面滚动的操作"""  # javascript
    for x in range(1, 12, 2):  # for循环下拉次数，取1 3 5 7 9 11， 在你不断的下拉过程中, 页面高度也会变的；
        time.sleep(1)
        j = x / 9  # 1/9  3/9  5/9  9/9
        # document.documentElement.scrollTop  指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)  # 执行我们JS代码

def get_user_agent():
    """
    模拟headers的user-agent字段，
    返回一个随机的user-agent字典类型的键值对
    """
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]

    fakeheader = {}
    fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
    return fakeheader


def get_html(url):
    try:
        r = request.get(url, timeout=30, headers=get_user_agent())
        r.raise_for_status
        r.encoding = r.apparent_encding
        return r.status_code

    except:
        return "someting wrong!"

def get_shop_info():
    lis = driver.find_elements(By.CSS_SELECTOR, '#J_goodsList ul li')  # 找到本页中的所有商品页面的SCC
    for li in lis:
        try:
            title = li.find_element(By.CSS_SELECTOR, '.p-name em').text.replace('\n', '')  # 商品标题 获取标签文本数据
            price = li.find_element(By.CSS_SELECTOR, '.p-price strong i').text  # 价格
            commit = li.find_element(By.CSS_SELECTOR, '.p-commit strong a').text  # 评论量下·
            href = li.find_element(By.CSS_SELECTOR, '.p-img a').get_attribute('href')  # 商品详情页
            icons = li.find_elements(By.CSS_SELECTOR, '.p-icons i')
            icon = ','.join([i.text for i in icons])  # 列表推导式  ','.join 以逗号把列表中的元素拼接成一个字符串数据
            dit = {
                '商品标题': title,
                '商品价格': price,
                '评论量': commit,
                '标签': icon,
                '商品详情页': href,
            }
            csv_writer.writerow(dit)
        except:
            pass


for page in range(1,100):
    drop_down()
    get_shop_info()
    get_user_agent()
    driver.find_element(By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.pn-next > i').click()#下一页
    get_html(driver.current_url)


