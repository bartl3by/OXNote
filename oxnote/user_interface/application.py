#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import os
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QStyleFactory

from user_interface.main_window import MainWindow
from user_interface.setup_wizard import SetupWizard
from util.environment import Environment

logger = logging.getLogger(__name__)


class Application(object):

    def __init__(self):
        Environment.bootstrap_application_directories()

        self._app = QApplication(sys.argv)
        self._app.setStyle(QStyleFactory.create("Fusion"))
        self._app.setWindowIcon(QtGui.QIcon(os.path.join(Environment.get_resource_path(),
                                                         'designs/default/OXNote.icns')))
        self._app.setApplicationDisplayName('OXNote')
        self._app.setApplicationName('OXNote')

    def start_wizard(self):
        logger.debug('Preparing to start account setup wizard')

        self._oxnote_setup_wizard_widget = SetupWizard()
        self._oxnote_setup_wizard_widget.show()
        self.exit()

    def start_main_window(self):
        logger.debug('Preparing to start main window')

        self._oxnote_main_window_widget = MainWindow()
        self._oxnote_main_window_widget.show()
        self.exit()


    def exit(self):
        sys.exit(self._app.exec_())
