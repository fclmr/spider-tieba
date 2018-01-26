#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: teiba_spider.py
# @Author: lio
# @Date: 2018-01-19

import scrapy

from tieba.items import TiebaItem


class TiebaSpider(scrapy.Spider):

    name = "tieba"
    allowed_domains = [
        'tieba.baidu.com'
    ]

    start_urls =[
        #'http://tieba.baidu.com/f?kw=%E6%98%BE%E5%8D%A1&fr=index&red_tag=j2179617181',
        'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%85%A8%E5%A2%83%E5%B0%81%E9%94%81&fr=search',
    ]




    def parse(self, response):

        li_list = response.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div')
        for li in li_list:
            item = TiebaItem()
            item['reply_num'] = li.xpath('div["col2_left j_threadlist_li_left"]/span[@title="回复"]/text()').extract_first()
            item['theme'] = li.xpath('div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract_first()
            item['theme_site'] = li.xpath('div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@href').extract_first()
            item['theme_author'] = li.xpath('div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author "]/@title').extract_first()
            item['create_time'] = li.xpath('div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="pull-right is_show_create_time"]/text()').extract_first()
            item['content'] = li.xpath('div["col2_right j_threadlist_li_right "]/div["threadlist_detail clearfix"]/div["@class=threadlist_text pull_left"]/div/text()').extract_first()
            item['replyer'] = li.xpath('div["col2_right j_threadlist_li_right "]/div["threadlist_detail clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author_rely j_replyer"]/@title').extract_first()
            item['reply_date'] = li.xpath('div["col2_right j_threadlist_li_right "]/div["threadlist_detail clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="threadlist_reply_date pull_right j_reply_data"]/text()').extract_first()
            yield item

        # 下一页
        num = int(response.xpath('//*[@id="frs_list_pager"]/span[@class="pagination-current pagination-item "]/text()').extract_first())
        if num <= 10:
            next_page = response.xpath('//*[@id="frs_list_pager"]/a[@class="next pagination-item "]/@href').extract_first()
            print("next_page, %s", next_page)
            print(num)
            if next_page is not None:
                yield response.follow(next_page, self.parse)

        # 回复
        # //*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div["col2_left j_threadlist_li_left"]/span[@title="回复"]/text()')
        # 主题
        # //*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit  member_thread_title_frs "]/a/@href
        # //*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit  member_thread_title_frs "]/a/@title
        # 作者
        # //*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author no_icon_author"]/@title
        # 创建时间
        # //*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="pull-right is_show_create_time"]/text()
        # 内容
        # //*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div["col2_right j_threadlist_li_right "]/div["threadlist_detail clearfix"]/div["@class=threadlist_text pull_left"]/div/text()
        # 最后回复人
        # //*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div["col2_right j_threadlist_li_right "]/div["threadlist_detail clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author_rely j_replyer"]/@title
        # 最后回复时间
        # //*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div["col2_right j_threadlist_li_right "]/div["threadlist_detail clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="threadlist_reply_date pull_right j_reply_data"]/text()'
        def getInfo(self, response):
            print("存入信息")
            li_list = response.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div')
            for li in li_list:
                item = TiebaItem()
                item['reply_num'] = li.xpath(
                    'div["col2_left j_threadlist_li_left"]/span[@title="回复"]/text()').extract_first()
                item['theme'] = li.xpath(
                    'div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract_first()
                item['theme_site'] = li.xpath(
                    'div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@href').extract_first()
                item['theme_author'] = li.xpath(
                    'div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author "]/@title').extract_first()
                item['create_time'] = li.xpath(
                    'div["col2_right j_threadlist_li_right "]/div["threadlist_lz clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="pull-right is_show_create_time"]/text()').extract_first()
                item['content'] = li.xpath(
                    'div["col2_right j_threadlist_li_right "]/div["threadlist_detail clearfix"]/div["@class=threadlist_text pull_left"]/div/text()').extract_first()
                item['replyer'] = li.xpath(
                    'div["col2_right j_threadlist_li_right "]/div["threadlist_detail clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author_rely j_replyer"]/@title').extract_first()
                item['reply_date'] = li.xpath(
                    'div["col2_right j_threadlist_li_right "]/div["threadlist_detail clearfix"]/div[@class="threadlist_author pull_right"]/span[@class="threadlist_reply_date pull_right j_reply_data"]/text()').extract_first()
                yield item
