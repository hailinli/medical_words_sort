#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/25 下午11:47
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : pre_medical_etyma.py
# @Software: PyCharm

from common_import import *
from conf.conf import *
from log import init_logging
import util

logger = logging.getLogger()  # 获取日志logger

RE = [r'([a-z]+\（o\）-)', r'([a-z]+-)', r'(-[a-z]+\（o\）)', r'(-[a-z]+)']


def deal_medical_etyma():
    """
    :return:
    """
    open_ret, inf = util.open_file_r(MEDICAL_ETYMA)
    etymas = dict()
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
                gr = 0
                if g.startswith('-'):
                    gr = 0
                if g.endswith('-'):
                    gr = 1
                g = g.replace('-', '')
                g = g.replace('（o）', '')
                etymas[g] = gr

    util.mk_dirname(MEDICAL_ETYMA_PRE)
    with open(MEDICAL_ETYMA_PRE, 'w') as f:
        json.dump(etymas, f)
    logging.info('词缀文件处理成功')
    logging.info(etymas)


if __name__ == "__main__":
    init_logging()
    deal_medical_etyma()