# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WebcrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


from scrapy.exceptions import DropItem

class PricePipeline(object):

    def process_item(self, item, spider):
        if item.get('price'):
        	item['price'] = '$' + item['price']
        	return item
        else:
            raise DropItem("Missing price in %s" % item)

    # def process_item(self, item, spider):
    #     if item.get('tags'):
    #     	item['tags'] = item['tags'].split(',')
    #     	return item
    #     else:
    #         raise DropItem("Missing tags in %s" % item)
