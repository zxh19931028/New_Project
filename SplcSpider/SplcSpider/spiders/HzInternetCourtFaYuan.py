# -*- coding: utf-8 -*-
import datetime
import os

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HzInternetCourtFaYuan(CrawlSpider):
    name = 'HzInternetCourtFaYuan'
    allowed_domains = ['https://www.netcourt.gov.cn/suit/caseSearchRpc/queryCaseInfo.json']
    start_urls = ['http://https://www.netcourt.gov.cn/suit/caseSearchRpc/queryCaseInfo.json/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    custom_settings = {
        'LOG_LEVEL': ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"][3],
        'LOG_FILE': os.path.join(os.path.dirname(__file__), "../logs/%s_%s.log" % (name, str(datetime.date.today()))),
        'ITEM_PIPELINES': {
            'New_Project.SplcSpider.SplcSpider.piplines.HzInternetCourtFaYuanPipline': 300,
        }
    }
    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(
                url=start_url,
                meta={
                    "key": "",
                    "type": "suit",
                    "courtId": "",
                    "phase": "",
                    "status": "dropped",
                    "procedureType": "statusSuitList",
                    "page": {"begin": 50, "length": 10},
                },
                headers=self.headers,
                callback=self.parse_item
            )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
