import pickle
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import pandas as pd
from PIL import Image
from konlpy.tag import Twitter
from collections import Counter
import matplotlib.pyplot as plt

class WordCloud():
    def Review_cloud(self, Review):
        heart = np.array(Image.open('./heart.png'))

        Reviews = Review['Review']

        twitter = Twitter()
        word_counts=12000           #빈출단어중 1위부터 몇위까지만 보여줄지 선택
        sentences_tag = []

        with open('stopwords.pickle', 'rb') as f:
            stopwords = pickle.load(f)

        for sentence in Reviews:
            morph = twitter.pos(sentence)
            sentences_tag.append(morph)
        noun_adj_list = []

        #명사와 형용사만 구분하여 이스트에 넣기
        for sentence1 in sentences_tag:
            for word, tag in sentence1:
                if tag in ['Noun', 'Adjective']:
                    noun_adj_list.append(word)

        #형태소별 count
        counts = Counter(noun_adj_list)
        tags = counts.most_common(word_counts)

        #wordCloud생성
        #한글꺠지는 문제 해결하기위해 font_path 지정
        wc = WordCloud(font_path='c:\\windows\\fonts\\NanumGothic.ttf', stopwords = stopwords, background_color='white', max_words=1500,
                       mask=heart, colormap="Reds")

        a=dict(tags)
        a_list=list(a)

        for i in range(len(a_list)):
            if a_list[i] in stopwords:
                del a[a_list[i]]

        cloud = wc.generate_from_frequencies(a)

        plt.figure(figsize=(20,20))
        plt.axis('off')
        plt.imshow(cloud, interpolation='bilinear')
        fig = plt.gcf() #변경한 곳
        fig.savefig(str(Product)+'.png') #변경한 곳
        fig.clf()
        plt.clf()
