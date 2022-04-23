# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class MysteamSpider(CrawlSpider):
    name = 'mysteam'
    # allowed_domains = ['www.steam.com']
    start_urls = ['https://search.bilibili.com/all?keyword=python&from_source=webtop_search&spm_id_from=666.4']

    link = LinkExtractor(allow=r'')
    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        li_list = response.xpath('//*[@id="all-list"]')

        for li in li_list:
            gameName = li.xpath('./div[1]/div[2]/ul/li[1]/a').extract_first()
            gameNum = li.xpath('./div[1]/div[2]/ul/li[1]/div/div[3]/span[1]/text()').extract_first()
            print(gameName, gameNum)

            # model = li.xpath('./div/div[3]/a/em/text()').extract()
            # model = ''.join(model)
            # brand = model[model.rfind('联想'):11]
            # # memory = re.findall(r"/d",model[0:model.rfind('G内存')][-3:],3)
            # memory = model[0:model.rfind('内存')][-4:]
            # print(brand,memory)
            # print(price,model)
            # item = ThinkpadItem()
            # item['price'] = price
            # item['model'] = model
            # item['brand'] = brand
            # item['memory'] = memory

            # yield item   #将item提交给管道   print (a[a.rfind('联想'):11])
