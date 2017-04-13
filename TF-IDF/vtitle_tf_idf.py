#-*- coding:utf-8 -*-

import jieba.analyse
from sklearn.feature_extraction.text import TfidfVectorizer

jieba.load_userdict("dic/tangdoukey.dic")
jieba.analyse.set_stop_words("dic/stopLibrary.dic")

corpus = []
dius = []
with open("text/diu_videotitle_mini.txt", 'r') as f:
    for line in f:
        dius.append(line.split('\t')[0])
        corpus.append("".join(jieba.cut(line.split('\t')[1], cut_all=False)))

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(corpus)
print tfidf.shape


words = vectorizer.get_feature_names()
for i in xrange(len(corpus)):
    print '----Document %d----' % (i) + '----' + dius[i]
    max_tfidf = 0
    max_index = 0
    for j in xrange(len(words)):
        if tfidf[i,j] >= max_tfidf:
            max_tfidf = tfidf[i,j]
            max_index = j
        if tfidf[i,j] > 0.3:
            print words[j].encode('utf-8'),  tfidf[i,j]
    print words[max_index].encode('utf-8'),  max_tfidf



