import scrapy
from qiubaiPro.items import QiubaiproItem
import twisted

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text']

    # def parse(self, response):
    #     div_list=response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []  # 存储所解析到的数据
    #     for div in div_list:
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first() #////*[@id="qiushi_tag_124879110"]/div[1]/a[2]/h2
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         print(author,content)
    #         dic = {
    #             'author':author,
    #             'content':content
    #         }
    #         all_data.append(dic)
    #     return all_data
    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        # all_data = []  # 存储所解析到的数据
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item   #将item提交给管道