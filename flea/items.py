# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HouseItem(scrapy.Item):

    # 用户名称
    username = scrapy.Field()
    # 手机号码
    phone = scrapy.Field()
    # 发布日期
    createDate = scrapy.Field()
    # 网站
    website = scrapy.Field()
    # 所属城市
    city = scrapy.Field()
    pass
