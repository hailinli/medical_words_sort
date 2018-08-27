#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/26 下午7:56
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : xls2csv.py
# @Software: PyCharm

from common_import import *
from conf.conf import *
from log import init_logging
import util

def xls2csv(xlsFile, csvFileName):
    # excel文件转csv
    data = pd.read_excel(xlsFile, sheetname=0, index_col=0)
    data.to_csv(csvFileName, encoding='utf-8')

if __name__ == "__main__":
    fs = os.listdir(NANFANG_SENTENCE_PATH)
    # os.system('rm %s/*.csv' % NANFANG_SENTENCE_PATH)
    for f in fs:
        f = NANFANG_SENTENCE_PATH + '/' + f
        xls2csv(f, f.replace('.xlsx', '.csv'))
        print(f)