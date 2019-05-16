
import scrapy


class GitdocSpider(scrapy.Spider):
    name = "gitdoc"
    start_urls = [
        'https://docs.scrapy.org/en/latest/intro/tutorial.html',
    ]

    def parse(self, response):
        for data in response.css("div.highlight"):
            yield {
                'title': data.css('title::text').get(),
                # 'author': data.css('small.author::text').get(),
                # 'tags': data.css('div.tags a.tag::text').getall(),
                'code' : data.css("span::text").getall()
                }


