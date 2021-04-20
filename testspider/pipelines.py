# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
from testspider import settings


class TestspiderPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True
        )

        # 通过cursor执行增删改查
        self.cursor = self.connect.cursor()

        # # 清除历史数据
        # if settings.MYSQL_CLRDATA == True:
        #     self.cursor.execute("""TRUNCATE TABLE %sS;""" % settings.MYSQL_TABLE)

    def process_item(self, item, spider):
        sql = "INSERT INTO {0}(name, xinzi, gongsi, weizhi, zige, fuli, zhize, url) " \
              "VALUE ('{1}' ,'{2}' ,'{3}' ,'{4}' ,'{5}' ,'{6}' ,'{7}' ,'{8}');".format(
            settings.MYSQL_TABLE,
            item['name'],
            item['xinzi'],
            item['gongsi'],
            item['weizhi'],
            item['zige'],
            item['fuli'],
            item['zhize'],
            item['url']
        )
        # print(sql)
        print(item['name'], item['gongsi'], item['weizhi'])
        self.cursor.execute(sql)
        self.connect.commit()  # 提交sql语句
        return item

    def close_spider(self, spider):
        self.connect.close()
        self.cursor.close()
