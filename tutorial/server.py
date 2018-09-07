import tornado.ioloop
import tornado.web
from handlers.StartCrawl import StartCrawl
from handlers.StopCrawl import StopCrawl
from handlers.InitCrawl import InitCrawl
from handlers.PauseCrawl import PauseCrawl
from handlers.ResumeCrawl import ResumeCrawl



application = tornado.web.Application([
    (r"/startCrawl", StartCrawl),
    (r"/stopCrawl", StopCrawl),
    (r"/initCrawl", InitCrawl),
    (r"/pauseCrawl", PauseCrawl),
    (r"/resumeCrawl", ResumeCrawl),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()