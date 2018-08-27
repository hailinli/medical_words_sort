#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/25 下午3:28
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : util.py
# @Software: PyCharm
from common_import import *
from conf.conf import *
logger = logging.getLogger()  # 获取日志logger


def open_file_r(f):
    """
    打开文件, 返回文件流
    :param f: str, 文件名
    :return:
    """
    rf = ''
    try:
        rf = open(f, 'r')
    except:
        logger.exception('打开文件失败')
        return RET_FAIL, rf
    logger.debug('打开文件成功 %s' %f)
    return RET_SUCC, rf


def write_file(f, out_str):
    """
    写文件
    :param f: str, 文件名
    :param out_str: str
    :return:
    """

    mk_dirname(f)
    try:
        wf = open(f, mode='a+', encoding='utf-8')
        wf.write(out_str)
        wf.write('\n')
        wf.close()
    except:
        logger.exception('写入文件失败')
        return RET_FAIL

    return RET_SUCC


def mk_dirname(f):
    """
    根据文件名f,判断文件目录是否存在,如果不存在那么创建
    :param f:
    :return:
    """
    dir_name = os.path.dirname(f)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
