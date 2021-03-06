# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/hys02245/03cb90dee288331d05f48bd923ae734c/untitled5.ipynb
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install ckiptagger
!pip install tensorflow
!pip install gdown
from ckiptagger import data_utils
data_utils.download_data_gdown("./")

import csv
import jieba, re, os, sys
from ckiptagger import WS

corpus = []

ws = WS("./data")
with open('/content/drive/MyDrive/處理中備份資料/2018預測用_Final 0601(對照檔).csv', encoding = 'big5hkscs', newline='') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    corpus.append(ws([row[6]]))
#print(corpus) 

corpus=corpus[1:]

with open('/content/drive/MyDrive/處理中備份資料/KAM測試集_0601.csv', encoding = 'big5hkscs', newline='') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    corpus.append(ws([row[3]]))

corpus1=[]
for item in corpus:
  corpus1.append(" ".join(item[0]))
#print(corpus1)

import jieba
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
 
vectorizer=CountVectorizer()
transformer=TfidfTransformer()
tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus1))
word=vectorizer.get_feature_names()
weight=tfidf.toarray()

with open("/content/drive/MyDrive/處理中備份資料/outputnew.csv","w") as csvfile: 
  writer = csv.writer(csvfile)
  for i in range(len(weight)):
    writer.writerow([u"第",i+1,u"個文本tf-idf權重"])
    for j in range(len(word)):
      if weight[i][j] != 0 :
        writer.writerow([word[j],weight[i][j],Counter(corpus[i][0])[word[j]]])