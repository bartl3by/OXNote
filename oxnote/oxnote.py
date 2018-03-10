#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from models.accounts import AccountManager
from multiprocessing import freeze_support
from user_interface.application import Application
from util.configuration import Configuration
from util.environment import Environment

logger = logging.getLogger(__name__)

application = None


def main():
    logger.debug('Initiated logging environment')

    Environment.initiate_logging_environment(Configuration().get_setting('oxnote',
                                                                         'extended_logging.requests_debug_level',
                                                                         default=0))

    logger.debug('Starting OXNote')

    global application
    application = Application()

    if not AccountManager().list_accounts():
        application.start_wizard()
    else:
        application.start_main_window()


if __name__ == "__main__":
    freeze_support()
    main()
