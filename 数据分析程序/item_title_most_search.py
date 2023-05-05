# -*- coding = utf-8 -*-
# @Time : 2023/2/26 17:07
# @Author : 彭睿
# @File : item_title_most_search.py
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv('冰箱.csv')
# print(df)
itemname = df['item']
# print(itemname)
stopwords = 'D:/数据爬取/test/关键字/无.txt'
stop_single_words=['\n','',' ','\r\n']

with open(stopwords,'r',encoding='utf-8') as f:
    for line in f:
        content=line.strip()
        stop_single_words.append(content)
print(stop_single_words)

def draw_word_cloud(a,name):
    word_list = []
    for sentence in a:
        word_cut = [i for i in jieba.cut(sentence)]
        for word in word_cut:
            if word not in stop_single_words:
                word_list.append(word)
    text = ' '.join(word_list)
    mask = plt.imread('冰箱.jpg')
    wc = WordCloud(mask=mask,background_color='white',font_path='C:\Windows\Fonts\simhei.ttf')
    wc.generate(text)
    plt.title(str(name))
    plt.imshow(wc)
    plt.axis('off')
    plt.show()


draw_word_cloud(itemname, "常见词")
