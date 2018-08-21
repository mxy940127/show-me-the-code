# -*- coding:utf8 -*-

# **第 0003 题：** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。


import redis
import random
import string
import datetime

words = string.ascii_letters + string.digits

r = redis.Redis(host='localhost', port=6379, db=2)

def main(count, digit):
    for i in range(count):
        code = ''
        for k in range(digit):
            code = code + random.choice(words)
        try:
            r.set(i, code)
        except:
            print 'fail'


if __name__ == '__main__':
    main(200,10)
