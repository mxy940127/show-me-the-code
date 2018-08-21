# -*- coding:utf8 -*-

# 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)


import requests
import lxml.html
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/2166231880'

def main():
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
    list = soup.select('img.BDE_Image')
    for i in range(len(list)):
        with open('image/%d.jpg' % i, 'wb') as f:
            f.write(requests.get(list[i]['src']).content)
            f.close()

if __name__ == '__main__':
    main()
