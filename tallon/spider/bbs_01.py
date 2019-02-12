# -*- coding: utf-8 -*-
# @Time    : 2018-02-29 00:16
# @Author  : YangBo
# @File    : test_tieba.py

# 需求：输入贴吧名称、起始页码、结束页码，
#      在当前文件夹中新建一个以吧名为名字的📁，里面是每一页的HTML内容

import urllib.parse
import os


url = 'http://tieba.baidu.com/f?ie=utf-8&'

ba_name = input("请输入要爬取的吧名：")
start_page = int(input('请输入要爬取的起始页码：'))
end_page = int(input('请输入要爬取的结束页码：'))

# 如果不存在则创建📁
if not os.path.exists('../'+ba_name):
    os.mkdir('../'+ba_name)

# 循环，依次爬取每一页的数据
for page in range(start_page, end_page + 1):
    data = {
        'kw': ba_name,
        'pn': (page - 1) * 50,
    }
    data = urllib.parse.urlencode(data)
    # 生成指定URL
    url_t = url + data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    request = urllib.request.Request(url=url_t, headers=headers)
    print('第%s页开始下载···' % page)
    response = urllib.request.urlopen(request)
    # 生成文件名
    fileName = ba_name + "_" + str(page) + ".html"
    #  拼接文件路径
    filePath = '../' + ba_name + '/' + fileName
    # 写内容
    with open(filePath, 'wb') as fp:
        fp.write(response.read())
    print('第%s页下载完成···' % page)
