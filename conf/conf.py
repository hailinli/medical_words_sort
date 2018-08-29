#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/16 下午11:39
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : conf.py
# @Software: PyCharm

# 项目根目录
MEDICAL_WORDS_SORT_ROOT = '/Users/lihailin/Repository/tmpRepository/medical_words_sort'

# 配置日志
LOG_PATH = '%s/log' % MEDICAL_WORDS_SORT_ROOT  # 相对于项目跟目录
MEDICAL_SORT_NAME = 'medical_sort.log'  # 日志名

# 数据预处理
MEDICAL_WORDS_DIC = '%s/医学英语资源-非压缩版/英汉医学大词典.txt' % MEDICAL_WORDS_SORT_ROOT
WORD_FREQ = '%s/医学英语资源-非压缩版/UMLS/词频.txt' % MEDICAL_WORDS_SORT_ROOT # 词频文件
WORD_FREQ_PRE = '%s/data_pre_handle/词频_PRE.json' % MEDICAL_WORDS_SORT_ROOT   # 词频文件

MEDICAL_ETYMA = '%s/医学英语资源-非压缩版/词根词缀表.txt' % MEDICAL_WORDS_SORT_ROOT   # 医学词典
MEDICAL_ETYMA_PRE = '%s/data_pre_handle/词根词缀表_pre.json' % MEDICAL_WORDS_SORT_ROOT

MEDICAL_ETYMA_FREQ_PRE = '%s/data_pre_handle/词根词缀频率表.json' % MEDICAL_WORDS_SORT_ROOT
MEDICAL_ETYMA_WORD = '%s/data_pre_handle/词缀_单词关联表.json' % MEDICAL_WORDS_SORT_ROOT
MEDICAL_ETYMA_WORD_RE = '%s/data_pre_handle/单词_词缀关联表.json' % MEDICAL_WORDS_SORT_ROOT

MEDICAL_WORD_GROUP = '%s/医学英语资源-非压缩版/UMLS/umls-medical english phrase(804W+).txt' % MEDICAL_WORDS_SORT_ROOT
MEDICAL_WORD_GROUP_FREQ = '%s/data_pre_handle/词组各词频率表.json' % MEDICAL_WORDS_SORT_ROOT
MEDICAL_WORD_GROUP_FREQ_USE  = '%s/data_pre_handle/词组各词频率表(useful).json' % MEDICAL_WORDS_SORT_ROOT

NANFANG_SENTENCE_PATH = '%s/医学英语资源-非压缩版/南方科技大学英汉双语平行语料库双语例句(1)-(19)' % MEDICAL_WORDS_SORT_ROOT

MEDICAL_SORT_RET = '%s/data_pre_handle/sort_result.txt' % MEDICAL_WORDS_SORT_ROOT

# 配置返回状态
RET_SUCC = 0
RET_FAIL = -1
RET_CONTINUE = -2