# -*- coding: utf-8 -*-
import scrapy


class EspnspiderSpider(scrapy.Spider):
    name = "espnSpider"
    allowed_domains = ["espn.com"]
    start_urls = (
        'http://www.espn.com/nfl/boxscore?gameId=400874586',
    )

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
