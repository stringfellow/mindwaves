#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime

import tornado.ioloop
import tornado.web
import tornado.websocket

from pymindwave.headset import Headset

hs = None
clients = []


def brainwaves(fp):
    tornado.ioloop.IOLoop.instance().add_timeout(
        datetime.timedelta(seconds=1),
        brainwaves, fp
    )
    if hs is not None:
        data = [
            hs.get_alpha_waves(),
            hs.get_beta_waves(),
            hs.get_delta_waves(),
            hs.get_theta_waves(),
            hs.get_gamma_waves(),
            hs.get_current_meditation(),
            hs.get_current_attention(),
        ]
        data = map(str, data)
        line = '{0},{1}\n'.format(
            datetime.datetime.now().isoformat(),
            ','.join(data)
        )
        fp.write(line)
        fp.flush()
        for cl in clients:
            cl.write_message(",".join(data))


class Hello(tornado.websocket.WebSocketHandler):

    def open(self):
        clients.append(self)

    def on_message(self, message):
        pass

    def on_close(self):
        clients.remove(self)


class Main(tornado.web.RequestHandler):
    def get(self):
        self.render("brain.html")


if __name__ == "__main__":
    handlers = [
        (r"/", Main),
        (r"/websocket", Hello),
    ]
    application = tornado.web.Application(
        handlers,
        static_path=os.path.abspath('.'),
    )

    try:
        fp = open('out.csv', 'w')
        hs = Headset('/dev/tty.MindWave')
        print application.settings
        application.listen(8888)
        brainwaves(fp)
        tornado.ioloop.IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit):
        fp.close()
