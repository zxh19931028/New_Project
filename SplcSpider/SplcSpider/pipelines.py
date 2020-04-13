# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from MySQL import MySQL

mysql_20 = MySQL("172.16.0.20")


class SplcspiderPipeline(object):
    def process_item(self, item, spider):
        return item



class HzInternetCourtFaYuanPipline(object):

    @staticmethod
    def process_item(item, spider):
        sql = "insert ignore into ktgg.hefei_yaohai(ah,ay,dsr,place,data_time,sj,add_time,) " \
              "values(%s,%s,%s,%s,%s,%s,%s,now()) "
        mysql_20.execute_update(sql, (
            item['title'],
            item['courtName'],
            item['caseCode'],
            item['trialName'],
            item['prosecutionStr'],
            item['defendantStr'],
            item['causeAction'],
            item['status'],

        ))
        return item