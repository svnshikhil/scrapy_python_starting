import tornado.web
import crawl_handler

import json


class StartCrawl(tornado.web.RequestHandler):
    crawlerHandler = crawl_handler
    def post(self):
        request_string = self.request.body.decode('utf-8')
        response = None
        if self.crawlerHandler.crawler is None:
            self.crawlerHandler.startCrawl(request_string)
            response = {
                'message': 'Successfully started crawl'
            }
        else:
            response = {
                'message': 'Busy'
            }
        self.write(response)