# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 回复数
    reply_num = scrapy.Field()
    # 主题
    theme = scrapy.Field()
    # 地址
    theme_site = scrapy.Field()
    # 主题作者
    theme_author = scrapy.Field()
    # 创建时间
    create_time = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 最后回复人
    replyer = scrapy.Field()
    # 最后回复时间
    reply_date = scrapy.Field()
