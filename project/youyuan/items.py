# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class YouyuanItem(Item):
    name=Field()      #姓名
    address = Field() #地址
    age = Field()     #年龄
    height = Field()  #身高
    salary = Field()  #收入
    house = Field()   #房子
    hobby = Field()   #爱好
    image = Field()   #照骗
    motto = Field()   #内心独白
    detail = Field()  #详细资料
    boy_condition = Field() #男友标准
    url=Field()       #个人主页
