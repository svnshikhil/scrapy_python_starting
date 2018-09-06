import tornado.ioloop
import tornado.web
from handlers.StartCrawl import StartCrawl
from handlers.StopCrawl import StopCrawl
from handlers.InitCrawl import InitCrawl



application = tornado.web.Application([
    (r"/startCrawl", StartCrawl),
    (r"/stopCrawl", StopCrawl),
    (r"/initCrawl", InitCrawl),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()