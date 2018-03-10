#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import os
import typing
import uuid

import keyring
import ruamel.yaml as yaml
from ruamel.yaml.scalarstring import SingleQuotedScalarString

from util.configuration import Configuration
from util.environment import Environment

logger = logging.getLogger(__name__)


class AccountManager(object):
    KEYRING_APPLICATION_IDENTIFIER = 'OXNote'

    __cache = {}

    __account_configuration_file = None

    def __init__(self):
        if not self.__account_configuration_file:
            self.__account_configuration_file = os.path.join(self.get_accounts_root_directory_path(), 'accounts.yaml')

        if not self.__cache:
            try:
                self.load_all_account_configurations()
            except FileNotFoundError as e:
                self.__cache = {}
                logger.warning(e)

    def get_account(self, account_id: str) -> 'Account':
        return self.__cache[account_id] if account_id in self.__cache else None

    def set_account(self, account: 'Account'):
        self.__cache[account.id] = account

    def unload_account(self, account_id: str):
        if account_id in self.__cache:
            del self.__cache[account_id]

    def list_accounts(self) -> (typing.List[str], None):
        return list(self.__cache.keys()) if self.__cache else None

    def load_all_account_configurations(self):
        logger.debug('Loading account configurations from {}'.format(self.__account_configuration_file))

        if not os.path.isfile(self.__account_configuration_file):
            raise FileNotFoundError('{} does not exist'.format(self.__account_configuration_file))

        with open(self.__account_configuration_file, 'r') as f:
            configured_accounts = yaml.round_trip_load(f, preserve_quotes=True)

        for key in configured_accounts.keys():
            if key == 'version':
                continue

            try:
                configured_accounts[key]['password'] = keyring.get_password(
                        AccountManager.KEYRING_APPLICATION_IDENTIFIER, key)

                self.__cache[key] = Account.from_dict(key, configured_accounts[key])

                Environment.bootstrap_account_directories(self.__cache[key])
            except KeyError as e:
                logger.warning(e, exc_info=True)

    def load_account_configuration(self, account_id: str) -> 'Account':
        raise NotImplementedError

    def save_account_configuration(self, account: 'Account'):
        logger.debug('Writing new account configuration for {} to {}'.format(account.username,
                                                                             self.__account_configuration_file))

        self.set_account(account)

        with open(self.__account_configuration_file, 'w') as f:
            configuration_dictionary = {
                'version': 1.2
            }
            for id, cached_account in self.__cache.items():
                configuration_dictionary[id] = cached_account.as_dict()
                if 'password' in configuration_dictionary[id]:
                    del configuration_dictionary[id]['password']

            yaml.round_trip_dump(configuration_dictionary, f, default_flow_style=False)

            keyring.set_password(AccountManager.KEYRING_APPLICATION_IDENTIFIER, account.id, account.password)

        self.load_all_account_configurations()

    def disable_account(self, account: 'Account'):
        raise NotImplementedError

    def delete_account_configuration(self, delete_account_root: bool = False):
        raise NotImplementedError

    def get_accounts_root_directory_path(self) -> (str, None):
        return os.path.join(Environment.get_base_path(),
                            Configuration().get_setting('oxnote',
                                                        'application.directories.accounts',
                                                        default='.oxnote/accounts'))


