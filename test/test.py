#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 15:12
# @Author  : HEHE
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')]
urllib.request.install_opener(opener)
url = 'http://m10.music.126.net/20180716155637/a94f36fecc5157479fd38ae89bf126ed/ymusic/b318/cab0/ed12/42f184d033c79481e9117242789baf75.mp3'
local_path = r'D:\music\4.mp3'
urllib.request.urlretrieve(url, local_path)







