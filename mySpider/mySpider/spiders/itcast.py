from ast import Str
from imp import reload
from mySpider.items import ItcastItem
import scrapy
import logging
import os
import sys

log_path = os.path.join(os.curdir,"example.log")

logging.basicConfig(filename=log_path, filemode='w', level=logging.DEBUG)


class ItcastSpider(scrapy.Spider):
    # 这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字
    name = 'itcast'
    # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只能爬取这个域名下的网页，不存在的url会被忽略
    allowed_domains = ['itcast.cn']
    
    # 爬取的url元组、列表，爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些url开始
    # 其他子url将会从这些起始url中继承性生成
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee',]

    # 解析的方法，每个初始url完成下载后将被调用，调用的时候传入从每一个url传回的response对象来作为唯一参数
    """
    负责解析返回的网页数据，提取结构化数据
    生成需要下一页的url请求
    将start_urls的值修改为需要爬虫的第一个url
    """
    def parse(self, response):
        
        items = []
        
        for each in response.xpath("//div[@class='li_txt']"):
            item = ItcastItem()
            
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()
            
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            
            items.append(item)
            
        return items
