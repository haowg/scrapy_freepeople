# -*- coding: utf-8 -*-
import urllib
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.request import Request

from x.items import XItem


class FreepeopleSpider(CrawlSpider):
    name = 'freepeople'
    allowed_domains = ['freepeople.com']
    start_urls = ['http://www.freepeople.com/whats-new/']
    cookie_json = json.loads(file('cookie.us').read())

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies=self.cookie_json)

    rules = (
        Rule(LinkExtractor(allow=r'http://www.freepeople.com/whats-new/.*startResult.*'), callback='parse_item',follow=True),
    )

    #获取列表页的信息
    def parse_item(self, response):
        f = open('x.html','w')
        sits = response.xpath("//li[@class='thumbnail--large thumbnail']")
        print len(sits)
        for sit in sits:
            item = XItem()
            item['name'] = sit.xpath('.//h3/a/text()').extract()[0]
            item['URL'] = sit.xpath('.//h3/a/@href').extract()
            item['cover_image'] = sit.xpath('./div/div/a/img/@src').extract()
            detail_url = sit.xpath('.//h3/a/@href').extract()[0]
            yield scrapy.Request(detail_url, callback=self.get_detail, meta={'item': item})

    def download_image(self, url):
        return urllib.urlopen(url).read()

    #获取详情页的信息，并返回item
    def get_detail(self, response):
        i = response.meta['item']
        images_detail_alt = response.xpath('//*[@class="alternates clearfix"]/ul/li/a/img/@src').extract()
        images_zoom_super = [url.replace('detail-alt','zoom-super') for url in images_detail_alt]
        #images = [self.download_image(url) for url in images_zoom_super]
        #i['image_in_full_size'] = images
        i['image_in_full_size'] = images_zoom_super
        i['Available_sizes'] = list(set(response.xpath('//ul[starts-with(@class,"size")]/li[not(starts-with(@class,"una"))]/a/span/text()').extract()))
        i['description'] = response.xpath('//div[@class="long-desc"]/text()').extract()[0].strip()
        yield i
