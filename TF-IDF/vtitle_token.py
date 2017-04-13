# encoding=utf-8
import jieba
import jieba.analyse
import sys
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer

reload(sys)
sys.setdefaultencoding('utf8')

#
# vectorizer = CountVectorizer()
# corpus = [
#         'This is the first document.',
#         'This is the second second document.',
#         'And the third one.',
#         'Is this the first document?',
#     ]
# X = vectorizer.fit_transform(corpus)
# print X.toarray()
# print vectorizer.get_feature_names()
#
# transformer = TfidfTransformer()
# # counts = [[3, 0, 1],
# #           [2, 0, 0],
# #           [3, 0, 0],
# #           [4, 0, 0],
# #           [3, 2, 0],
# #           [3, 0, 2]]
# tfidf = transformer.fit_transform(X.toarray())
# print tfidf.toarray()



jieba.load_userdict("dic/tangdoukey.dic")
jieba.analyse.set_stop_words("dic/stopLibrary.dic")
file = open("text/diu_videotitle_mini.txt").read()
# file = open("text/diu_videotitle_mini.txt").read()

# tags = jieba.analyse.extract_tags(file, topK=20, withWeight=False, allowPOS=())
# print(",".join(tags))

n=1
for line in file:
    n=n+1
    # print str(n) + " " + line.split("\t",1)[0] + " ".join(jieba.cut(line.split("\t",1)[1]))
    # 对文档进行分词处理，采用默认模式
    seg_list = jieba.cut(line.split("\t",1)[1])

    # 对空格，换行符进行处理
    for seg in seg_list:

        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n"):
            # result.append(seg)
            print seg
