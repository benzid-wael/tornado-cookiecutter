import os
import sys
import json

import tornado.ioloop
import tornado.web

from config.settings import settings, BASE_DIR 

from apps.urls import urls


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, urls, **settings)


def make_app():
    app = Application()
    return app



if __name__ == '__main__':
    make_app()
