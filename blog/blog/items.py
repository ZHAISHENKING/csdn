# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    # 个人相关信息
    name = scrapy.Field()
    num = scrapy.Field()
    fans = scrapy.Field()
    like = scrapy.Field()
    commit = scrapy.Field()
    level = scrapy.Field()
    look = scrapy.Field()
    ranking = scrapy.Field()
    integral = scrapy.Field()


class BlogItem(scrapy.Item):
    title = scrapy.Field()
    create_time = scrapy.Field()
    look = scrapy.Field()
    commit = scrapy.Field()
    is_origin = scrapy.Field()