# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from thinkpadQz.items import ThinkpadqzItem
import re




class ThinkpadSpider(CrawlSpider):
    name = 'thinkpad'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://search.jd.com/Search?keyword=thinkpad&qrst=1&ev=exbrand_ThinkPad%5E&pvid=727a43bea3244f41afc218843e57075e&page=3&s=57&click=0']

    # 1.LinkExtractor联接提取器,指定联接提取（alllow）
    link = LinkExtractor(allow=r'') #/Search?keyword=thinkpad&page=\d+

    rules = (
        #2.规则解析器
        #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #print(response)
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
        li_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        # all_data = []  # 存储所解析到的数据  //*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a
        for li in li_list:
            price = li.xpath('./div/div[2]/strong/i/text()').extract_first()
            model = li.xpath('./div/div[3]/a/em/text()').extract()
            model = ''.join(model)
            brand = model[model.rfind('联想'):11]
            # memory = re.findall(r"/d",model[0:model.rfind('G内存')][-3:],3)
            memory = model[0:model.rfind('内存')][-4:]
            print(model,memory)
            # print(price,model)
            item = ThinkpadqzItem()
            item['price'] = price
            item['model'] = model
            item['brand'] = brand
            item['memory'] = memory

            yield item   #将item提交给管道   print (a[a.rfind('联想'):11])

