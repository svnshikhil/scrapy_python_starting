import scrapy
import logging
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S")


class LinkSpider(scrapy.Spider):
    name = "link"
    allow_domains = None
    deny_domains = None

    link_extractor = LxmlLinkExtractor(allow=(), deny=(), allow_domains=(["grainger.com"]), deny_domains=(deny_domains),
                                       deny_extensions=None, restrict_xpaths=(), restrict_css=(), tags=('a', 'area'),
                                       attrs=('href',), canonicalize=False, unique=True, process_value=None, strip=True)

    def __init__(self, *args, **kwargs):
        self.crawl_request = kwargs.get('crawl_request')
        print("INSIDE", self.crawl_request.get('request_url'))
        self.start_urls = self.crawl_request.get('request_url')
        # self.allow_domains = self.crawl_request.get('allow_domains')
        self.deny_domains = self.crawl_request.get('deny_domains')
        super(LinkSpider, self).__init__()

    def parse(self, response):
        print('RESPONSE | URL : %s | STATUS : %s | META : %s ' % (
        str(response.url), str(response.status), str(response.meta['download_latency'])))
        links = self.link_extractor.extract_links(response)
        # if self.crawl_request.get('dont_crawl_links_found',True):
            # for link in links:
            #     # print(link.url)
            #     yield scrapy.Request(url=link.url, callback=self.parse)

        yield {
            'url': response.url,
            'download_time': response.meta['__end_time'] - response.meta['__start_time'],
            'download_latency': response.meta['download_latency']
        }

    def parseError(self, response):
        print('Error')
