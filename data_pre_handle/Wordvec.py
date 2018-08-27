#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/26 下午8:29
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : Wordvec.py
# @Software: PyCharm

from gensim.models import Word2Vec
import os

def word2vec(sentences):

    if os.path.exists('model/word2vec.model'):
        model = Word2Vec.load('model/word2vec.model')
    else:
        model = Word2Vec(sentences, sg=1, size=50,  window=5,  min_count=5,  negative=3, sample=0.001, hs=1, workers=4)
        model.save('model/word2vec.model')
    return model  # 返回词向量字典,后续可根据该词向量字典获得句子矢量矩阵


if __name__ == '__main__':
    sentences = word2vec.LineSentence('./in_the_name_of_people_segment.txt') 
    word2vec(sentences)