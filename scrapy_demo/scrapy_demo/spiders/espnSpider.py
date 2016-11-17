import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field


from items import awayTeamRushItem
import logging
import re

class EspnspiderSpider(scrapy.Spider):
    name = "espnSpider"
    allowed_domains = ["espn.com"]
    start_urls = (
        'http://www.espn.com/nfl/boxscore?gameId=400874586',
    )

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=False),
    )

    global awayItem
    awayItem = awayTeamRushItem()

    def parse(self, response):
        rushers = response.xpath('//*[@id="gamepackage-rushing"]/div/div[1]/div/div/table/tbody/*/td[1]/a/span[1]/text()').extract()

        carries = response.xpath('//*[@id="gamepackage-rushing"]/div/div[1]/div/div/table/tbody/*/td[2]/text()').extract()

        yards = response.xpath('//*[@id="gamepackage-rushing"]/div/div[1]/div/div/table/tbody/*/td[3]/text()').extract()

        averages = response.xpath('//*[@id="gamepackage-rushing"]/div/div[1]/div/div/table/tbody/*/td[4]/text()').extract()

        touchdowns = response.xpath('//*[@id="gamepackage-rushing"]/div/div[1]/div/div/table/tbody/*/td[5]/text()').extract()

        longs = response.xpath('//*[@id="gamepackage-rushing"]/div/div[1]/div/div/table/tbody/*/td[6]/text()').extract()

        awayItemIndex = 0

        for rusher in rushers:
            awayItem = awayTeamRushItem()

            awayItem['car'] = carries[awayItemIndex]
            awayItem['yds'] = yards[awayItemIndex]
            awayItem['avg'] = averages[awayItemIndex]
            awayItem['td'] = touchdowns[awayItemIndex]
            awayItem['longest'] = longs[awayItemIndex]
            awayItem['rusher'] = rusher

            awayItemIndex+=1

            yield awayItem
