# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymysql
import json
# from twisted.enterprise import adbapi

class YouyuanPipeline(object):

    # def __init__(self):
    #     dbparams = {
    #         'host': '',
    #         'user': '',
    #         'password': '',
    #         'database': '',
    #         'charset': 'utf8',
    #         'cursorclass': pymysql.cursors.DictCursor
    #     }
    #     self.adpool = adbapi.ConnectionPool('pymysql', **dbparams)
    #     self._sql = None
    #     # self.conn = pymysql.connect(**dbparams)
    #     # self.cursor = self.conn.cursor()
    #
    # @property
    # def sql(self):
    #     if not self._sql:
    #         self._sql = '''insert into youyuan(name,address,age,height,salary,house,hobby,image,
    #         motto,detail,boy_condition,url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    #     return self._sql

    def process_item(self, item, spider):
        pass
        # if spider.name == 'yy':
        #     print(item)
        #     defer = self.adpool.runInteraction(self.insert_item, item)  # 需要传一个真正导入数据库操作的函数给它，不然跟同步下载一样
        #     defer.addErrback(self.handle_error, item, spider)  # 添加一个接收错误信息的函数
        #     # self.conn.commit()
        return item

    # def insert_item(self,cursor,item):
    #     cursor.execute(self.sql,[item['name'],item['address'],item['age'],item['height'],item['salary'],
    #                          item['house'],json.dumps(item['hobby'],ensure_ascii=False),json.dumps(item['image'],ensure_ascii=False),item['motto'],
    #                          json.dumps(item['detail'],ensure_ascii=False),
    #                          json.dumps(item['boy_condition'],ensure_ascii=False),item['url']])
    #
    # def handle_error(self, error,item, spider):
    #     print('-' * 30)
    #     print('Error:', error)
    #     print('-' * 30)
    # # def close_spider(self):
    # #     self.cursor.close()
    # #     self.conn.close()
