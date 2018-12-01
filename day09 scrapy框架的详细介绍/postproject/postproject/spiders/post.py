# -*- coding: utf-8 -*-
import scrapy


class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['fanyi.baidu.com']
    # start_urls = ['http://fanyi.baidu.com/']

    def start_requests(self):
    	post_url = 'http://fanyi.baidu.com/sug'
    	# 表单数据
    	formdata = {
    		'kw': 'wolf',
    	}
    	# 发送请求
    	yield scrapy.FormRequest(url=post_url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        print('*' * 50)
        print(response.text)
        print('*' * 50)