class Account(object):

    def __init__(self, id: str = None, description: str = None, account_root_directory: str = None,
                 oxnote_home_folder: str = None, application_data_folder: str = None,
                 url_scheme: str = SingleQuotedScalarString('https'), url_host: str = None,
                 url_port: str = SingleQuotedScalarString('443'), url_uri: str = None, username: str = None,
                 password: str = None, context_id: str = None, user_id: str = None, enabled: bool = False,
                 drive_quota: int = 0):
        self._id = id
        self._description = description
        self._account_root_directory = account_root_directory
        self._oxnote_home_folder = oxnote_home_folder
        self._application_data_folder = application_data_folder
        self._url_scheme = url_scheme
        self._url_host = url_host
        self._url_port = url_port
        self._url_uri = url_uri
        self._username = username
        self._password = password
        self._context_id = context_id
        self._user_id = user_id
        self._enabled = enabled
        self._drive_quotas = drive_quota

    def as_dict(self) -> typing.Dict:
        account_as_dict = dict()

        account_as_dict['description'] = SingleQuotedScalarString(self.description)
        account_as_dict['account_root_directory'] = SingleQuotedScalarString(self.account_root_directory)
        account_as_dict['folder'] = dict()
        account_as_dict['folder']['oxnote_home_folder'] = SingleQuotedScalarString(self.oxnote_home_folder)
        account_as_dict['folder']['application_data_folder'] = SingleQuotedScalarString(self.application_data_folder)
        account_as_dict['url'] = dict()
        account_as_dict['url']['scheme'] = SingleQuotedScalarString(self.url_scheme)
        account_as_dict['url']['host'] = SingleQuotedScalarString(self.url_host)
        account_as_dict['url']['port'] = self.url_port
        account_as_dict['url']['uri'] = SingleQuotedScalarString(self.url_uri)
        account_as_dict['username'] = SingleQuotedScalarString(self.username)
        account_as_dict['password'] = SingleQuotedScalarString(self.password)
        account_as_dict['context_id'] = SingleQuotedScalarString(self.context_id)
        account_as_dict['user_id'] = SingleQuotedScalarString(self.user_id)
        account_as_dict['enabled'] = self.enabled
        account_as_dict['drive_quota'] = self.drive_quota

        return account_as_dict

    def assign_autogenerated_id(self):
        self._id = str(uuid.uuid4())

    @classmethod
    def from_dict(cls, id: str, account: typing.Dict) -> 'Account':
        instance = cls(id)

        instance.description = account['description']
        instance.account_root_directory = account['account_root_directory']
        instance.oxnote_home_folder = account['folder']['oxnote_home_folder']
        instance.application_data_folder = account['folder']['application_data_folder']
        instance.url_scheme = account['url']['scheme']
        instance.url_host = account['url']['host']
        instance.url_port = account['url']['port']
        instance.url_uri = account['url']['uri']
        instance.username = account['username']
        instance.password = account['password']
        instance.context_id = account['context_id']
        instance.user_id = account['user_id']
        instance.enabled = account['enabled']
        instance.drive_quota = account['drive_quota']

        return instance

    def get_account_root_directory_path(self) -> (str, None):
        if self._account_root_directory and self._oxnote_home_folder:
            return os.path.join(Environment.get_base_path(),
                                Configuration().get_setting('oxnote',
                                                            'application.directories.accounts',
                                                            default='.oxnote/accounts'),
                                self._account_root_directory)

    def get_oxnote_home_folder_path(self) -> (str, None):
        if self._account_root_directory and self._oxnote_home_folder:
            return os.path.join(self.get_account_root_directory_path(),
                                self._oxnote_home_folder)
        else:
            return None

    def get_application_data_folder_path(self) -> (str, None):
        if self._account_root_directory and self._application_data_folder:
            return os.path.join(self.get_account_root_directory_path(),
                                self._application_data_folder)
        else:
            return None

    def get_synchronization_statefile(self):
        return os.path.join(self.get_account_root_directory_path(),
                            Configuration().get_setting('drive_client',
                                                        'synchronization.state_filename',
                                                        default='state.yaml'))

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def account_root_directory(self):
        return self._account_root_directory

    @account_root_directory.setter
    def account_root_directory(self, account_root_directory):
        self._account_root_directory = account_root_directory

    @property
    def oxnote_home_folder(self):
        return self._oxnote_home_folder

    @oxnote_home_folder.setter
    def oxnote_home_folder(self, oxnote_home_folder):
        self._oxnote_home_folder = oxnote_home_folder

    @property
    def application_data_folder(self):
        return self._application_data_folder

    @application_data_folder.setter
    def application_data_folder(self, application_data_folder):
        self._application_data_folder = application_data_folder

    @property
    def url_scheme(self):
        return SingleQuotedScalarString('https') if not self._url_scheme else self._url_scheme

    @url_scheme.setter
    def url_scheme(self, url_scheme):
        self._url_scheme = url_scheme

    @property
    def url_host(self):
        return self._url_host

    @url_host.setter
    def url_host(self, url_host):
        self._url_host = url_host

    @property
    def url_port(self):
        return SingleQuotedScalarString('443') if not self._url_port else self._url_port

    @url_port.setter
    def url_port(self, url_port):
        self._url_port = url_port

    @property
    def url_uri(self):
        return self._url_uri

    @url_uri.setter
    def url_uri(self, url_uri):
        self._url_uri = url_uri

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def context_id(self):
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        self._context_id = context_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        self._enabled = enabled

    @property
    def drive_quota(self):
        return self._drive_quota

    @drive_quota.setter
    def drive_quota(self, drive_quota):
        self._drive_quota = drive_quota
