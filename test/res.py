#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 14:36
# @Author  : HEHE
# @Site    : 
# @File    : resource.py
# @Software: PyCharm


from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex
from urllib import request,parse,error

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
# 一定要注意井号的问题井号
url = 'https://music.163.com/discover/toplist?id=2250011882'
req = request.Request(url,headers = headers )
try:
    response = request.urlopen(req)
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, seq='\n')
print(response.status)
print(response.read().decode('utf-8'))
print(response.url)
