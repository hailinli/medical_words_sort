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


def deal_word_group():
    """
    统计词组频率
    :return:
    """
    word_group = dict()
    open_ret1, f = util.open_file_r(MEDICAL_WORD_GROUP)
    if open_ret1 == RET_FAIL:
        logger.error('打开文件失败')
    # i = 0
    for line in f:
        line = line.strip()
        for word in line.split(' '):
            if not word in word_group:
                word_group[word] = 0
            word_group[word] += 1
        # i += 1
        # if i > 1000:
        #     break

    with open(MEDICAL_WORD_GROUP_FREQ, 'w') as werrf:
        json.dump(word_group, werrf)
    logging.info('词组词汇频率文件处理成功')
    logging.info(word_group)


def get_word_group_freq():
    """
    从词组词频文件中拿到词频文件中单词的词组词频
    :return:
    """
    word_group_freq = dict()
    # 加载词频文件,用于获取其中的词汇
    open_ret1, wrf = util.open_file_r(WORD_FREQ_PRE)
    if open_ret1 == RET_FAIL:
        logger.error('打开文件失败')
    # 加载词组词频文件
    open_ret2, wgfrf = util.open_file_r(MEDICAL_WORD_GROUP_FREQ)
    if open_ret2 == RET_FAIL:
        logger.error('打开文件失败')
    # 加载字典
    wd = json.load(wrf)
    wgfd = json.load(wgfrf)
    for wd_i in wd:  # 对每词频文件中的一个单词进行词组统计
        if wd_i in wgfd:  # 如果该词在词组词频文件中
            word_group_freq[wd_i] = wgfd[wd_i]

    with open(MEDICAL_WORD_GROUP_FREQ_USE, 'w') as werrf:
        json.dump(word_group_freq, werrf)
    logging.info('有用词组频率文件处理成功')
    logging.info(word_group_freq)
    logging.info('词组词频词个数: %s' % len(wgfd.keys()))
    logging.info('词组词频有用词个数: %s' % len(word_group_freq.keys()))


if __name__ == "__main__":
    init_logging()
    # deal_word_group()
    get_word_group_freq()