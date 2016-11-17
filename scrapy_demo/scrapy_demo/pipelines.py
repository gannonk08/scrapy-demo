# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
import logging
from spiders.items import awayTeamRushItem
from scrapy.conf import settings
from scrapy.exceptions import DropItem


class ScrapyDemoPipeline(object):
  def __init__(self):
    self.connection = psycopg2.connect(host='localhost', database='scraping_demo', user='Gannon')
    self.cursor = self.connection.cursor()

  def process_item(self, item, spider):
    try:
      if type(item) is awayTeamRushItem:
        table = """awayteamrush"""
        self.cursor.execute("""INSERT INTO """ + table + """  (rusher, car, yds, avg, td, longest) VALUES(%s, %s, %s, %s, %s, %s)""", (item.get('rusher'), item.get('car'), item.get('yds'), item.get('avg'), item.get('td'), item.get('longest')))

      self.connection.commit()
      self.cursor.fetchall()

    except psycopg2.DatabaseError, e:
      print "Error: %s" % e
    return item
