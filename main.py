#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/25 下午5:37
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : main.py
# @Software: PyCharm

from common_import import *
from conf.conf import *
from log import init_logging
import util

logger = logging.getLogger()  # 获取日志logger


class Deal:

    def __init__(self):
        self.wed = dict()
        self.load_word_etyma()
        self.ewd = dict()
        self.load_etyma_word()
        self.wgfu = dict()
        self.load_word_group()
        self.wfd = dict()
        self.load_word_freq()
        self.word = ''  # 单词
        self.word_etyma = ''  # 该单词词缀
        self.ret_set = set()  # 记录已经排好序的词汇集合
        self.word_freq_order_dict = []  # 词频按顺序保存,方便拿去最高频率的词,拿掉的马上删掉
        self.fill_word_freq_order_dict()

    def load_word_etyma(self):
        """

        :return:
        """
        # 打开词缀词频文件
        open_ret2, f = util.open_file_r(MEDICAL_ETYMA_WORD_RE)
        if open_ret2 == RET_FAIL:
            logger.error('打开文件失败')
        # 加载字典
        self.wed = json.load(f)

    def load_etyma_word(self):
        """

        :return:
        """
        # 打开词缀词频文件
        open_ret2, f = util.open_file_r(MEDICAL_ETYMA_WORD)
        if open_ret2 == RET_FAIL:
            logger.error('打开文件失败')
        # 加载字典
        self.ewd = json.load(f)

    def load_word_group(self):
        """

        :return:
        """
        # 打开词缀词频文件
        open_ret2, f = util.open_file_r(MEDICAL_WORD_GROUP_FREQ_USE)
        if open_ret2 == RET_FAIL:
            logger.error('打开文件失败')
        # 加载字典
        self.wgfu = json.load(f)

    def load_word_freq(self):
        """

        :return:
        """
        # 打开词缀词频文件
        open_ret2, f = util.open_file_r(WORD_FREQ_PRE)
        if open_ret2 == RET_FAIL:
            logger.error('打开文件失败')
        # 加载字典
        self.wfd = json.load(f)


    def find_first_few(self, tmp_dict, number):
        """
        找到字典,返回值前几的单词
        :param tmp_dict:
        :param number:
        :return:
        """
        f = zip(tmp_dict.values(),tmp_dict.keys())
        f = list(f)
        sorted(f)
        if len(f) < number:
            return f
        return f[:number]

    def fill_word_freq_order_dict(self):
        """

        :param tmp_dict:
        :return:
        """
        f = zip(self.wfd.values(), self.wfd.keys())
        f = list(f)
        sorted(f)
        self.word_freq_order_dict = f

    def get_and_rm_word_freq_most(self):
        """
        得到词频最高的词,并删除
        :return:
        """
        if len(self.word_freq_order_dict) == 0:
            return ''
        t = self.word_freq_order_dict[0][1]
        del(self.word_freq_order_dict[0])
        return t

    def has_same_etyma_word(self):
        """查找单词是否有同词缀单词,有,那么填写该词缀

        :return:
        """
        if not self.word in self.wed:
            return False
        etyma_t = self.wed[self.word]  # 找打单词的词缀
        if len(self.ewd[etyma_t]) == 0:  # 如果该单词没有同词缀单词
            return False
        self.word_etyma = etyma_t
        return True

    def random_select(self, tmp_list):
        """

        :param tmp_list:
        :param number:
        :return:
        """
        if len(tmp_list) == 0:
            return ''
        tl = set(tmp_list)
        while True:
            if len(tl) == 0:
                return ''
            s = random.sample(tl, 1)[0]
            if not s in self.ret_set:
                return s
            else:
                tl.remove(s)
        return ''

    def deal_has_same_etyma_word(self):
        """
        从同词缀单词集合,选择最合适的
        :return:
        """
        wg_tmp = {}
        wf_tmp = {}
        for w in self.ewd[self.word_etyma]:  # 找到同词缀的单词
            if w in self.ret_set:
                continue

            if w in self.wgfu:
                wg_tmp[w] = self.wgfu[w]  # 单词-词组频率,构词能力
            if w in self.wfd:
                wf_tmp[w] = self.wfd[w]  # 统计单词频率
        t1 = self.find_first_few(wf_tmp, 2)  # 找到词频最高同词缀的两个词
        t2 = self.find_first_few(wg_tmp, 2)  # 找到构词能力最好的同词缀两个词
        if len(t1) > 0:  # 先看频率最高的同词缀单词
            return t1[0][1]
        elif len(t2) > 0:  # 再看构词能力最高的同词缀单词
            return t2[0][1]
        else:  # 否则随机选一个
            return self.random_select(self.ewd[self.word_etyma])  #

    def deal_has_diff_etyma_word(self):
        """

        :return:
        """
        return ''

    def get_next(self):
        """

        :return:
        """

        has_etyma = self.has_same_etyma_word()
        if has_etyma == True:  # 如果有词缀单词
            return self.deal_has_same_etyma_word()  # 处理同词缀单词
        else:
            return self.deal_has_diff_etyma_word()  # 处理不同词缀

    def sort(self):
        """
        单词排序
        :return:
        """
        i = 1
        ret_list = []
        start_word = self.get_and_rm_word_freq_most()  # 找词频最高的词
        # start_word = 'dermatitis'
        self.word = start_word  # 设置开始词汇
        self.ret_set.add(start_word)
        ret_list.append(start_word)
        while True:
            nw = self.get_next()
            if nw == '':
                nw = self.get_and_rm_word_freq_most()
                if nw == '':
                    continue
            if not nw in self.ret_set:
                self.ret_set.add(nw)
                ret_list.append(nw)
                # print(nw)
                # print(self.ret_set)
            self.word = nw
            # break
            i += 1
            print(nw, self.wfd[nw], i)
        print(ret_list)

if __name__ == '__main__':
    # 初始化日志, 配置了基本的logger
    init_logging()
    deal = Deal()
    deal.sort()

