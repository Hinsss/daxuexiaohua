# -*- coding: utf-8 -*-
import scrapy
from xiaohuaproject.items import XiaohuaprojectItem

class HuaSpider(scrapy.Spider):
    name = 'hua'
    allowed_domains = ['www.521609.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/']

    # 爬取每一页
    url = 'http://www.521609.com/daxuexiaohua/list3{}.html'
    page = 1

    def parse(self, response):
        # 解析内容,先查找所有的li标签
        li_list = response.xpath('//div[@class="index_img list_center"]/ul/li')
        # 遍历li_list，依次获取每个图片的链接和名字
        for oli in li_list:
        	# 创建一个item对象
        	item = XiaohuaprojectItem()
        	# 获取图片链接
        	image_src = oli.xpath('./a/img/@src').extract_first()
        	image_src = 'http://www.521609.com' + image_src
        	# 获取图片名字
        	name = oli.xpath('./a/img/@alt').extract_first().strip()
        	item['image_url'] = image_src
        	item['name'] = name
        	yield item

        if self.page <= 57:
        	self.page += 1
        	url = self.url.format(self.page)
        	yield scrapy.Request(url=url, callback=self.parse)

