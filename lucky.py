#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, sys, bs4, webbrowser

print("googling........")
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()  # エラーがあれば例外を発生させる
noSoup = bs4.BeautifulSoup(res.text, 'html.parser') 
print(noSoup) #  beautifulsoup4オブジェクトとして取り込む
link_elems = noSoup.select('.r a') # タグの取得
num_open = min(5, len(link_elems))
for i in range(num_open):

    webbrowser.open('https://www.google.com' + link_elems[i].get('href'))  # タグのリンクを取得
    #print(link_elems[i].get('href'))  # タグのリンクを取得
    #print(link_elems[i].getText())  # タグのテキストを取得


#  Googleの検索結果をうまく取得できなくなっている。市販の有料のAPIがあるようだ。