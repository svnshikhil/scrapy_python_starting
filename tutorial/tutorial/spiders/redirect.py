import scrapy


class RedirectSpider(scrapy.Spider):
    name = "redirect"
    start_urls = [
        'http://www.bestbuy.ca/en-CA/category/smart-home/33195.aspx',
    ]

    def parse(self, response):
        print('RESP',response)
        print('REASON',response.meta['reason'])
        yield {
            'url':self.start_urls,
            'redirect':response.meta['reason']
        }
        print('Completed')

    def spider_error(self, failure):
        print('ERR')
        response = failure.value.respons