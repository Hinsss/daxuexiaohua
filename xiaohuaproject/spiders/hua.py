# -*- coding: utf-8 -*-
import scrapy
from xiaohuaproject.items import XiaohuaprojectItem

class HuaSpider(scrapy.Spider):
    name = 'hua'
    allowed_domains = ['www.521609.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/']

    url = 'http://www.521609.com/daxuexiaohua/list3{}.html'
    page = 1

    def parse(self, response):
        li_list = response.xpath("//div[@class='index_img list_center']/ul/li")
        for oli in li_list:
            item = XiaohuaprojectItem()
            image_src = oli.xpath("./a/img/@src").extract_first()
            image_src = 'http://www.521609.com' + image_src
            name = oli.xpath("./a/img/@alt").extract_first().strip()
            item['image_src'] = image_src
            item['name'] = name
            yield item

        if self.page <= 10:
            self.page +=1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url,callback=self.parse)