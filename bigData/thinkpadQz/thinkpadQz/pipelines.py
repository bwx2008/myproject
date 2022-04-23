# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from itemadapter import ItemAdapter
import pymysql
import re

class ThinkpadqzPipeline(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='localhost',port=3306,user='root',password='123',db='mysqldb',charset='utf8')
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()

        try:
            if item["memory"] != item["model"][-5:-1]:
                  self.cursor.execute('insert into thinkpad values("%s","%s","%s","%s")'%(item["price"],item["model"],item["brand"],re.sub("\D","",item["memory"])))
                  self.conn.commit()
        except Exception as e:
            print(e)
        def close_spider(self,spider):
            self.cursor.close()
            self.conn.close()
