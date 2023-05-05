# -*- coding = utf-8 -*-
# @Time : 2023/2/26 15:27
# @Author : 彭睿
# @File : clean_second.py
# @Software : PyCharm
import pandas as pd
import numpy as np

df = pd.read_csv('D:/数据爬取/test/除湿器.csv',encoding='utf-8')

def gettxt(txtpath):
    with open(txtpath, 'r',encoding='utf-8') as f:
        data = f.read().strip().split()
    return data

def item_clean():
    pinpailist = gettxt(r'D:\数据爬取\test\品牌\除湿器.txt')
    item = []
    for i in df['商品标题']:
        for pinpai in pinpailist:
            if i.find(pinpai) != -1 :
                item.append(pinpai)
                break
    return item


def price_clean():
    price = []
    for i in df['商品价格']:
        price.append(int(i))
    return price

def comments_clean():
    df['评论量'] = df['评论量'].replace(np.nan, 0)
    df['评论量'].astype('str')
    comments = []
    # print(df['评论量'].tail())
    # print(i[-1])
    for i in df['评论量']:
        # print(type(i))
        a = "cl"
        if type(i) == type(a):
            if i[-1] == '+':
                i = i[:-1]
                if i[-1] == '万':
                    i = i[:-1]+str('0000')
            comments.append(int(i))
        else:
            comments.append(int(i))
    return comments

def icon_clean():
    icons = []
    df['标签'] = df['标签'].replace(np.nan, '无')
    for i in df['标签']:
        icons.append(i)
    return icons

def good_comment_clean():
    good_comments = []
    for i in df['好评数量']:
        if str(i) == 0:
            good_comments.append(i)
        elif str(i).find('-') != -1:
            good_comments.append(0)
        elif str(i).find('万') != -1:
            i = i[1:i.find('万')]
            i = float(i) * 10000
            good_comments.append(i)
        elif str(i).find('+') != -1:
            i = i[1:i.find('+')]
            good_comments.append(i)
        elif str(i) == '()':
            good_comments.append(i)
        else:
            good_comments.append(i)
    return good_comments

def mid_comment_clean():
    mid_comment = []
    for i in df['中评数量']:
        if str(i) == 0:
            mid_comment.append(i)
        elif str(i).find('-') != -1:
            mid_comment.append(0)
        elif str(i).find('万') != -1:
            i = i[1:i.find('万')]
            i = float(i) * 10000
            mid_comment.append(i)
        elif str(i).find('+') != -1:
            i = i[1:i.find('+')]
            mid_comment.append(i)
        elif str(i) == '()':
            mid_comment.append(i)
        else:
            mid_comment.append(i)
    return mid_comment

def bad_comment_clean():
    bad_comment = []
    for i in df['差评数量']:
        if str(i) == 0:
            bad_comment.append(i)
        elif str(i).find('-') != -1:
            bad_comment.append(0)
        elif str(i).find('万') != -1:
            i = i[1:i.find('万')]
            i = float(i) * 10000
            bad_comment.append(i)
        elif str(i).find('+') != -1:
            i = i[1:i.find('+')]
            bad_comment.append(i)
        elif str(i) == '()':
            bad_comment.append(i)
        elif str(i) == '()':
            bad_comment.append(0)
        else:
            bad_comment.append(i)
    return bad_comment

def scores_clean():
    scores=[]
    for i in df['分数']:
        i = str(i)[:-1]
        scores.append(int(i))
    return scores

# print(len(item_clean()))
# print(len(price_clean()))
# print(len(price_clean()))
# print(len(comments_clean()))
# print(len(icon_clean()))
# print(len(good_comment_clean()))
# print(len(bad_comment_clean()))
# print(len(mid_comment_clean()))
# print(len(scores_clean()))

if __name__ == '__main__':
    item_clean()
    price_clean()
    comments_clean()
    icon_clean()
    good_comment_clean()
    mid_comment_clean()
    bad_comment_clean()
    scores_clean()
    data = {'item':item_clean(),'price':price_clean(),'comments':comments_clean(),
            'icon':icon_clean(),'good':good_comment_clean(),'mid':mid_comment_clean(),'bad':bad_comment_clean()}
    df1 = pd.DataFrame(data)
    df1.to_csv('D:/数据爬取/test/清洗数据备份/除湿器.csv')

