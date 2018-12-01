# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib.request
import json

class XiaohuaprojectPipeline(object):
    def __init__(self):
        self.fp = open('hua.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        # 下载图片
        self.download_image(item)

        obj = dict(item)
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def download_image(self, item):
        # 指定下载的路径
        dirpath = r'C:\Users\ZBLi\Desktop\1801\day09\xiaohua'
        filename = item['name'] + '.jpg'
        filepath = os.path.join(dirpath, filename)
        urllib.request.urlretrieve(item['image_url'], filepath)

    def close_spider(self, spider):
        self.fp.close()
