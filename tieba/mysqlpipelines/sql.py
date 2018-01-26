#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: sql.py
# @Author: lio
# @Date: 2018-01-22
import MySQLdb
from twisted.enterprise import adbapi

from tieba import settings
from tieba.items import TiebaItem
from scrapy import log

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB



class Sql(object):
    def __init__(self):
        #log.INFO("开始连接")

        self.connect = MySQLdb.connect(
            host = '127.0.0.1', #MYSQL_HOSTS,
            db = 'spider', #MYSQL_DB,
            user = 'root', #MYSQL_USER,
            passwd = 'root', #MYSQL_PASSWORD,
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()

    def insert_tieba_header(self, item):
        try:
            self.cursor.execute("""insert into tieba_theme_header(reply_num, theme, theme_site, theme_author, create_date, content, replyer, reply_date) values (%s, %s, %s, %s, %s, %s, %s, %s)""",
                                (item['reply_num'],
                                 item['theme'],
                                 item['theme_site'],
                                 item['theme_author'],
                                 item['create_time'],
                                 item['content'],
                                 item['replyer'],
                                 item['reply_date']
                                 ))
            self.connect.commit()
        except Exception as error:
            print(error)