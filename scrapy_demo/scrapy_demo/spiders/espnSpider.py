import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field


from items import awayTeamRushItem
import logging
import re

# class awayTeamRushItem(Item):
#     test = 'this is a test item'
#     rusher = Field()
#     car = Field()
#     yds = Field()
#     avg = Field()
#     td = Field()
#     longest = Field()

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
        print awayItem

        rushers = response.xpath('//*[@id="gamepackage-rushing"]/div/div[1]/div/div/table/tbody/*/td[1]/a/span[1]/text()').extract()





        for rusher in rushers:
            print rusher
            awayItem['rusher'] = rusher

        yield awayItem
