#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: pipelines.py
# @Author: lio
# @Date: 2018-01-22
from tieba.items import TiebaItem
from .sql import Sql

class TiebaPipeline(object):

    def process_item(self, item, spider):
        if item.__class__ == TiebaItem:
            ex = Sql()
            ex.insert_tieba_header(item)
        else:
            pass

