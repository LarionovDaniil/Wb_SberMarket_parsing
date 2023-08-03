import re
import pandas as pd
from wordcloud import WordCloud
from pymystem3 import Mystem


def kirill_list():
    reviews = pd.read_csv('reviews.csv', sep='$').T
    all_reviews = reviews.index.to_list()[:-1]
    reviews_list = reviews.index.map(str.lower).to_list()[:-1]
    reviews_kirill = list(map(lambda x: ' '.join(re.sub(r'[^а-яё ]', ' ', x).split()), reviews_list))
    return reviews_kirill, all_reviews


def make_word_cloud(words_kirill_only):
    """
    Read comments from file and make Wordcloud
    :return: 0
    """
    m = Mystem()

    stop_words = open('stop-ru.txt', 'r', encoding='utf8')
    stop_words = stop_words.read()
    stop_words = set(stop_words.split('\n'))

    reviews_clean = ' '.join(list(map(lambda x: ' '.join(set(x.split()) - stop_words), words_kirill_only)))
    pril_nar = []
    okonch = ['ая', 'яя', 'ой', 'ий', 'ый', 'ое', 'ее']
    for word in reviews_clean.split():
        if word[-1] == 'o' or word[-2:] in okonch or word == 'брак':
            pril_nar.append(word)
    reviews_clean = ' '.join(pril_nar)
    reviews_lemm = ''.join(m.lemmatize(reviews_clean))
    need_or_not = ' '.join(reviews_lemm.split())

    wordCloud_gen = WordCloud(width=2000, height=2000, random_state=1, background_color='black', colormap='Set2', collocations=False).generate(need_or_not)
    wordCloud_gen.to_file("wordcloud.png")

    return 0

