#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from functools import partial

from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from requests.exceptions import ConnectionError, RequestException
from urllib3.exceptions import LocationValueError

from appsuite_api_wrapper.drive_client import DriveClient
from appsuite_api_wrapper.exceptions import (PermissionException, SessionException)
from appsuite_api_wrapper.models.drive_extended_action import DriveExtendedAction
from appsuite_api_wrapper.session import HttpApiSession
from models.accounts import AccountManager
from util.configuration import Configuration

logger = logging.getLogger(__name__)


class SynchronizeNotesThreadWorker(QObject):
    signal_restart_timer = pyqtSignal()
    signal_synchronization_status_update = pyqtSignal(str)
    signal_synchronization_note_updated = pyqtSignal(str, str, str, int, DriveExtendedAction)
    signal_synchronization_finished = pyqtSignal()

    @pyqtSlot()
    def run(self):
        logger.debug('Starting synchronization threads {}'.format(int(QThread.currentThreadId())))

        drive_client = None
        session_id = None

        account_manager = AccountManager()

        for account_id in account_manager.list_accounts():
            account = account_manager.get_account(account_id)

            try:
                drive_client = DriveClient(
                        username=account.username,
                        password=account.password,
                        url='{}://{}:{}{}'.format(account.url_scheme,
                                                  account.url_host,
                                                  str(account.url_port),
                                                  account.url_uri),
                        local_synchronization_directory=account.get_account_root_directory_path(),
                        synchronization_statefile=account.get_synchronization_statefile(),
                        compatible_api_version=Configuration().get_setting('drive_client', 'api.compatibility.api_version'),
                        api_client_identifier=Configuration().get_setting('drive_client',
                                                                        'api.defaults.compatibility.client_identifier',
                                                                        default='OXNote'),
                        notification_callback=partial(self.signal_synchronization_note_updated.emit, account_id))

                self.signal_synchronization_status_update.emit('Synchronizing notes for account {}'.format(account.username))
                drive_client.synchronize_files(account.application_data_folder)

                self.signal_synchronization_status_update.emit('Synchronizing previews for account {}'.format(account.username))
                drive_client.synchronize_files(account.oxnote_home_folder)

                drive_client.close()
            except ConnectionError as e:
                logger.warning(e)
            except (SessionException, RequestException, LocationValueError, PermissionException) as e:
                logger.error(e)
            except Exception as e:
                logger.error(e, exc_info=True)
            finally:
                if drive_client:
                    del drive_client

            if session_id:
                try:
                    HttpApiSession().logout(session_id)
                except:
                    logger.error('Unable to terminate session {}'.format(session_id))

        self.signal_restart_timer.emit()
        self.signal_synchronization_finished.emit()
