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
MERGE_WORD_WORDGROUP_WEIGHT = [0.4, 0.6]

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
        self.merge_wf_wgf = dict()
        self.merge_wf_wgf = self._merge_wordfreq_wgfreq(self.wfd, self.wgfu)  # merge 词频与词组频率
        self.word_merge_freq_order_dict = dict()  # merge后排序
        self.fill_word_merge_freq_order_dict()


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

        self.word_freq_order_dict =  self.find_first_few(self.wfd, len(self.wfd))


    def fill_word_merge_freq_order_dict(self):
        """

        :return:
        """
        self.word_merge_freq_order_dict =  self.find_first_few(self.merge_wf_wgf, len(self.merge_wf_wgf))

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
        # print(self.word)
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


    def _merge_wordfreq_wgfreq(self, wf_tmp, wg_tmp):
        """
        融合构词能力和词组频率
        :param wf_tmp: 词频
        :param wg_tmp: 词组频
        """
        merge_d = dict()
        for wf_i in wf_tmp:
            if wf_i in wg_tmp:  # 如果该词有词组评率
                merge_d[wf_i] = wf_tmp[wf_i] * MERGE_WORD_WORDGROUP_WEIGHT[0]  \
                                + wg_tmp[wf_i] * MERGE_WORD_WORDGROUP_WEIGHT[1]
            else:
                merge_d[wf_i] = wf_tmp[wf_i] * MERGE_WORD_WORDGROUP_WEIGHT[0] * 2
        return merge_d


    def deal_has_same_etyma_word(self):
        """

        :return: 返回值是[(word,34),(word2,4456)]
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
        if len(wg_tmp) == 0 and len(wf_tmp) == 0:
            return []
        merge_tmp = self._merge_wordfreq_wgfreq(wf_tmp, wg_tmp)
        t = self.find_first_few(merge_tmp, 2)  # 找到融合分值最高的两个词
        # print('deal_has_same_etyma_word', t)
        return t


    def deal_has_diff_etyma_word(self):
        """

        :return: 处理没有词根词缀的词,找到构词能力和频率最高词merge最高分
        """
        # print(self.merge_wf_wgf)  # {'method': 496261.2, 'device': 577184.8}
        # print(self.word_merge_freq_order_dict)  # [(345653.60000000003, 'signal'), (339355.00000000006, 'data')]
        words = []

        while True:
            if len(self.word_merge_freq_order_dict) == 0:
                break
            t = self.word_merge_freq_order_dict[0]  # 取得融合分值最高的1个
            del(self.word_merge_freq_order_dict[0])
            if t[1] in self.ret_set:
                continue
            words.append(t)
            if len(words) >= 2:
                break
        # print(self.word_merge_freq_order_dict[:3])
        self.word_merge_freq_order_dict = words + self.word_merge_freq_order_dict  # 恢复词典
        # print(words)
        return words


    def get_next(self):
        """

        :return:
        """

        has_etyma = self.has_same_etyma_word()
        if has_etyma == True:  # 如果有词缀单词
            return self.deal_has_same_etyma_word()  # 处理同词缀单词
        else:
            return self.deal_has_diff_etyma_word()  # 处理不同词缀


    def sort_by_word_len(self, word_list):
        """
        根据词汇长度排序,音节数
        :param word_list:
        :return:
        """
        word_dict = dict()
        for word in word_list:
            word_dict[word] = len(word)
        sort_list2 = self.find_first_few(word_dict, len(word_dict))
        sort_list = list(map(lambda x:x[1], sort_list2))
        # print(sort_list, 'sort_list')
        return sort_list


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
            nw = self.get_next()  # 2个
            # print(nw)
            if len(nw) == 0:  # 没找到结果
                start_a = self.get_and_rm_word_freq_most()
                if start_a == '':
                    break
                self.word = start_a
                self.ret_set.add(start_a)
                ret_list.append(start_a)

                i += 1
                print(start_a, self.wfd[start_a], i)
                continue

            ret_result = []
            for nw_i in nw:
                # 有效排序结果
                if not nw_i in self.ret_set:
                    ret_result.append(nw_i)

            # 按音节数排序
            useful = list(map(lambda x:x[1], ret_result))
            sort_ret = self.sort_by_word_len(useful)
            # print('sort_ret', sort_ret)
            for word in sort_ret:
                self.ret_set.add(word)
                ret_list.append(word)
                i += 1
                # print(word,'word sort in')
                print(word, self.wfd[word], i)
            if len(sort_ret) != 0:
                # self.word = sort_ret[0]
                start_a = self.get_and_rm_word_freq_most()
                if start_a == '':
                    break
                self.word = start_a

        print(ret_list)
        util.write_file(MEDICAL_SORT_RET, '\n'.join(ret_list))

if __name__ == '__main__':
    # 初始化日志, 配置了基本的logger
    init_logging()
    deal = Deal()
    deal.sort()

