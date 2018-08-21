# -*- coding:utf8 -*-

# **第 0002 题:** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。


import MySQLdb as mdb
import random
import string
import datetime

words = string.ascii_letters + string.digits

def create_table():
    db = mdb.connect("localhost","root","root","testdb", charset='utf8')
    cursor = db.cursor()
    cursor.execute("drop table if exists activation_code")
    sql = """
            CREATE TABLE `activation_code` (
              `id` int(10) NOT NULL,
              `code` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
              `time` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
              PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
          """
    cursor.execute(sql)
    db.close()

def main(count, digit):
    db = mdb.connect("localhost","root","root","testdb", charset='utf8')
    cursor = db.cursor()
    for i in range(count):
        code = ''
        for k in range(digit):
            code = code + random.choice(words)
        try:
            now_time = datetime.datetime.now()
            cursor.execute('insert into activation_code values("%d", "%s", "%s")' % (i, code, now_time.strftime('%Y-%m-%d %H:%M:%S')))
            db.commit()
        except:
            db.rollback()
    db.close()


if __name__ == '__main__':
    create_table()
    main(200,10)
