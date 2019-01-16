# -*- coding: utf-8 -*-
import pymysql
import logging

from flea.db.connect import MYSQL_HOST, MYSQL_PORT, MYSQL_DBNAME, MYSQL_USER, MYSQL_PASSWD, MYSQL_CHARSET, MYSQL_UNICODE

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class FleaPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host=MYSQL_HOST,
                                    port=MYSQL_PORT,
                                    user=MYSQL_USER,
                                    passwd=MYSQL_PASSWD,
                                    db=MYSQL_DBNAME,
                                    charset=MYSQL_CHARSET,
                                    use_unicode=MYSQL_UNICODE)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            username = item['username']
            phone = item['phone']
            createDate = item['createDate']
            website = item['website']
            city = item['city']
            sql = "insert into house(username, phone, createDate, website, city)" \
                  " VALUES(%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (username, phone, createDate, website, city))
            self.conn.commit()
        except Exception as error:
            logging.log(error)
        return item

    def close_spider(self, spider):
        self.conn.close()
