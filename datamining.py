import mysql
import jieba
import jieba.analyse
from pyecharts import WordCloud


def wordcloud():
    datas = mysql.readdata()
    stringtemp = ""
    for data in datas:
        stringtemp += data[4].split('-')[0]
    print(jieba.analyse.extract_tags(stringtemp, topK=20, withWeight=True, allowPOS=()))

    name, value = [], []
    for data in jieba.analyse.extract_tags(stringtemp, topK=20, withWeight=True, allowPOS=()):
        name.append(data[0])
        value.append(data[1])
    wordcloud = WordCloud("词云", title_pos='40%', title_top=10, width=1200,
                          height=600, title_text_size=25,
                          page_title=' 词 云 图 ',
                          background_color='#40E0D0')
    wordcloud.add("", name, value, shape='diamond', word_size_range=[20, 100])
    wordcloud.render('词云图.html')


wordcloud()
