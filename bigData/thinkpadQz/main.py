from scrapy.cmdline import execute
import sys
import os
import schedule

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'thinkpad'])  # ����Ҫ���˴���spider_name�滻Ϊ���Լ�����������

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
        schedule.every(12).seconds.do('thinkpad1')

def thinkpad1():
    process = CrawlerProcess(get_project_settings())
    process.crawl('thinkpad')    #  ����Ҫ���˴���spider_name�滻Ϊ���Լ�����������
    process.start()



