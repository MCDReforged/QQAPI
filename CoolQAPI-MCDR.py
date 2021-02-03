# -*- coding: utf-8 -*-
import time

from mcdreforged.api.command import *
from CoolQAPI.utils.constant import VERSION
from CoolQAPI.utils.functions import load_source
from CoolQAPI.utils.update import check

cool_q_api = load_source('plugins/CoolQAPI/CoolQAPI.py')

PLUGIN_METADATA = {
    'id': 'cool_q_api',
    'version': VERSION,
    'name': 'CoolQAPI',
    'description': 'Connect Minecraft and QQ',
    'author': 'zhang_anzhi',
    'link': 'https://github.com/zhang-anzhi/CoolQAPI'
}
HELP_MESSAGE = '''§6!!cq reload all §7重载所有
§6!!cq reload plugin §7重载插件
§6!!cq update §7检查并自动更新'''


def on_load(server, old):
    global cool_q_api
    if old is not None and hasattr(old, 'cool_q_api'):
        cool_q_api = old.cool_q_api
    else:
        check(server)
        start(server)

    def reload_all(src):
        stop()
        time.sleep(1)
        start(server)
        time.sleep(0.1)
        src.reply('§a已成功重载所有')

    def reload_plugin(src):
        reload_plugins()
        src.reply('§a已成功重载插件')

    server.register_command(
        Literal('!!cq').
            runs(lambda src: src.reply(HELP_MESSAGE)).
            then(
            Literal('reload').
                then(
                Literal('all').runs(reload_all)
            ).
                then(
                Literal('plugin').runs(reload_plugin)
            )
        ).
            then(
            Literal('update').runs(lambda src: check(src.get_server(), src))
        )
    )


def on_mcdr_stop(server):
    stop()


def start(server):
    global cool_q_api
    cool_q_api = load_source('plugins/CoolQAPI/CoolQAPI.py')
    cool_q_api.start(server)


def stop():
    global cool_q_api
    cool_q_api.stop()


def reload_plugins():
    """reload plugins api"""
    global cool_q_api
    cool_q_api.load_event()


def get_bot():
    """return bot object"""
    global cool_q_api
    return cool_q_api.get_bot()


def get_config():
    """get the api config"""
    global cool_q_api
    return cool_q_api.get_config()
