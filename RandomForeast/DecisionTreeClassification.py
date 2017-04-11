# -*- coding:utf-8 -*-

import pandas as pd
import os
from sklearn import tree,metrics

train = pd.read_table("/Users/wenlong.zhang/Documents/work/app-expand/sample.txt")

print(len(train))
# print(train.head(10))

predictors = ["is_reg", "os_version", "div_f", "hour_f", "resolution", "u_nettype", "u_province", "u_city", "u_netop",
              "search_cnt", "sug_cnt", "homepage_cnt", "hp_hot_cnt", "hp_dancemusic_cnt", "hp_talent_cnt",
              "hp_category_cnt", "hp_new_cnt", "hp_follow_cnt", "hp_greatest_cnt", "hp_live_cnt", "hp_stage_cnt",
              "hp_more_cnt", "feaddback_cnt", "showdance_cnt", "upload_cnt", "serv_cnt", "serv_unique_cnt", "vcnt",
              "vv", "vp", "vst", "vc", "vsf", "vf", "vs", "vd"]

clf = tree.DecisionTreeClassifier()  # 加载决策树分类器
clf = clf.fit(train[predictors][:11000], train['tag'][:11000])  # 训练决策树

with open("model.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

# 在终端输入命令 dot -Tpng model.dot -o model.png 调用mac上的graphviz 生成模型决策树图片
# graphviz 需要用homebrew cask 安装 brew cask install graphviz

# os.unlink('model.dot') # 删除文件

predicted = clf.predict(train[predictors][11001:])

# summarize the fit of the model
print(metrics.classification_report(train['tag'][11001:], predicted))
print(metrics.confusion_matrix(train['tag'][11001:], predicted))

print(pd.merge(train[predictors][11001:],predicted))


