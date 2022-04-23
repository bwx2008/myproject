# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import twisted

# class QiubaiproPipeline(object):
#     fp = None
#     def open_spider(self,spider):
#         print('爬虫开始！')
#         self.fp = open('./qiubai.txt','w',encoding='utf-8') #,encoding='utf-8'
#
#     def process_item(self, item, spider):
#         author = item['author']
#         content = item['content']
#
#         self.fp.write(author+':'+content+'\n')
#         return item
#     def close_spider(self,spider):
#         print('爬虫结束！')
#         self.fp.close()

class mysqlPileLine():
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='localhost',port=3306,user='root',password='123',db='mysqldb',charset='utf8')
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute('insert into qiubai values("%s","%s")'%(item["author"],item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        def close_spider(self,spider):
            self.cursor.close()
            self.conn.close()