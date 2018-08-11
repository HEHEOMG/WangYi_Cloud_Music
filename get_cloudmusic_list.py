#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 18:19
# @Author  : HEHE
# @Site    : 
# @File    : cloudmusic_list.py
# @Software: PyCharm

"""
该模块用于从网易云排行版入口获取多个排行版的URL，
对各个排行版进行遍历解析，获取每日的排行版内容并按日期存储排行版的版单

"""


from bs4 import BeautifulSoup
import resource
import urllib
import csv
import os
import datetime


def get_html(url):
    '''
    该方法用于请求榜单页面
    :param url:
    :return:
    '''
    req = urllib.request.Request(url,headers = resource.UserAgent)       # 设置请求头
    try:
        response = urllib.request.urlopen(req)                           # 请求页面
    except urllib.error.HTTPError as e:
        print(e.reason, e.code, e.headers, seq='\n')
    return response



def get_list_id():
    '''
    从榜单页面获取各个榜单的id
    :return: 榜单id列表
    '''
    list_url = resource.CloudMusic_List_URL                              # 获取初始榜单URL
    html = get_html(list_url + '/discover/toplist')
    soup = BeautifulSoup(html.read().decode('utf-8'), 'lxml')            # 创建BeautifulSoup对象
    soup_list = soup.find_all('li',class_='mine')                        # 匹配榜单列表相应模块
    list_id = []                                                         # list_id用于存放榜单列表
    try:
        for soup_part in soup_list:
            list_id.append(soup_part.a.get('href'))
    except Exception as e:
        print('榜单列表获取失败')
    print('榜单列表获取成功')
    return list_id


def parse_list_info(list_id):
    '''
    获取每一个榜单列表的信息并将其存储到csv文件中
    :param list_id:
    :return:
    '''
    for id in list_id:                                                   # 遍历各大排行版
        url = resource.CloudMusic_List_URL + id
        html = get_html(url)
        info_to_csv(html)                                                # 获取排行版具体信息


def info_to_csv(html):
    '''
    获取排行版各种信息，包括排行版名称，排行列表
    :param html:
    :return:
    '''
    soup = BeautifulSoup(html.read().decode('utf-8'), 'lxml')            # 创建BeautifulSoup对象
    title = soup.title.string
    print(soup.title.string)
    dir_name = resource.music_list_path + title
    get_time = datetime.datetime.now().date()
    if not os.path.exists(dir_name):                                     # 判断排行版是否存在，不存在则创建一个
        os.makedirs(dir_name)
    path = dir_name + '/'+ str(get_time) + '.csv'                        # 当前日期排行版地址
    soup_music_list =soup.find('ul',class_='f-hide')                     # 筛选歌单列表
    each_music = soup_music_list.contents                                # 获取歌单列表
    if os.path.exists(path):
        os.remove(path)
        print('先删除：%s' % path)
    with open(path,'a',newline='',encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for i, music in enumerate(each_music,start = 1):
            csv_writer.writerow([i,music.a.get('href'),music.a.string])  # 列表按行写入




if __name__ == '__main__':
    list_id = get_list_id()                                              # 获取榜单列表
    parse_list_info(list_id)                                             # 获取相应榜单列表信息




