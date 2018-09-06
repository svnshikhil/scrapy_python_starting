# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from elasticsearch import Elasticsearch
# import json
# import configparser
# config = configparser.RawConfigParser()
# config.read('scrapy.cfg')
# eshost = config.get('elasticsearch', 'host')
# esport = config.get('elasticsearch', 'port')
#
# es = Elasticsearch([{'host': eshost, 'port': esport}])

class TutorialPipeline(object):
    def process_item(self, item, spider):
        print('RESP=====>',item)
        # es.index(index='scrapy_test', doc_type='doc', body=dict(item))
        return item
