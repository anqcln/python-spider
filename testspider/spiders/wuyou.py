# import scrapy
#
#
# class WuyouSpider(scrapy.Spider):
#     name = 'wuyou'
#     allowed_domains = ['51job.com']
#     start_urls = ['http://www.51job.com/']
#
#     def parse(self, response):
#         print(response.url)
# -*- coding: utf-8 -*-
from urllib import response

import scrapy

# class WuyouSpider(scrapy.Spider):
#     name = 'wuyou'
#     allowed_domains = ['baidu.com']
#     start_urls = ['http://www.baidu.com/']
#
#     def parse(self, response):
#         print(response.meta)    # 打印 response 的参数
#         print(response.body)    # 打印 response 的二进制返回结果
#         print(response.body_as_unicode())   # 打印 response 的 utf-8 编码格式返回结果
#
#     # def parse(self, response):
#     #     print(type(response))
#     #     print(help(response))


# # -*- coding: utf-8 -*-
# import scrapy
#
# class WuyouSpider(scrapy.Spider):
#     name = 'wuyou'
#     allowed_domains = ['51job.com']
#     # start_urls = ['https://jobs.51job.com/shanghai-xhq/89396222.html?s=01&t=0']
#     start_urls = ['https://jobs.51job.com/suzhou/128521723.html?s=sou_sou_soulb&t=0']
#
#     def parse(self, response):
#
#         print(response.body_as_unicode())    # 打印 response 的 utf-8 编码格式返回结果


# # -*- coding: utf-8 -*-
# import scrapy
# from lxml import etree  # 解析 xml 文档的三方包，etree 解析器包含 xpath 的语法，xpath 主要解析 html 格式数据
#
# class WuyouSpider(scrapy.Spider):
#     name = 'wuyou'
#     allowed_domains = ['51job.com']
#     start_urls = ['https://jobs.51job.com/xian-caq/121046624.html?s=sou_sou_soulb&t=0']
#
#
#     @staticmethod
#     def datahandle(li):
#         if type(li) == list:
#             liresult = [i.strip() for i in li]
#             while '' in liresult:
#                 liresult.remove('')
#         return liresult
#
#
#
#     def parse(self, response):
#         # htmldata = etree.HTML(response.body_as_unicode())
#         htmldata = etree.HTML(response.text)
#         print('类型：',type(htmldata))
#         print(htmldata)
#         print(htmldata.xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/h1"))
#         print(htmldata.xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()"))
#
#         print('职位名称：',htmldata.xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()"))
#         print('薪资：',htmldata.xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()"))
#         print('公司名称：',htmldata.xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a/@title"))
#         company = htmldata.xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div//text()")
#         print('公司简介：', self.datahandle(company))


# # -*- coding: utf-8 -*-
# import sys
# import scrapy
# from lxml import etree # 解析 xml 文档的三方包，etree 解析器包含 xpath 的语法，xpath 主要解析 html 格式数据
# class WuyouSpider(scrapy.Spider):
#     name = 'wuyou'
#     allowed_domains = ['51job.com']
#     start_urls =['https://search.51job.com/list/200200,000000,0000,00,9,99,+,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']
#
#     def parse(self, response):
#         htmldata = etree.HTML(response.body_as_unicode())
#         netpage =htmldata.xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[7]/a/@href')
#         print(sys._getframe().f_code.co_name) # 打印当前函数名
#         print(response.url)
#         print(netpage)
#         yield scrapy.Request(netpage[0], callback=self.parse_nextpage)
#
#     def parse_nextpage(self, response):
#         print(sys._getframe().f_code.co_name)
#         print(response.url)


# -*- coding: utf-8 -*-
import sys
import scrapy
from testspider import items
from lxml import etree  # 解析 xml 文档的三方包，etree 解析器包含 xpath 的语法，xpath 主要解析 html 格式数据


def liststrip(listtmp):
    if type(listtmp) == list:
        listresult = [i.strip() for i in listtmp]
        while '' in listresult:
            listresult.remove('')
    return listresult


def cutdata(data):
    if type(data) == str:
        return data[:255]
    else:
        return "-"


class WuyouSpider(scrapy.Spider):
    name = 'wuyou'
    allowed_domains = ['liepin.com']
    start_urls = [
        'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=a5222af08149fcb246a6e4d336c94aac&d_ckId=a5222af08149fcb246a6e4d336c94aac&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=LGV-fc5u_67LtFjetF6ACg%7EfA9rXquZc5IkJpXC-Ycixw&key=%E5%A4%A7%E6%95%B0%E6%8D%AE']

    def parse(self, response):
        htmldata = etree.HTML(response.text)
        allurl = htmldata.xpath('//*[@class="job-info"]/h3/a/@href')  # 本页所有的职位详细信息链接
        for url in allurl:
            yield scrapy.Request(url, callback=self.qinqiu)

        netpage = htmldata.xpath('//*[@class="pagerbar"]/a[8]/@href')  # 下一页连接
        if netpage:
            yield scrapy.Request('https://www.liepin.com' + netpage[0], callback=self.parse)

    def qinqiu(self, response):

        data = items.TestspiderItem()

        htmldata = etree.HTML(response.text)
        # print(htmldata.xpath('//*[@class="title-info"]/h1/@title'))     # 职位名称
        # print(liststrip(htmldata.xpath('//*[@class="job-item-title"]/text()')))     # 薪资
        # print(liststrip(htmldata.xpath('//*[@class="title-info"]/h3/a/@title')))     # 公司
        # print(htmldata.xpath('//*[@class="basic-infor"]/span/a/text()'))        # 位置
        # print(htmldata.xpath('//*[@class="job-qualifications"]/span/text()'))        # 工作资格
        # print(htmldata.xpath('//*[@class="comp-tag-list clearfix"]/li/span/text()'))        # 福利待遇
        # print(cutdata('\t'.join(liststrip(htmldata.xpath('//*[@class="content content-word"]/text()')))))    # 职位描述

        data['name'] = htmldata.xpath('//*[@class="title-info"]/h1/@title')[0]  # 职位名称
        data['xinzi'] = liststrip(htmldata.xpath('//*[@class="job-item-title"]/text()'))[0]  # 薪资
        data['gongsi'] = htmldata.xpath('//*[@class="title-info"]/h3/a/@title')[0]      # 公司
        data['weizhi'] = htmldata.xpath('//*[@class="basic-infor"]/span/a/text()')[0]  # 位置
        data['zige'] = ','.join(htmldata.xpath('//*[@class="job-qualifications"]/span/text()'))  # 工作资格
        data['fuli'] = ','.join(htmldata.xpath('//*[@class="comp-tag-list clearfix"]/li/span/text()'))  # 福利待遇
        data['zhize'] = cutdata('\t'.join(liststrip(htmldata.xpath('//*[@class="content content-word"]/text()'))))  # 职位描述
        data['url'] = response.url

        yield data