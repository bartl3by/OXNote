#!/usr/bin/python3#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import os
import typing

import ruamel.yaml
from requests import RequestException
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.scalarstring import SingleQuotedScalarString
from urllib3.exceptions import LocationValueError
from urllib3.util import parse_url

from appsuite_api_wrapper.exceptions import ApiException, DefaultFolderException, PermissionException, SessionException
from appsuite_api_wrapper.models.drive_extended_action import DriveExtendedAction
from appsuite_api_wrapper.models.drive_object_version import DriveObjectVersion
from appsuite_api_wrapper.modules.capabilities import Capabilities
from appsuite_api_wrapper.modules.drive import Drive
from appsuite_api_wrapper.session import HttpApiSession
from appsuite_api_wrapper.types import SynchronizationActionType
from appsuite_api_wrapper.util import Util

logger = logging.getLogger(__name__)


class DriveClient(object):

    def __init__(self,
                 username: str,
                 password: str,
                 url: str,
                 local_synchronization_directory: str,
                 synchronization_statefile: str,
                 compatible_api_version: str,
                 api_client_identifier: str,
                 session_id: str = None,
                 notification_callback=None):
        self._url = parse_url(url)

        self._username = username
        self._password = password

        self._local_synchronization_directory = local_synchronization_directory
        self._synchronization_statefile = synchronization_statefile
        self._compatible_api_version = compatible_api_version
        self._api_client_identifier = api_client_identifier

        self._session_id = session_id if session_id else None
        self._foreign_session_id = True if session_id else False

        self._notification_callback = notification_callback

        if not self._session_id:
            self._session_id = HttpApiSession().login(
                    self._url.scheme if self._url.scheme and self._url.scheme in ('http', 'https') else 'https',
                    self._url.host + ':' + str(self._url.port) if self._url.port else self._url.host,
                    self._url.request_uri if self._url.request_uri and self._url.request_uri != '/' else '/ajax/',
                    self._username, self._password)

        if not self.__drive_enabled():
            raise PermissionException('Account has no access to Drive/Infostore')
        else:
            self.__bootstrap_client()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __drive_enabled(self) -> bool:
        capability = Capabilities().action_get('infostore', self._session_id)

        if capability and capability.id and capability.id == 'infostore':
            return True
        else:
            return False

    def __bootstrap_synchronization_statefile(self, directory: str = None):
        synchronization_state = CommentedMap()
        if os.path.isfile(self._synchronization_statefile):
            synchronization_state = self.__load_synchronization_state()

        if 'version' not in synchronization_state:
            synchronization_state['version'] = 1.2
        if 'directories' not in synchronization_state:
            synchronization_state['directories'] = CommentedMap()
        if 'original_versions' not in synchronization_state['directories']:
            synchronization_state['directories']['original_versions'] = CommentedMap()
        if '/' not in synchronization_state['directories']['original_versions']:
            synchronization_state['directories']['original_versions']['/'] = CommentedMap()
        if 'files' not in synchronization_state:
            synchronization_state['files'] = CommentedMap()
        if 'original_versions' not in synchronization_state['files']:
            synchronization_state['files']['original_versions'] = CommentedMap()
        if '/' not in synchronization_state['files']['original_versions']:
            synchronization_state['files']['original_versions']['/'] = CommentedMap()

        if directory and '/{}'.format(directory) not in synchronization_state['files']['original_versions']:
            synchronization_state['files']['original_versions']['/{}'.format(directory)] = CommentedMap()

        self.__save_synchronization_state(synchronization_state)

    def __generate_client_versions_list(self, directory: str) -> typing.List:
        return [DriveObjectVersion(name=f, checksum=Util.calculate_file_checksum(
                os.path.join(self._local_synchronization_directory, directory, f))) for f in
                os.listdir(os.path.join(self._local_synchronization_directory, directory)) if
                os.path.isfile(os.path.join(self._local_synchronization_directory, directory, f))]

    def __generate_original_versions_list(self, synchronization_state: typing.Dict, directory: str) -> typing.List:
        return [DriveObjectVersion(name=f, checksum=c) for f, c in
                synchronization_state['files']['original_versions']['/{}'.format(directory)].items()]

    def __update_synchronization_state(self,
                                       directory: str,
                                       action: DriveExtendedAction,
                                       synchronization_state: typing.Dict) -> typing.Dict:
        '''
        ..todo: Account for the situation that a file has been moved and content has changed.
        '''
        if action.version and action.new_version:
            del synchronization_state['files']['original_versions']['/{}'.format(directory)][action.version.name]
            synchronization_state['files']['original_versions']['/{}'.format(directory)][
                action.new_version.name] = SingleQuotedScalarString(action.new_version.checksum)
        elif action.new_version:
            synchronization_state['files']['original_versions']['/{}'.format(directory)][
                action.new_version.name] = SingleQuotedScalarString(action.new_version.checksum)
        elif action.version:
            del synchronization_state['files']['original_versions']['/{}'.format(directory)][action.version.name]

        self.__save_synchronization_state(synchronization_state)

        return synchronization_state

    def __load_synchronization_state(self) -> typing.Dict:
        with open(self._synchronization_statefile, 'r') as f:
            return ruamel.yaml.round_trip_load(f, preserve_quotes=True)

    def __save_synchronization_state(self, synchronization_state: typing.Dict):
        with open(self._synchronization_statefile, 'w') as f:
            ruamel.yaml.round_trip_dump(synchronization_state, f, default_flow_style=False)

    def __bootstrap_client(self):
        self.__bootstrap_synchronization_statefile()

        drive_interface = Drive(
                device=self._api_client_identifier,
                api_version=self._compatible_api_version)

        drive_default_folder = list(d for d in drive_interface.action_subfolders(self._session_id) if d.default_folder)
        if len(drive_default_folder) <= 0:
            raise DefaultFolderException('No Infostore root folder found')
        elif len(drive_default_folder) > 1:
            raise DefaultFolderException('Found more than one root folder for Infostore')
        else:
            self._drive_default_folder = drive_default_folder[0]

    def __send_notification_callback(self, file: str, directory: str, synchronization_action_type: int, drive_extended_action: DriveExtendedAction):
        if self._notification_callback:
            self._notification_callback(file, directory, synchronization_action_type, drive_extended_action)

    def synchronize_files(self, directory: str = None):
        directory = '' if not directory else directory

        self.__bootstrap_synchronization_statefile(directory)

        try:
            if not os.path.isdir(os.path.join(self._local_synchronization_directory, directory)):
                os.makedirs(os.path.join(self._local_synchronization_directory, directory))

            synchronization_state = self.__load_synchronization_state()

            drive_client = Drive(
                    device=self._api_client_identifier,
                    api_version=self._compatible_api_version)

            '''
            Start synchronization cycle
            '''
            syncfiles_actions = drive_client.action_syncfiles(
                    root=self._drive_default_folder.id,
                    path='/{}'.format(directory),
                    drive_meta='false',
                    client_versions=self.__generate_client_versions_list(directory),
                    original_versions=self.__generate_original_versions_list(synchronization_state, directory),
                    session_id=self._session_id)

            '''
            Work through the actions that have been returned by the syncfiles action
            '''
            while len(syncfiles_actions) > 0:
                for action in syncfiles_actions:
                    if action.action == 'upload':
                        logger.info('Processing upload action for file {}'.format(action.new_version.name))

                        upload_actions = (drive_client.action_upload(
                                file=os.path.join(self._local_synchronization_directory,
                                                  directory,
                                                  action.new_version.name),
                                root=self._drive_default_folder.id,
                                path='/{}'.format(directory),
                                new_name=action.new_version.name if action.new_version else None,
                                new_checksum=action.new_version.checksum if action.new_version else None,
                                name=action.version.name if action.version else None,
                                checksum=action.version.checksum if action.version else None,
                                session_id=self._session_id))
                        if upload_actions:
                            self.__send_notification_callback(os.path.join(self._local_synchronization_directory,
                                                                           directory,
                                                                           action.new_version.name),
                                                              directory,
                                                              SynchronizationActionType.Upload, action)
                    elif action.action == 'acknowledge':
                        logger.info('Processing acknowledge action for file {}'.format(str(action)))

                        synchronization_state = self.__update_synchronization_state(directory, action,
                                                                                    synchronization_state)
                    elif action.action == 'remove':
                        logger.info('Processing remove action for file {}'.format(action.version.name))

                        os.remove(os.path.join(self._local_synchronization_directory,
                                               directory,
                                               action.version.name))
                        if synchronization_state['files']['original_versions']['/{}'.format(directory)][
                            action.version.name]:
                            del synchronization_state['files']['original_versions']['/{}'.format(directory)][
                                action.version.name]
                            synchronization_state = self.__update_synchronization_state(directory, action,
                                                                                        synchronization_state)

                            self.__send_notification_callback(os.path.join(self._local_synchronization_directory,
                                                                           directory, action.version.name),
                                                              directory, SynchronizationActionType.Remove, action)
                    elif action.action == 'edit':
                        logger.info('Processing edit action for file {}'.format(action.version.name))

                        synchronization_state = self.__update_synchronization_state(directory,
                                                                                    action,
                                                                                    synchronization_state)

                        if os.path.isfile(os.path.join(self._local_synchronization_directory,
                                                       directory,
                                                       action.version.name)):
                            os.rename(
                                    os.path.join(self._local_synchronization_directory, directory, action.version.name),
                                    os.path.join(self._local_synchronization_directory, directory,
                                                 action.new_version.name))

                            synchronization_state = self.__update_synchronization_state(directory,
                                                                                        action,
                                                                                        synchronization_state)
                            self.__send_notification_callback(os.path.join(self._local_synchronization_directory,
                                                                           directory,
                                                                           action.version.name),
                                                              directory, SynchronizationActionType.Rename, action)
                    elif action.action == 'download':
                        logger.info('Processing download action for file {}'.format(action.new_version.name))

                        file_bytes = drive_client.action_download(root=self._drive_default_folder.id,
                                                                  path='/{}'.format(directory),
                                                                  name=action.new_version.name,
                                                                  checksum=action.new_version.checksum,
                                                                  session_id=self._session_id)

                        with open(os.path.join(self._local_synchronization_directory,
                                               directory,
                                               action.new_version.name), 'wb') as f:
                            f.write(file_bytes)

                        synchronization_state = self.__update_synchronization_state(directory,
                                                                                    action,
                                                                                    synchronization_state)

                        if action.version and action.new_version:
                            self.__send_notification_callback(os.path.join(self._local_synchronization_directory, directory, action.new_version.name), directory, SynchronizationActionType.Download, action)
                        elif action.new_version:
                            self.__send_notification_callback(os.path.join(self._local_synchronization_directory, directory, action.new_version.name), directory, SynchronizationActionType.Download, action)
                        elif action.version:
                            self.__send_notification_callback(os.path.join(self._local_synchronization_directory, directory, action.version.name), directory, SynchronizationActionType.Download, action)
                    else:
                        raise ValueError('Unknown syncfiles action \'{}\''.format(action.action))

                logger.info(
                    'Finished processing through actions from last syncfiles requests executing a finalize syncfiles request.')

                syncfiles_actions = drive_client.action_syncfiles(
                        root=self._drive_default_folder.id,
                        path='/{}'.format(directory),
                        drive_meta='false',
                        client_versions=self.__generate_client_versions_list(directory),
                        original_versions=self.__generate_original_versions_list(synchronization_state, directory),
                        session_id=self._session_id)

            self.__save_synchronization_state(synchronization_state)
        except ConnectionError as e:
            logger.warning(e)
        except (SessionException, RequestException, LocationValueError, PermissionException) as e:
            logger.warning(e)
        except ApiException as e:
            logger.error(e, exc_info=True)
        except Exception as e:
            logger.exception(e)

    def close(self):
        if not self._foreign_session_id and self._session_id:
            try:
                HttpApiSession().logout(self._session_id)
            except Exception as e:
                logger.error('Unable to terminate session {}: '.format(self._session_id, e))
