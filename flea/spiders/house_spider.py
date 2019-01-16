# -*- coding: utf-8 -*-
import scrapy

from datetime import date, timedelta

from flea.items import HouseItem

class HouseSpiderSpider(scrapy.Spider):
    # 第一种类型网站
    name = "house_spider"
    # 入口url, 扔到调度器里面去, 通知引擎, 调用下载器下载, 用parse解析返回的数据
    start_urls = []

    def start_requests(self):
        # 逐行读取文件
        with open('../files/website.txt', 'r') as f:
            for l in f:
                if not l.startswith('#'):
                    # 获得 url 路径
                    domain = l.rstrip('\n').rstrip().split('\t')[0].split('@')[1]
                    url = domain + "/post/fangwu/chuzu/gr/list-0-0-0-0-0-2-1-0-0-0-0-0.html"
                    request = scrapy.Request(url=url, callback=self.parse)
                    request.meta['domain'] = domain
                    yield request

    # 默认的解析方法
    def parse(self, response):
        domain = response.meta['domain']

        # 获得昨天日期
        yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
        # 列表页面
        house_list = response.xpath("//ul[@class='zf_list']/li")
        count = 0
        hasNextPage = False
        for index in range(0, len(house_list) - 1, 1):
            createDate = house_list[index].xpath(".//div[@class='fccc']/span[last()]/text()").extract_first()
            if index == len(house_list) - 1 and (createDate == "今天" or createDate == yesterday):
                hasNextPage = True
            if createDate == yesterday:
                count = count + 1
                link = house_list[index].xpath(".//div[@class='esfcen']//a/@href").extract_first()
                request = scrapy.Request(domain + link, callback=self.parse_details, dont_filter=True)
                request.meta['createDate'] = createDate
                request.meta['website'] = domain
                yield request

        # 解析下一页数据
        next_link = response.xpath("//div[@id='page_x']/a[contains(text(),'下一页')]/@href").extract()
        if next_link and hasNextPage:
            next_link = next_link[0]
            yield scrapy.Request(domain + next_link, callback=self.parse)

    def parse_details(self, response):
        house_item = HouseItem()
        house_item["username"] = response.xpath("//div[@class='smleft']//dd[7]/text()").extract_first()
        house_item["phone"] = response.xpath("//div[@class='smleft']//dd[8]/i/text()").extract_first()
        house_item["createDate"] = response.meta['createDate']
        house_item["website"] = response.meta['website']
        city = response.xpath("//div[@class='fenleiq']/a[1]/text()").extract_first()
        house_item["city"] = city.replace("首页", "")

        # 将数据 yield 到 pipelines 里面
        yield house_item





