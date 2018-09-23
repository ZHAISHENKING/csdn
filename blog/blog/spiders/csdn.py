# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from blog.items import UserItem, BlogItem


# 格式化空格及\n
def s_format(text):
    import re
    a = re.sub("\s", "", text)
    return a


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['https://blog.csdn.net/weixin_42042680/']

    def parse(self, response):
        item = UserItem()
        post = response.xpath('//div[contains(@class,"data-info")]')

        item["num"] = post.xpath('./dl[1]/dd//span/text()').get()
        item["fans"] = post.xpath('./dl[2]/dd//span/text()').get()
        item["like"] = post.xpath('./dl[3]/dd//span/text()').get()
        item["commit"] = post.xpath('./dl[4]/dd//span/text()').get()

        item["name"] = response.xpath('//a[@id="uid"]/text()').get()
        item["ranking"] = s_format(response.xpath('//div[@class="grade-box clearfix"]/dl[3]/dd/text()').get())
        item["integral"] = response.xpath('//div[@class="grade-box clearfix"]/dl[4]/dd/text()').get()
        item["look"] = s_format(response.xpath('//div[@class="grade-box clearfix"]/dl[2]/dd/text()').get().strip(' '))
        item["level"] = response.xpath('//div[@class="grade-box clearfix"]/dl[1]/dd/a/@title').get().split(',')[0]
        yield item
        num = 1
        url = "https://blog.csdn.net/weixin_42042680/article/list/%d" % num
        request = Request(url, callback=self.detail_parse, meta={"num": num})
        yield request

    def detail_parse(self, response):

        post = response.xpath('//div[contains(@class,"article-item-box")]')
        for i in post:
            item = BlogItem()
            item["is_origin"] = s_format(i.xpath('//a/span/text()').get())
            item["title"] = s_format(i.xpath('./h4//text()[2]').get())
            item["commit"] = i.xpath('//div[contains(@class,"info-box")]/p[3]/span/text()').get().split('：')[1].strip(' ')
            item["look"] = i.xpath('//div[contains(@class,"info-box")]/p[2]/span/text()').get().split("：")[1].strip(' ')
            item["create_time"] = i.xpath('//div[contains(@class,"info-box")]/p[1]/span/text()').get()
            yield item

