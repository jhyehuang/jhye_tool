# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 16:19:51 2018

@author: admin
"""

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-23 15:02:00
# Project: douban_music

from pyspider.libs.base_handler import *
import re

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://music.douban.com/top250?', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if re.match("https://music.douban.com/top250?", each.attr.href, re.U):
                self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        musics = response.doc('#content')('table')
        music_name=[]
        music_author=[]
        music_href=[]
        music_score=[]
        music_cimmit=[]
        for music in musics.items():
            music_name.append(music('div > a').text())
            music_author.append(music('div > p').text().split('/')[:2])
            music_href.append(music('div > a').attr('href'))
            music_score.append(music('div > div > span')(' .rating_nums').text().split(' ')[0])
            music_cimmit.append(music('div > div > span')(' .pl').text().split(' ')[1])
     
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "music_name":music_name,
            "music_author":music_author,
            "music_href":music_href,
            "music_score":music_score,
            "music_cimmit":music_cimmit,
          
        }
