
import scrapy
from webcrawler.items import AngularItem


class AngularSpider(scrapy.Spider):
    name = "angular"
    start_urls = [
        'https://themeforest.net/tags/angular',
    ]

    def parse(self, response):
        for data in response.css("div._2sT86"):
        	item_data = AngularItem()
        	item_data['title'] = data.css("a._2Pk9X::text").get()
        	item_data['author'] = data.css("a.R8zaM::text")[1].get()
        	item_data['price'] = data.css("div.-DeRq::text")[1].get()
        	item_data['star'] = data.xpath('//div[@class="_3yoIm"]/@aria-label').get()
        	item_data['tags'] = data.css('div.HogM0 span._3Q47d::text')[1].getall()
        	yield item_data
            # yield {
            #     'title': data.css("a._2Pk9X::text").get(),
            #    	'author': data.css("a.R8zaM::text").getall()[1],
            #    	'price' : data.css("div.-DeRq::text")[1].get(),
            #     'star': data.xpath('//div[@class="_3yoIm"]/@aria-label').get(),
            #     'tags': data.css('div.HogM0 span._3Q47d::text').getall()[1],
            #     }
        next_page = response.css('li.pIPk0 a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        # return item_data


