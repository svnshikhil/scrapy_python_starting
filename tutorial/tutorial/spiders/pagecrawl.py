import scrapy


class PageSpider(scrapy.Spider):
    name = "page"
    default_meta = {'redirect_flg': False}

    def __init__(self, *args, **kwargs):
        self.crawl_request = kwargs.get('crawl_request')
        print("INSIDE",self.crawl_request.get('request_url'))
        self.start_urls = self.crawl_request.get('request_url')
        super(PageSpider, self).__init__()

    def start_requests(self):
        print('TEST',self.start_urls)

        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.parseError,
                                 meta=self.default_meta)


    def parse(self, response):
        page = response.url.split("/")[-2]
        yield {
            'title': response.xpath('//title/text()').extract_first().strip(),
            'description': response.xpath('//meta[@name="description"]/@content').extract_first(),
            'url': response.url,
            'download_time': response.meta['__end_time'] - response.meta['__start_time']
        }
        self.log('Saved file %s' % page)

    def parseError(self, response):
        print('Error')