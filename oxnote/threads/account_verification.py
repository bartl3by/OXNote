#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

import requests
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from requests.exceptions import ConnectionError, InvalidURL, RequestException
from urllib3.exceptions import LocationValueError
from urllib3.util import parse_url

from appsuite_api_wrapper.exceptions import PermissionException, SessionLoginException, DriveException
from appsuite_api_wrapper.modules.capabilities import Capabilities
from appsuite_api_wrapper.session import HttpApiSession

logger = logging.getLogger(__name__)


class AccountVerificationThreadWorker(QObject):
    finished = pyqtSignal(bool, str)

    def __init__(self, username: str, password: str, server_address: str):
        QObject.__init__(self)

        self._username = username
        self._password = password
        self._server_address = server_address

    @pyqtSlot()
    def run(self):
        account_valid = False
        message = None

        try:
            if not self._username or len(self._username.strip()) <= 0:
                raise ValueError('Empty username')
            if not self._password or len(self._password.strip()) <= 0:
                raise ValueError('Empty password')
            if not self._server_address or len(self._server_address.strip()) <= 0:
                raise ValueError('Empty server address')

            url = parse_url(self._server_address)

            http_api_session = HttpApiSession()
            session_id = http_api_session.login(
                    url.scheme if url.scheme and url.scheme in ('http', 'https') else 'https',
                    url.host + ':' + str(url.port) if url.port else url.host,
                    url.request_uri if url.request_uri and url.request_uri != '/' else '/ajax/',
                    self._username,
                    self._password)

            capability = Capabilities().action_get('infostore', session_id)

            http_api_session.logout(session_id)

            if not capability or not capability.id or not capability.id == 'infostore':
                raise PermissionException('Account has no access to Drive')

            drive_api_response = requests.get('{}://{}{}drive'.format(
                    url.scheme if url.scheme and url.scheme in ('http', 'https') else 'https',
                    url.host + ':' + str(url.port) if url.port else url.host,
                    url.request_uri if url.request_uri and url.request_uri != '/' else '/ajax/'
            ))
            if drive_api_response.status_code > 400:
                raise DriveException('Drive API is not available on this server')

            account_valid = True
        except DriveException as e:
            logger.warning(e)
            account_valid = False
            message = str(e)
        except ValueError as e:
            logger.warning(e)
            account_valid = False
            message = str(e)
        except ConnectionError as e:
            logger.warning(e)
            account_valid = False
            message = 'Cannot connect to server'
        except (LocationValueError, InvalidURL) as e:
            logger.warning(e)
            account_valid = False
            message = 'Invalid server address'
        except SessionLoginException as e:
            logger.warning(e)
            account_valid = False
            message = str(e)
        except PermissionException as e:
            logger.warning(e)
            account_valid = False
            message = str(e)
        except RequestException as e:
            logger.error(e)
            account_valid = False
            message = 'Cannot connect to server'
        except Exception as e:
            logger.exception(e)
            account_valid = False
            message = 'Unknown Error'
        finally:
            self.finished.emit(account_valid, message)
