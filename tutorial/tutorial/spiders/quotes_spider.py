import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        start_urls =[]


    def parse(self, response):
        page = response.url.split("/")[-2]
        print('PAGES',response.body)

        self.log('Completed',page)