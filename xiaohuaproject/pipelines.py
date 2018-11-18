# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import urllib
class XiaohuaprojectPipeline(object):
    def __init__(self):
        self.fp = open('hua.txt','w',encoding='utf8')

    def process_item(self, item, spider):
        self.download_image(item)
        obj  = dict(item)
        s = json.dumps(obj,ensure_ascii=False)
        self.fp.write(s + '\n')
        return item

    def download_image(self,item):
        dirpath = os.getcwd()+'\\img'
        filename = item['name'] + '.jpg'
        filepath = os.path.join(dirpath,filename)
        urllib.request.urlretrieve(item['image_src'],filepath)

    def close_spider(self,spider):
        self.fp.close()