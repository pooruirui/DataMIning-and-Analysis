# -*- coding = utf-8 -*-
# @Time : 2023/2/5 10:27
# @Author : 彭睿
# @File : level_uptest.py
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import random
from urllib import request

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome()
driver.get('https://search.jd.com/')

driver.implicitly_wait(2)

driver.find_element(By.ID, 'keyword').send_keys('冰箱')
driver.find_element(By.CSS_SELECTOR,'body > div.searchbox > form > input.input_submit').click()

f = open(f'test.csv',mode='a',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
    '商品标题',
    '商品价格',
    '评论量',
    '店铺名字',
    '标签',
    '商品详情页',
    '好评数量',
    '中评数量',
    '差评数量',
    '分数',
])#爬取存入dic中然后用csv库办法以键相对应写入csv
csv_writer.writeheader()

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


def drop_down():
    """执行页面滚动的操作"""  # javascript
    for x in range(1, 12, 2):  # for循环下拉次数，取1 3 5 7 9 11， 在你不断的下拉过程中, 页面高度也会变的；
        time.sleep(1)
        j = x / 9  # 1/9  3/9  5/9  9/9
        # document.documentElement.scrollTop  指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)  # 执行我们JS代码

def scroll():
    js = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)

a = 0
if __name__ == '__main__':
    for page in range(1, 17):
        drop_down()
        lis = driver.find_elements(By.CSS_SELECTOR, '#J_goodsList ul li')  # 找到本页中的所有商品页面的SCC
        for li in lis:
            try:
                title = li.find_element(By.CSS_SELECTOR, '.p-name em').text.replace('\n', '')  # 商品标题 获取标签文本数据
                price = li.find_element(By.CSS_SELECTOR, '.p-price strong i').text  # 价格
                commit = li.find_element(By.CSS_SELECTOR, '.p-commit strong a').text  # 评论量
                href = li.find_element(By.CSS_SELECTOR, '.p-img a').get_attribute('href')  # 商品详情页
                icons = li.find_elements(By.CSS_SELECTOR, '.p-icons i')
                icon = ','.join([i.text for i in icons])  # 列表推导式  ','.join 以逗号把列表中的元素拼接成一个字符串数据
            except:
                pass
            li.find_element(By.CSS_SELECTOR, '.p-name em').click()  # 点击进入二级页面
            windows = driver.window_handles
            driver.switch_to.window(windows[-1])
            # 已经切换到了这个位置，在这个条目下操作
            scroll()
            time.sleep(1)
            try:
                driver.find_element(By.CSS_SELECTOR, '#detail > div.tab-main.large > ul > li:nth-child(5)').click()
                haoping = driver.find_element(By.CSS_SELECTOR,
                                              '#comment > div.mc > div.J-comments-list.comments-list.ETab > div.tab-main.small > ul > li:nth-child(5) > a > em').text
                zhongping = driver.find_element(By.CSS_SELECTOR,
                                                '#comment > div.mc > div.J-comments-list.comments-list.ETab > div.tab-main.small > ul > li:nth-child(6) > a > em').text
                chaping = driver.find_element(By.CSS_SELECTOR,
                                              '#comment > div.mc > div.J-comments-list.comments-list.ETab > div.tab-main.small > ul > li:nth-child(6) > a > em').text
                fenshu = driver.find_element(By.CSS_SELECTOR,
                                             '#comment > div.mc > div.comment-info.J-comment-info > div.comment-percent > div').text
            except:
                pass
            dit = {
                '商品标题': title,
                '商品价格': price,
                '评论量': commit,
                '标签': icon,
                '商品详情页': href,
                '好评数量': haoping,
                '中评数量': zhongping,
                '差评数量': chaping,
                '分数': fenshu,
            }
            csv_writer.writerow(dit)
            a+=1
            print(a)
            driver.close()
            driver.switch_to.window(windows[0])
        driver.find_element(By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next > i').click()  # 下一页
        get_html(driver.current_url)