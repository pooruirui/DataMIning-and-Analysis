# -*- coding = utf-8 -*-
# @Time : 2023/2/26 17:07
# @Author : 彭睿
# @File : item_title_most_search.py
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import jieba

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv('洗衣机.csv')
# print(df)
itemname = df['商品标题']
# print(itemname)
stopwords = '品牌\洗衣机.txt'
stop_single_words=['\n','',' ','\r\n']

with open(stopwords,'r',encoding='utf-8') as f:
    for line in f:
        content=line.strip()
        stop_single_words.append(content)
print(stop_single_words)

word_list = []
for sentence in itemname:
    word_cut = [i for i in jieba.cut(sentence)]
    for word in word_cut:
        if word not in stop_single_words:
            word_list.append(word)

Note=open('关键字\洗衣机.txt',mode='w',encoding='utf-8')#可变

for i in word_list:
    Note.write(i+'\n')