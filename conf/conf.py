#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/16 下午11:39
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : conf.py
# @Software: PyCharm

# 配置日志
LOG_PATH = '../log'  # 相对于项目跟目录
MEDICAL_SORT_NAME = 'medical_sort.log'  # 日志名

# 数据预处理
WORD_FREQ = '/Users/lihailin/Repository/tmpRepository/medical_word_sort/医学英语资源-非压缩版/UMLS/词频.txt'  # 词频文件
WORD_FREQ_PRE = '/Users/lihailin/Repository/tmpRepository/medical_word_sort//data_pre_handle/UMLS/词频_pre.txt'  # 词频文件
MEDICAL_ETYMA = '/Users/lihailin/Repository/tmpRepository/medical_word_sort//医学英语资源-非压缩版/词根词缀表.txt'  # 医学词典
MEDICAL_ETYMA_PRE = '/Users/lihailin/Repository/tmpRepository/medical_word_sort//data_pre_handle/词根词缀表_pre.txt'
MEDICAL_ETYMA_FREQ_PRE = '/Users/lihailin/Repository/tmpRepository/medical_word_sort//data_pre_handle/词根词缀频率表.txt'
MEDICAL_ETYMA_WORD = '/Users/lihailin/Repository/tmpRepository/medical_word_sort//data_pre_handle/词缀_单词关联表.txt'
MEDICAL_ETYMA_WORD_RE = '/Users/lihailin/Repository/tmpRepository/medical_word_sort/data_pre_handle/单词_词缀关联表.txt'
MEDICAL_WORD_GROUP = '/Users/lihailin/Repository/tmpRepository/medical_word_sort/医学英语资源-非压缩版/UMLS/umls-medical english phrase(804W+).txt'
MEDICAL_WORD_GROUP_FREQ = '/Users/lihailin/Repository/tmpRepository/medical_word_sort/data_pre_handle/词组各词频率表.txt'
MEDICAL_WORD_GROUP_FREQ_USE  = '/Users/lihailin/Repository/tmpRepository/medical_word_sort//data_pre_handle/词组各词频率表(useful).txt'

NANFANG_SENTENCE_PATH = '/Users/lihailin/Repository/tmpRepository/medical_word_sort/医学英语资源-非压缩版/南方科技大学英汉双语平行语料库双语例句(1)-(19)'


# 配置返回状态
RET_SUCC = 0
RET_FAIL = -1
RET_CONTINUE = -2