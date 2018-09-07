import os
import threading

import tornado.ioloop
import tornado.web
from tutorial.spiders.redirect import RedirectSpider
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
import json
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from tutorial import settings as my_settings

crawler = None
runner = None

def startCrawl(crawl_request):
    crawler_settings = get_project_settings()
    crawler_settings.setmodule(my_settings)
    global runner
    runner = CrawlerRunner(settings=crawler_settings)
    global crawler
    d = runner.crawl('amazon')

    d.addBoth(lambda _: reactor.stop())
    # threading._start_new_thread(reactor.run,((),))
    if list(runner.crawlers):
        crawler = list(runner.crawlers)[0]
    threading._start_new_thread(reactor.run,((),))
    # reactor.run()




def stopCrawl(crawl_request):
    global crawler
    global runner
    print('HEY',crawler.engine)
    # os._exit(1)
    try:
        crawler.engine.stop()
        runner.stop()

    except Exception as e:
        print('Error',e)

def pauseCrawl(crawl_request):
    global crawler
    global runner
    print('HEY',crawler.engine)
    # os._exit(1)
    try:
        crawler.engine.pause()
        runner.pause()

    except Exception as e:
        print('Error',e)

def resumeCrawl(crawl_request):
    global crawler
    global runner
    print('HEY',crawler.engine)
    # os._exit(1)
    try:
        crawler.engine.unpause()
        runner.unpause()

    except Exception as e:
        print('Error',e)

def initCrawl(crawl_request):
    crawler_settings = get_project_settings()
    crawler_settings.setmodule(my_settings)
    print(crawl_request)
    global runner
    runner = CrawlerRunner(settings=crawler_settings)
    global crawler
    d = runner.crawl(start_urls=crawl_request.get('request_url')[0], crawler_or_spidercls=crawl_request.get('spider'),crawl_request=crawl_request)

    d.addBoth(lambda _: reactor.stop())
    # threading._start_new_thread(reactor.run,((),))
    if list(runner.crawlers):
        crawler = list(runner.crawlers)[0]
    threading._start_new_thread(reactor.run,((),))
    d.addBoth(lambda _: reactor.stop())
    # reactor.run()
