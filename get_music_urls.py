#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 10:59
# @Author  : HEHE
# @Site    : 
# @File    : get_music_urls.py
# @Software: PyCharm

"""
该模块用于从各个版单中获取当日榜单，通过对已下载榜单对比，
下载未下载的音乐以及音乐歌词
"""

from urllib import request,parse,error
from Crypto.Cipher import AES
import base64
import pandas as pd
import datetime
import resource
import os
import re

def get_music_path():
    '''
    获取今天每个版单的path
    :return:
    '''
    list_path = resource.music_list_path
    music_list = os.listdir(list_path)                                  # 获取榜单名称
    print(music_list)
    print(len(music_list))
    for music_path in music_list:                                       # 获取榜单具体路径
        time = datetime.datetime.now().date()
        path = r'%s%s/%s.csv' % (list_path ,music_path , str(time))
        print(path)
        if os.path.exists(path):
            get_music_url(path)
        else:
            print('路径不存在：%s' % path )


def get_music_url(path):
    '''
    遍历表格获取musicid
    :param path:
    :return:
    '''
    f = open(path,'rb')
    music_matrix = pd.read_csv(f,index_col=0,header=None)
    music_url = music_matrix.iloc[:,0]
    for i, line in music_matrix.iterrows():
        pattern = re.compile(r'\d+')
        #print(i,i)
        id = re.findall(pattern,line[1])
        #print(i,i,i)
        #print(id)
        if len(id):
            mp3_url = get_mp3_url(id[0])                            # 时间暂停
            if mp3_url!= None:
                #print(i)
                download_mp3(mp3_url,line[2])
            else:
                print('id为：%s的歌曲需要下载权限'% id)







def aes_encrypt(data, g):
    '''
    用aes加密，再用base64  encode
    :param data:
    :param g:
    :return:
    '''
    iv = '0102030405060708'
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(g.encode('utf-8'),AES.MODE_CBC,iv.encode('utf-8'))
    encrypted = cipher.encrypt(pad(data).encode('utf-8'))  # aes加密
    result = base64.b64encode(encrypted)  # base64 encode
    return result


def get_mp3_url(id):
    '''
    从resource中获取相应的参数
    :return:
    '''
    text1 = aes_encrypt('%s%s%s' % (resource.d1,id,resource.d2),resource.g).decode()
    text2 = aes_encrypt(text1, resource.i)
    print(text2)
    data = bytes(parse.urlencode({'encSecKey': resource.enc, 'params': text2}), encoding='utf8')
    req = request.Request(resource.music_url, data=data, headers=resource.headers)
    try:
        response = request.urlopen(req, timeout=8)
    except Exception as e:
        #print(e.reason, e.code, e.headers, seq='\n')
        print('连接超时')
        return None
    str1 = response.read().decode()
    print(str1)
    pattern = re.compile(r'http.+\.mp3')
    mp3_url = re.search(pattern,str1[:])
    if mp3_url:
        return mp3_url[0]


def download_mp3(url,name):
    opener = request.build_opener()
    opener.addheaders = [('User-agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')]
    request.install_opener(opener)
    local_path = resource.local_path
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    path =local_path + str(name) + '.mp3'
    try:
        if not os.path.exists(path):
            #print('歌曲，正在下载：%s ' % name)
            request.urlretrieve(url, path)
            print('歌曲，已下载完成：%s ' % name)
        else:
            pass
            #print('歌曲，已经下载过了：%s ' % name)
    except Exception as e:
        pass
        #print('歌曲，下载出错：%s 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111' % name)





if __name__ == '__main__':
    get_music_path()