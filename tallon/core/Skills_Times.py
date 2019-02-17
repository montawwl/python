# -*- coding: utf-8 -*-
# @Time    : 2019-02-17 15:40
# @Author  : YangBo
# @File    : Skills_Times.py

# 统计某个人名在书中出现的次数
print("《朝闻道》中人物出场次数")
import jieba
import time

start = time.perf_counter()
txt = open("朝闻道.txt","r",encoding="GBK").read()
excludes = {"宇宙","一个","他们"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word)==1:
        continue
    elif word=="主角":
        rword="丁仪"
    elif word=="角色":
        rword="牛顿"
    else:
        rword=word
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}次".format(word,count))
dur=time.perf_counter()-start
print("运行时间为{:.2f}s".format(dur))
print("--------------------------")
