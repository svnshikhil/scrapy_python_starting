import tornado.web
import crawl_handler


class ResumeCrawl(tornado.web.RequestHandler):
    crawlerHandler = crawl_handler
    def post(self):
        request_string = self.request.body.decode('utf-8')
        response = None
        self.crawlerHandler.resumeCrawl(request_string)
        response = {
            'message': 'Successfully resume crawl'
        }
        # if self.crawlerHandler.crawler is not None:
        #     response = {
        #         'message': 'Successfully stoped crawl'
        #     }
        # else:
        #     response = {
        #         'message': 'No crawl to stop'
        #     }
        self.write(response)