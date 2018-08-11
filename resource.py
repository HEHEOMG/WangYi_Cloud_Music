#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 18:21
# @Author  : HEHE
# @Site    : 
# @File    : resource.py
# @Software: PyCharm

UserAgent = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

CloudMusic_List_URL = 'https://music.163.com'                            # 网易云音乐主页

music_list_path = r'resource/music_list/'                                # 版单存放路径

d1 = '{"ids":"['
d2 = ']","br":128000,"csrf_token":""}'
e = '010001'
g = '0CoJUm6Qyw8W8jud'
i = 'jKlchtX8XMzRiJS8'
enc = '5ac3be6ba236e21cdc30c25179149f8578095e05e206ee923b2ef59b02b2d8f2295c84a45489c6dd1c198dbdb820e795ac35e6f64079b9a5c958319092c0bf2c9b2e4ac391d8ed2bef4a4f029103fc7e229d1992d3d57b0bcf17dedd9cb259fe12afef25096d078517fb097bca6d2fdb16e24895f99ee64507dcb9db8015ddb7'


headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
   'Content-Type': 'application/x-www-form-urlencoded'}

music_url =r'https://music.163.com/weapi/song/enhance/player/url?csrf_token='


local_path = r'resource/music/'
