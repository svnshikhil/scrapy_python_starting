import tornado.web
import crawl_handler

import json


class InitCrawl(tornado.web.RequestHandler):
    crawlerHandler = crawl_handler
    def post(self):
        request_string = self.request.body.decode('utf-8')
        request_json = json.loads(request_string)
        response = None
        if self.crawlerHandler.crawler is None:
            self.crawlerHandler.initCrawl(request_json)
            response = {
                'message': 'Successfully started crawl'
            }
        else:
            response = {
                'message': 'Busy'
            }
        self.write(response)