import scrapy
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class LinkSpider(scrapy.Spider):
    name = "link"
    allow_domains=None
    deny_domains=None

    link_extractor = LxmlLinkExtractor(allow=(), deny=(), allow_domains=(allow_domains), deny_domains=(deny_domains), deny_extensions=None, restrict_xpaths=(), restrict_css=(), tags=('a', 'area'), attrs=('href', ), canonicalize=False, unique=True, process_value=None, strip=True)

    def __init__(self, *args, **kwargs):
        self.crawl_request = kwargs.get('crawl_request')
        print("INSIDE", self.crawl_request.get('request_url'))
        self.start_urls = self.crawl_request.get('request_url')
        self.allow_domains = self.crawl_request.get('allow_domains')
        self.deny_domains = self.crawl_request.get('deny_domains')
        super(LinkSpider, self).__init__()


    def parse(self, response):

        links = self.link_extractor.extract_links(response)
        for link in links:
            print(link.url)
            yield scrapy.Request(url=link.url,callback=self.parse)

        print('RESPONSE')

        yield {
            'title':response.xpath('//title/text()').extract_first().strip(),
            'description':response.xpath('//meta[@name="description"]/@content').extract_first(),
            'url':response.url,
            'download_time':response.meta['__end_time']-response.meta['__start_time']
        }
        print('Completed')

    def parseError(self, response):
        print('Error')