## 结果
该结果为 同词缀， 频率,构词能力merge后按音节数排序的结果，但是貌似排序结果被频率和词缀左右了。
[sort_result_1.txt](data_pre_handle/sort_result_1.txt)
[sort_result_2.txt](data_pre_handle/sort_result_2.txt)
## 需求
![](https://gitee.com/hailinli/blogNote/raw/master/%E5%85%B6%E4%BB%96/%E8%8D%A3%E5%B2%A9%E8%AE%BA%E6%96%87/README_md_1.png)
## 数据
1. 百度云盘：链接: https://pan.baidu.com/s/1LwwktAMUY6bIQOpbnFdKtA 密码: 35tp
2. 词根词缀：http://note.youdao.com/noteshare?id=a73b3da1c8bb2b33426f1b936b8ae706
3. 词频：http://note.youdao.com/noteshare?id=e6e3b39b575cacd740251295de75521f
## 设计思路

==**提出思路**==
```
graph LR
A[排序]
B1[词频]
B2[词根词缀]
B3[词汇关联度]
B4[词汇长度]
C11[UMLS-词频.txt-medical词典做筛选->score]
C21[根据词频划分小集合]
C31[从句子里抽取距离比较近的medical word,形成词对,设置窗口]
C32[词对向量化one-hot并降维处理]
C33[word2vec处理,求关联度,UMLS短语权重加大->score]
C41[词汇长度->score]
D1[规则]
D2[随机森林]

A---B1
A---B2
A---B3
A---B4
B1---C11
B2---C21
B3---C31
B3---C32
B3---C33
B4---C41
C41-->|input|D1
C33-->|input|D1
C11-->|input|D1
C41-->|input|D2
C33-->|input|D2
C11-->|input|D2

```
1. 规则
2. 随机森林


==**老师建议**==

录音：http://note.youdao.com/noteshare?id=767e2c5e3390250e2ce56319f82c2688

特征
1. 词频
2. 词根词缀，词汇拆解成词根词缀(重要性高，构词能力更强)
3. 词组，整体频率(词能不能和其他词组合在一起，表达能力更高)
4. 关联词汇，词汇造词能力
5. 词汇长度，音节数

特征集描述词的重要性
- 唯一性价值排序，难
- 一组的数据刻画词的价值，规则方法必要的时候进行挑选，先按类分组，后排序
- 归一化，加权平均

==**最终**==

![](https://gitee.com/hailinli/blogNote/raw/master/%E5%85%B6%E4%BB%96/%E8%8D%A3%E5%B2%A9%E8%AE%BA%E6%96%87/README_md_2.jpg)

1. 医学单词词频-->UMLS语料库
2. 医学词根词频 --> 医学单词词频

## 参考论文
1. [英语词汇自适应测试系统中词汇难度的判定_胡一平](http://note.youdao.com/noteshare?id=a8fb84755ed8c7ffc376d0865f1403c1)
