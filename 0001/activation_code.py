# -*- coding:utf8 -*-

# **第 0001 题：** 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random
import string

words = string.ascii_letters + string.digits

def main(count, digit):
    for i in range(count):
        code = ''
        for x in range(digit):
            code = code + random.choice(words)
        print code

if __name__ == '__main__':
    main(200,10)
