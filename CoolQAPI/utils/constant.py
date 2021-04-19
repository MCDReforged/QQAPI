# -*- coding: utf-8 -*-
import os

VERSION = '0.1.0'
NAME = 'CoolQAPI'
RELEASE_URL = 'https://api.github.com/repos/zhang-anzhi/CoolQAPI/releases/latest'


class FilePath:
    CONFIG_DIR = os.path.join('config', NAME)
    CONFIG_NAME = os.path.join(CONFIG_DIR, 'config.yml')
