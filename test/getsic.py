#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 9:37
# @Author  : HEHE
# @Site    : 
# @File    : get_music_url.py
# @Software: PyCharm

from Crypto.Cipher import AES
import base64
from urllib import request,parse,error


def length_16():
    pass


# 用aes加密，再用base64  encode
def aes_encrypt(data, g):
    iv = '0102030405060708'
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(g.encode('utf-8'),AES.MODE_CBC,iv.encode('utf-8'))
    encrypted = cipher.encrypt(pad(data).encode('utf-8'))  # aes加密
    result = base64.b64encode(encrypted)  # base64 encode
    return result



if __name__ == '__main__':
    d = '{"ids":"[1294889112]","br":128000,"csrf_token":""}';e = '010001';
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7';
    g = '0CoJUm6Qyw8W8jud'
    i = 'jKlchtX8XMzRiJS8'

    text1 = aes_encrypt(d,g).decode()
    text2 = aes_encrypt(text1, i)
    print(text2)
    print(text2.decode())
    enc = '813a6937caf2823fcb0c473d54301aaea41a3d481a1cced332d2a5939d01213ebe7b173c60469404455f1a6660a4637068aaf384d9ed6f1933bec05f8bf739a58568f373fc6215e3b9ef78dff4678d9b1b6ac79717f61f9db817ad230ba3913e66885963b5785905f91dfef03ec28ef3213f718a8a10509d7ac710407bca5c8c'
    text2 = 'TUoqJX525JI/X/6SjmAmDeIULQwcZQNifzBH2QNRpkgKQJG3z1xqJK8tAXM6PgNNNWxtABn1lS9krVpdoMAMZVfLp04QB1zM5GwRVUyfL6J68pCzOViiv487077Pu2c6'
    data = bytes(parse.urlencode({'encSecKey':enc,'params':text2.encode() }),encoding='utf8')
    #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
     #          'Content-Type':'application/x-www-form-urlencoded'}
    headers = {
        'Host':'music.163.com',
        'Connection': 'keep-alive',
        'Origin': 'https://music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'https://music.163.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    req = request.Request('https://music.163.com/weapi/song/enhance/player/url?csrf_token=',data =data,headers = headers )
    try:
        response = request.urlopen(req)
    except error.HTTPError as e:
        print(e.reason,e.code,e.headers,seq = '\n')
    print(response.status)
    print(response.read())
    print(response.url)




