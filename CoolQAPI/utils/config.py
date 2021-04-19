# -*- coding: utf-8 -*-
import os
import yaml

from .constant import FilePath


class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.default = {
            'post_host': '127.0.0.1',
            'post_port': 5701,
            'post_path': 'post',
            'api_host': '127.0.0.1',
            'api_port': 5700,
            'command_prefix': '/',
        }
        if not os.path.isdir(FilePath.CONFIG_DIR):
            os.mkdir(FilePath.CONFIG_DIR)
        self._check()

    def _check(self):
        self._load()
        save_flag = False
        for key, value in self.default.items():
            if key not in self.data.keys():
                self.data[key] = value
                save_flag = True
        if save_flag:
            self._save()

    def _load(self):
        if os.path.isfile(self.file_path):
            with open(self.file_path, encoding='utf-8') as f:
                self.data = yaml.safe_load(f)
        else:
            self.data = self.default
            self._save()

    def _save(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.data, f)

    def __getitem__(self, item):
        return self.data[item]
