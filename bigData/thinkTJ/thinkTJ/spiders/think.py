# -*- coding: utf-8 -*-
import scrapy
from thinkTJ.items import ThinktjItem


class ThinkSpider(scrapy.Spider):
    name = 'think'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://search.jd.com/Search?keyword=thinkpad&enc=utf-8&wq=thinkpad&pvid=3cab24375cd94aa68446968df0bf8882']

    def parse(self, response):
        li_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        # all_data = []  # 存储所解析到的数据
        for li in li_list:
            price = li.xpath('./div/div[2]/strong/i/text()').extract_first()
            model = li.xpath('./div/div[3]/a/em/text()').extract()
            model = ''.join(model)
            print(model)
            # print(price,model)
            item = ThinktjItem()
            item['price'] = price
            item['model'] = model

            yield item   #将item提交给管道