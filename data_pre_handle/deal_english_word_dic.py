#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/27 下午8:14
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : deal_english_word_dic.py
# @Software: PyCharm

from common_import import *
from conf.conf import *
from log import init_logging
import util

logger = logging.getLogger()  # 获取日志logger

RE = [r'[a-zA-Z\-]+']


def deal_medical_dict():
    """
    :return:
    """
    medical_words = []
    open_ret, inf = util.open_file_r(MEDICAL_WORDS_DIC)
    # etymas = dict()
    if open_ret == RET_FAIL:
        logger.error('打开文件失败')
        return RET_FAIL
    for line in inf:
        if line.strip() == "":
            continue
        #  正则匹配
        for re_RE in RE:
            m = re.compile(re_RE)
            gs = m.findall(line)
            if gs == None:
                continue
            for g in gs:
                if len(g) < 3:
                    continue
                if '-' in g:
                    continue
                # print(g)
                medical_words.append(g)
    return medical_words

    # util.mk_dirname(MEDICAL_ETYMA_PRE)
    # with open(MEDICAL_ETYMA_PRE, 'w') as f:
    #     json.dump(etymas, f)
    # logging.info('词缀文件处理成功')
    # logging.info(etymas)


if __name__ == "__main__":
    init_logging()
    deal_medical_etyma()