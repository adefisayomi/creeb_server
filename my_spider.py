import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://example.com']

    def parse(self, response):
        # Your scraping logic here
        data = {
            'title': response.css('h1::text').get(),
            'content': response.css('p::text').getall(),
        }
        yield data
