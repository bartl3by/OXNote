#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging.config
import os
import typing

import ruamel.yaml as yaml

logger = logging.getLogger(__name__)


class Configuration(object):
    __cache = {}

    def __init__(self):
        from util.environment import Environment

        self._configuration_directory = Environment.get_configuration_path()

    def __format_configuration_dict(self, data, separator: str = '.', path: str = '') -> typing.Dict[str, str]:
        return {path + separator + k if path else k: v for kk, vv in data.items() for k, v in
                self.__format_configuration_dict(vv, separator, kk).items()} if isinstance(data, dict) else {
            path: data
        }

    def get_setting(self, namespace: str, key: str, separator: str = '.', default=None):
        if not namespace in self.__cache:
            with open(os.path.join(self._configuration_directory, '{}.yaml'.format(namespace)), 'r') as f:
                logger.debug('Loading configuration file into cache: {}'.format(f.name))

                self.__cache[namespace] = self.__format_configuration_dict(yaml.safe_load(f), separator)

        return self.__cache[namespace][key] if key in self.__cache[namespace] else default

    def set_value(self, namespace: str, key: str, value: str):
        raise NotImplementedError
