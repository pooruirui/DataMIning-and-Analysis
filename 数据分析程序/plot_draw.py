# -*- coding = utf-8 -*-
# @Time : 2023/2/27 0:34
# @Author : 彭睿
# @File : plot_draw.py
# @Software : PyCharm

#因为买了才能评论，而且几天后会自动评论，所以按照评论量来定义购买量
import pandas as pd
import matplotlib.pyplot as plt
import codecs
import jieba
from wordcloud import WordCloud

plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False

def ReadFile(filePath,encoding="utf-8"):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

frigedf = pd.read_csv('冰箱.csv')
washdf = pd.read_csv('洗衣机.csv')
waterdf = pd.read_csv('热水器.csv')
tvdf = pd.read_csv('电视.csv')
breakdf = pd.read_csv('破壁机.csv')
frieddf = pd.read_csv('空气炸锅.csv')
airdf = pd.read_csv('空调.csv')
wetdf = pd.read_csv('除湿器.csv')


def draw_market_buy_times(x):
    x = x.drop('Unnamed: 0', axis=1, level=None, inplace=False)
    df = x.groupby(['item']).agg(item=('item','first'),comments=('comments','sum'))
    df = df.sort_values('comments', ascending=False)
    print(df)
    values = df['comments']
    labels = []
    for i in df['item']:
        labels.append(i)
    labels = labels[0:10]
    plt.figure(figsize=(8,8))
    plt.pie(values[0:10], labels=labels, autopct='%1.1f%%')
    plt.title('市场购买份额占比前十名')
    plt.savefig('D:/数据爬取/test/市场份额前十占比图/frige.jpg')
    plt.show()


def top_good_comment(x):
    x = x.drop('Unnamed: 0', axis=1, level=None, inplace=False)
    df = x.groupby(['item']).agg(item=('item', 'first'), comments=('good', 'sum'))
    df = df.sort_values('comments', ascending=False)
    print(df)
    values = df['comments']
    labels = []
    for i in df['item']:
        labels.append(i)
    labels = labels[0:10]
    plt.figure(figsize=(8, 8))
    plt.pie(values[0:10], labels=labels, autopct='%1.1f%%')
    plt.title('市场购买好评数前十名')
    plt.savefig('D:/数据爬取/test/市场购买好评前十占比图/frige.jpg')
    plt.show()

def top_bad_comment(x):
    x = x.drop('Unnamed: 0', axis=1, level=None, inplace=False)
    df = x.groupby(['item']).agg(item=('item', 'first'), comments=('bad', 'sum'))
    df = df.sort_values('comments', ascending=False)
    print(df)
    values = df['comments']
    labels = []
    for i in df['item']:
        labels.append(i)
    labels = labels[0:10]
    plt.figure(figsize=(8, 8))
    plt.pie(values[0:10], labels=labels, autopct='%1.1f%%')
    plt.title('市场购买差评数前十名')
    plt.savefig('D:/数据爬取/test/市场购买差评前十占比图/frige.jpg')
    plt.show()

def hot_selling_goods_mean_price_draw(x):
    x = x.drop('Unnamed: 0', axis=1, level=None, inplace=False)
    x =x[x['comments'] >= 100000]
    # print(x)
    df = x.groupby(['item']).agg(item=('item', 'first'), mean_price=('price', 'mean'))
    df = df.sort_values('mean_price', ascending=False)
    print(df)
    columns = []
    values = []
    for i in df['item']:
        columns.append(i)
    for i in df['mean_price']:
        values.append(int(i))
    plt.figure(figsize=(8, 6))
    plt.title('产品销售量超10万的产品售价均值')
    plt.ylabel('元')
    plt.bar(columns[0:], values[0:])
    my_height = values[0:]
    for i in range(len(my_height)):
        plt.text(i, my_height[i] + 100, my_height[i], va='bottom', ha='center')
    plt.savefig('D:/数据爬取/test/市场热卖商品价格均值/frige.jpg')
    plt.show()

if __name__ == '__main__':
    x = frigedf
    draw_market_buy_times(x)
    top_good_comment(x)
    top_bad_comment(x)
    hot_selling_goods_mean_price_draw(x)