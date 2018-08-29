#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/26 下午4:12
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : get_etyma_freq.py
# @Software: PyCharm

from common_import import *
from conf.conf import *
from log import init_logging
import util

logger = logging.getLogger()  # 获取日志logger


def get_etyma_freq():
    """
    :return:
    """
    etyma_freq = dict()
    etyma_word = dict()
    # 加载词频文件
    open_ret1, wrf = util.open_file_r(WORD_FREQ_PRE)
    if open_ret1 == RET_FAIL:
        logger.error('打开文件失败')
    # 打开词缀文件
    open_ret2, wfrf = util.open_file_r(MEDICAL_ETYMA_PRE)
    if open_ret2 == RET_FAIL:
        logger.error('打开文件失败')
    # 加载字典
    wd = json.load(wrf)
    wfd = json.load(wfrf)
    for wd_i in wd:  # 对每一个单词进行词缀统计

        for wfd_i in wfd:  # 对一个词缀进行统计
            if not wfd_i in etyma_freq:
                etyma_freq[wfd_i]  = 0  # 用于统计该词缀出现次数
                etyma_word[wfd_i] = []  # 用于保存该词缀相关的词
            len_wfd_i = len(wfd_i)  # 词缀长度
            if wfd[wfd_i] == 0:  # 如果词缀是前缀
                if wd_i[:len_wfd_i] == wfd_i:  # 如果单词包含该词缀
                    # print(type(wd[wd_i]))
                    etyma_freq[wfd_i] += wd[wd_i]
                    etyma_word[wfd_i].append(wd_i)
            else:
                if wd_i[:-len_wfd_i] == wfd_i:  # 如果单词包含该词缀
                    etyma_freq[wfd_i] += wd[wd_i]
                    etyma_word[wfd_i].append(wd_i)
    with open(MEDICAL_ETYMA_FREQ_PRE, 'w') as werrf:
        json.dump(etyma_freq, werrf)
    logging.info('词缀频率文件处理成功')
    logging.info(etyma_freq)

    with open(MEDICAL_ETYMA_WORD, 'w') as werrf:
        json.dump(etyma_word, werrf)
    logging.info('词缀单词映射处理成功')
    logging.info(etyma_word)


def get_word_etyma():
    # 打开词缀词频文件
    open_ret2, f = util.open_file_r(MEDICAL_ETYMA_WORD)
    if open_ret2 == RET_FAIL:
        logger.error('打开文件失败')
    # 加载字典
    ewd = json.load(f)

    word_etyma = dict()
    for ewd_i in ewd:
        for word in ewd[ewd_i]:
            word_etyma[word] = ewd_i
    with open(MEDICAL_ETYMA_WORD_RE, 'w') as werrf:
        json.dump(word_etyma, werrf)
    logging.info('词缀单词映射转换成功,保存文件')
    logging.info(word_etyma)




if __name__ == "__main__":
    init_logging()
    get_etyma_freq()
    get_word_etyma()