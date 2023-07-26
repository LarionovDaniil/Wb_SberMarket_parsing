import pandas as pd
from wordcloud import WordCloud
import re
from pymystem3 import Mystem

def make_word_cloud():
    """
    Read comments from file and make Wordcloud
    :return: 0
    """
    m = Mystem()
    reviews = pd.read_csv('reviews.csv', sep='$').T

    reviews_list = reviews.index.map(str.lower).to_list()[:-1]

    stop_words = open('stop-ru.txt', 'r', encoding='utf8')
    stop_words = stop_words.read()
    stop_words = set(stop_words.split('\n'))

    reviews_kirill = list(map(lambda x: ' '.join(re.sub(r'[^а-яё ]', ' ', x).split()), reviews_list))
    print(len(reviews_kirill))
    reviews_clean = ' '.join(list(map(lambda x: ' '.join(set(x.split()) - stop_words), reviews_kirill)))
    reviews_lemm = ''.join(m.lemmatize(reviews_clean))
    need_or_not = ' '.join(reviews_lemm.split())

    wordCloud = WordCloud(width=2000, height=2000, random_state=1, background_color='black', colormap='Set2', collocations=False).generate(need_or_not)
    wordCloud.to_file("wordcloud.png")

    return 0

