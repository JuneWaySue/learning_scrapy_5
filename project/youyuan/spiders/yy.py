# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider
from youyuan.items import YouyuanItem
import re

# 这个函数是用于处理详细资料和征友条件的，返回一个字典
def process_data(data):
    key = data[::2]
    value = [re.sub(' ','',i) for i in data[1::2]]
    return dict(zip(key, value))


# class YySpider(CrawlSpider):
class YySpider(RedisSpider):
    name = 'yy'
    allowed_domains = ['youyuan.com']
    # start_urls = ['http://www.youyuan.com/city/']

    redis_key = 'yy:start_urls'
    # next_page_link=LinkExtractor(allow=r'/find/guangdong/mm18-25/advance-0-0-0-0-0-0-0/p\d+/')
    # detail_link=LinkExtractor(allow=r'/\d+-profile/')
    # rules = (
    #     Rule(next_page_link,follow=True),
    #     Rule(detail_link, callback='parse_item',follow=False),
    # )

    # def __init__(self, *args, **kwargs):
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(YySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 构造每个城市中的18岁以上的mm请求url
        base_url = 'http://www.youyuan.com/find{0}mm18-0/advance-0-0-0-0-0-0-0/p1/'
        a_list=response.xpath('//div[@class="yy_city_info"]/ul/li/font/a')
        for a in a_list:
            yield scrapy.Request(
                base_url.format(a.xpath('./@href').get()),
                callback=self.parse_all,
                priority=3
            )

    def parse_all(self, response):
        # 拿到列表页中所有mm的详情页url
        li_list = response.xpath('//ul[@class="mian search_list"]/li')
        for li in li_list:
            detail_url = response.urljoin(li.xpath('./dl/dt/a/@href').get())
            yield scrapy.Request(
                detail_url,
                callback=self.parse_item,
                priority=1
            )
        # 若有下一页，则继续发起请求
        temp = response.xpath('//a[@class="pe_right"]/@href').get()
        if temp != '###':
            next_page = response.urljoin(temp)
            yield scrapy.Request(
                next_page,
                callback=self.parse_all,
                priority=2
            )

    def parse_item(self, response):
        # 详情页里爬取mm的所有想要的信息
        flag=response.xpath('//p[@class="top_tit"]') # 判断是否已经进入了详情页，有一些页面会重定向到首页，从而会报错的
        if flag:
            item=YouyuanItem()
            item['name'] = response.xpath('//div[@class="main"]/strong/text()').get()  # 姓名
            temp=response.xpath('//p[@class="local"]/text()').get().split()
            item['address'] = temp[0]  # 地址
            item['age'] = temp[1]  # 年龄
            item['height'] = temp[2]  # 年龄
            item['salary'] = temp[3]  # 收入
            item['house'] = temp[4]  # 房子
            item['hobby'] = [i.strip() for i in response.xpath('//ol[@class="hoby"]/li//text()').getall()]  # 爱好
            item['image'] = response.xpath('//li[@class="smallPhoto"]/@data_url_full').getall()  # 照骗
            item['motto'] = response.xpath('//ul[@class="requre"]/li[1]/p/text()').get().strip()  # 内心独白
            item['detail'] = process_data(response.xpath('//div[@class="message"]')[0].xpath('./ol/li//text()').getall())  # 详细资料
            item['boy_condition'] = process_data(response.xpath('//div[@class="message"]')[1].xpath('./ol/li//text()').getall())  # 男友标准
            item['url'] = response.url  # 个人主页
            return item
