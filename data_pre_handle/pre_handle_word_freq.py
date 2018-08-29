#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/25 下午2:54
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : pre_handle_word_freq.py
# @Software: PyCharm

from common_import import *
from conf.conf import *
from log import init_logging
import util
import data_pre_handle.deal_english_word_dic as dd

logger = logging.getLogger()  # 获取日志logger
WORD_FREQ_SEPATOR = ' '
END_WORD_FREQ = ';'


def deal_word_frequency_data():
    """加载词频数据,并且剔除词频为0的词
    :return: True or False
    """
    word_freq = dict()
    open_ret, inf = util.open_file_r(WORD_FREQ)
    if open_ret == RET_FAIL:
        logger.error('打开文件失败')
        return RET_FAIL

    # 读取英汉医学大词典的单词
    words = set(dd.deal_medical_dict())
    # print(words)

    for line in inf:
        line= line.strip()
        word_freq_info = line.split(WORD_FREQ_SEPATOR)
        if len(word_freq_info) != 2:
            logger.debug('词频格式不对: %s' % line)
            continue
        word_freq_info[1] = word_freq_info[1].replace(END_WORD_FREQ,'')
        if word_freq_info[1] == '0':
            continue
        if not word_freq_info[0] in words:
            continue
        word_freq[word_freq_info[0]] = int(word_freq_info[1])

    # print(len(word_freq))
    util.mk_dirname(WORD_FREQ_PRE)
    with open(WORD_FREQ_PRE, 'w') as f:
        json.dump(word_freq, f)
    logging.info('词频文件预处理成功')


if __name__ == "__main__":
    init_logging()
    deal_word_frequency_data()

