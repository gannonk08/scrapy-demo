# -*- coding: utf-8 -*-
import scrapy


class EspnspiderSpider(scrapy.Spider):
    name = "espnSpider"
    allowed_domains = ["espn.com"]
    start_urls = (
        'http://www.espn.com/',
    )

    def parse(self, response):
        pass
