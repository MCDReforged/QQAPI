# -*- coding: utf-8 -*-
import requests

from plugins.CoolQAPI.utils.constant import FilePath
from plugins.CoolQAPI.utils.post_server import PostServer
from plugins.CoolQAPI.utils.config import Config

config = Config(FilePath.CONFIG_NAME)
post_server = PostServer(config)
is_work = False


def start(server):
    global is_work, config
    config = Config(FilePath.CONFIG_NAME)
    post_server.init(server, config)
    post_server.start()
    is_work = True


def stop():
    global is_work, config
    requests.post(
        f'http://{config["post_host"]}:{ config["post_port"]}/'
        f'{config["post_path"]}',
        json={'shutdown': True}
    )
    is_work = False


def get_bot():
    """get bot object"""
    return post_server.get_bot()


def get_config():
    """get config"""
    global config
    return config
