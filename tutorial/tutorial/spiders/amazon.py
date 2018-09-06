import scrapy
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        'https://www.amazon.in/dp/B01GGKYJG8?aaxitk=2G1aiBULRZuZmdsmjMskSg&pd_rd_i=B01GGKYJG8&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=98f2ac8f-072b-41ed-b07d-7646b42eb4b7&pf_rd_s=desktop-sx-top-slot&pf_rd_t=301&pf_rd_i=iphone&hsa_cr_id=5317368310402&sb-ci-n=productDescription&sb-ci-v=AmazonBasics%20USB%20Type-C%20to%20Micro-B%203.1%20Gen2%20Cable%20-%203%20Feet%20(0.9%20Meters)%20-%20White&sb-ci-a=B01GGKYJG8',
    ]
    link_extractor = LxmlLinkExtractor(allow=(), deny=(), allow_domains=('www.amazon.in'), deny_domains=(), deny_extensions=None, restrict_xpaths=(), restrict_css=(), tags=('a', 'area'), attrs=('href', ), canonicalize=False, unique=True, process_value=None, strip=True)

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
