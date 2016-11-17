import scrapy

from scrapy.item import Item, Field

class awayTeamRushItem(Item):
    test = 'this is a test item'
    rusher = Field()
    car = Field()
    yds = Field()
    avg = Field()
    td = Field()
    longest = Field()



# class homeTeamRushItem(Item):
#     rusher = Field()
#     car = Field()
#     yds = Field()
#     avg = Field()
#     td = Field()
#     longest = Field()
