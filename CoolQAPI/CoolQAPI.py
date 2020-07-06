# -*- coding: utf-8 -*-

import requests

from plugins.CoolQAPI.utils.post_server import PostServer
from plugins.CoolQAPI.utils.config import Config

config = {}
post_server = PostServer(config)
is_work = False


def start(server):
    global is_work, config
    config = Config('.\\plugins\\CoolQAPI\\config.yml')
    post_server.init(server, config)
    post_server.start()
    is_work = True


def load_event():
    """load plugins"""
    post_server.load_event()


def stop():
    global is_work, config
    requests.post('http://{}:{}{}'.format(
        config['post_host'], config['post_port'], config['post_url']),
        json={'shutdown': True})
    is_work = False


def get_bot():
    """get bot object"""
    return post_server.get_bot()
