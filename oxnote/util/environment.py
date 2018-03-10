#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import os
import sys
from http.client import HTTPConnection

import pathlib
import ruamel.yaml as yaml

logger = logging.getLogger(__name__)


class Environment(object):
    __base_path = None
    __bundle_path = None

    @staticmethod
    def is_bundled() -> bool:
        return getattr(sys, 'frozen', False) or hasattr(sys, '_MEIPASS') or hasattr(os.environ, '_MEIPASS2')

    @staticmethod
    def get_bundle_path() -> str:
        if not Environment.__bundle_path:
            logger.debug('Determining bundle_path based on environment attributes')

            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                Environment.__bundle_path = os.path.abspath(os.path.join(sys._MEIPASS, '../'))
            elif getattr(sys, 'frozen', False) and hasattr(os.environ, '_MEIPASS2'):
                Environment.__bundle_path = os.path.abspath(os.path.join(os.environ._MEIPASS2, '../'))
            else:
                Environment.__bundle_path = os.getcwd()

        return Environment.__bundle_path

    @staticmethod
    def get_base_path() -> str:
        '''
        ::todo: See if it is required to check if the bundle is in a security lock
        '''
        if not Environment.__base_path:
            logger.debug('Determining base_path based on environment attributes')

            if Environment.is_bundled():
                Environment.__base_path = pathlib.Path.home()
            else:
                Environment.__base_path = os.getcwd()

        return Environment.__base_path


    @staticmethod
    def get_configuration_path() -> str:
        if Environment.is_bundled():
            return os.path.join(Environment.get_bundle_path(), 'Resources/configuration')
        else:
            return os.path.join(Environment.get_base_path(), 'configuration')

    @staticmethod
    def get_resource_path() -> str:
        if Environment.is_bundled():
            return os.path.join(Environment.get_bundle_path(), 'Resources')
        else:
            return os.path.join(Environment.get_base_path(), 'resources')

    @staticmethod
    def bootstrap_application_directories():
        from util.configuration import Configuration

        directories = [
            Configuration().get_setting('oxnote', 'application.directories.workspace', default='.oxnote'),
            Configuration().get_setting('oxnote', 'application.directories.accounts', default='.oxnote/accounts'),
            Configuration().get_setting('oxnote', 'application.directories.temporary', default='.oxnote/tmp')
        ]

        for directory in directories:
            if not os.path.isdir(os.path.join(Environment.get_base_path(), directory)):
                logger.debug('Bootstrapping application directory: {}'.format(os.path.join(Environment.get_base_path(),
                                                                                           directory)))

                os.makedirs(os.path.join(Environment.get_base_path(), directory))

    @staticmethod
    def bootstrap_account_directories(account):
        from util.configuration import Configuration

        accounts_directory = os.path.join(Environment.get_base_path(),
                                          Configuration().get_setting('oxnote',
                                                                      'application.directories.accounts',
                                                                      default='.oxnote/accounts'))

        directories = [
            os.path.join(accounts_directory, account.account_root_directory),
            os.path.join(accounts_directory, account.account_root_directory, account.oxnote_home_folder),
            os.path.join(accounts_directory, account.account_root_directory, account.application_data_folder)
        ]

        for directory in directories:
            if not os.path.isdir(os.path.join(Environment.get_base_path(), directory)):
                logger.debug('Bootstrapping account directory: {}'.format(os.path.join(Environment.get_base_path(),
                                                                                       directory)))

                os.makedirs(os.path.join(Environment.get_base_path(), directory))

    @staticmethod
    def initiate_logging_environment(httpconnection_debug_level: int):
        HTTPConnection.debuglevel = httpconnection_debug_level

        with open(os.path.join(Environment.get_configuration_path(), 'logging.yaml'), 'r') as f:
            logging_configuration = yaml.safe_load(f)
            for handler in logging_configuration["handlers"].keys():
                if 'filename' in logging_configuration["handlers"][handler]:
                    logging_configuration["handlers"][handler]['filename'] = os.path.join(Environment.get_base_path(),
                                                                                          logging_configuration["handlers"][handler]['filename'])
                    if not os.path.exists(os.path.dirname(logging_configuration["handlers"][handler]['filename'])):
                        os.makedirs(os.path.dirname(logging_configuration["handlers"][handler]['filename']))

            logging.config.dictConfig(logging_configuration)
