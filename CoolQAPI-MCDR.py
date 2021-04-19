# -*- coding: utf-8 -*-
from mcdreforged.api.command import *
from CoolQAPI.utils.constant import VERSION
from CoolQAPI.utils.update import check
from CoolQAPI import CoolQAPI as cool_q_api

PLUGIN_METADATA = {
    'id': 'cool_q_api',
    'version': VERSION,
    'name': 'CoolQAPI',
    'description': 'Connect Minecraft and QQ',
    'author': 'zhang_anzhi',
    'link': 'https://github.com/zhang-anzhi/CoolQAPI'
}
HELP_MESSAGE = '§6!!cq update §7检查并自动更新'


def on_load(server, old):
    check(server)
    start(server)

    server.register_help_message('!!cq', 'CoolQAPI插件帮助')
    server.register_command(
        Literal('!!cq').
            runs(lambda src: src.reply(HELP_MESSAGE)).
            then(
            Literal('update').runs(lambda src: check(src.get_server(), src))
        )
    )


def on_unload(server):
    stop()


def on_mcdr_stop(server):
    stop()


def start(server):
    cool_q_api.start(server)


def stop():
    cool_q_api.stop()


def get_bot():
    """return bot object"""
    return cool_q_api.get_bot()


def get_config():
    """get the api config"""
    return cool_q_api.get_config()
