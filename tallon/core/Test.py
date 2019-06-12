# -*- coding: utf-8 -*-
# @Time    : 2019-02-12 22:26
# @Author  : YangBo
# @File    : Test.py

# 一行代码的99乘法表
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))

# 一行代码实现排序
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])