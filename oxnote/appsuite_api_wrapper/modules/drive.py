#!/usr/bin/python3#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import typing
from typing import List

from appsuite_api_wrapper.exceptions import DriveException
from appsuite_api_wrapper.models.drive_action import DriveAction
from appsuite_api_wrapper.models.drive_directory_metadata import DriveDirectoryMetadata
from appsuite_api_wrapper.models.drive_extended_action import DriveExtendedAction
from appsuite_api_wrapper.models.drive_object_version import DriveObjectVersion
from appsuite_api_wrapper.models.drive_settings_data import DriveSettingsData
from appsuite_api_wrapper.session import HttpApiSession

logger = logging.getLogger(__name__)

_api_path_drive = 'drive'

_api_action_get_folder = 'getFolder'
_api_action_download = 'download'
_api_action_subfolders = 'subfolders'
_api_action_settings = 'settings'
_api_action_syncfiles = 'syncfiles'
_api_action_syncfolders = 'syncfolders'
_api_action_upload = 'upload'


class Drive(HttpApiSession):

    def __init__(self, device: str, api_version: str):
        self._device = device
        self._api_version = api_version

    def action_get_folder(self, root: str, path: str, checksum: str, session_id: str) -> DriveDirectoryMetadata:
        request_parameters = {
            'root': root,
            'path': path,
            'checksum': checksum
        }

        response = self.authenticated_get(_api_path_drive,
                                          _api_action_get_folder,
                                          session_id,
                                          params=request_parameters)

        data = response.json(encoding='utf-8')
        if 'data' in data:
            return DriveDirectoryMetadata.from_api_response(data['data'])

    def action_download(self,
                        root: str,
                        path: str,
                        name: str,
                        checksum: str,
                        session_id: str,
                        offset: int = None,
                        length: int = None) -> bytes:
        request_parameters = {
            'root': root,
            'path': path,
            'name': name,
            'checksum': checksum,
            'apiVersion': self._api_version,
            'offset': offset,
            'length': length
        }

        response = self.authenticated_get(_api_path_drive,
                                          _api_action_download,
                                          session_id,
                                          params=request_parameters,
                                          stream=True)

        if response.status_code == 200 and response.content:
            return response.content
        else:
            raise DriveException('Empty response for drive download action, http status code {} was returned'.format(
                response.status_code))

    def action_subfolders(self, session_id: str, parent: str = None) -> List[DriveDirectoryMetadata]:
        request_parameters = {
            'parent': parent
        }

        response = self.authenticated_get(_api_path_drive,
                                          _api_action_subfolders,
                                          session_id,
                                          params=request_parameters)

        data = response.json(encoding='utf-8')
        if 'data' in data:
            return [DriveDirectoryMetadata.from_api_response(item) for item in data['data']]

    def action_settings(self, session_id: str, root: str = '0', language: str = None) -> DriveSettingsData:
        request_parameters = {
            'root': root,
            'language': language
        }

        response = self.authenticated_get(_api_path_drive,
                                          _api_action_settings,
                                          session_id,
                                          params=request_parameters)

        data = response.json(encoding='utf-8')
        if 'data' in data:
            return DriveSettingsData.from_api_response(data['data'])

    def action_syncfiles(self,
                         root: str,
                         path: str,
                         session_id: str,
                         diagnostics: bool = False,
                         push_token: str = None,
                         drive_meta: str = None,
                         client_versions: typing.List[DriveObjectVersion] = None,
                         original_versions: typing.List[DriveObjectVersion] = None) -> typing.List[DriveExtendedAction]:
        request_parameters = {
            'root': root,
            'path': path,
            'device': self._device,
            'apiVersion': self._api_version,
            'diagnostics': diagnostics,
            'pushToken': push_token,
            'driveMeta': drive_meta
        }
        request_json = { }

        if client_versions and len(client_versions) > 0:
            request_json['clientVersions'] = [item.to_dict() for item in client_versions]

        if original_versions and len(original_versions) > 0:
            request_json['originalVersions'] = [item.to_dict() for item in original_versions]

        response = self.authenticated_put(_api_path_drive,
                                          _api_action_syncfiles,
                                          session_id,
                                          params=request_parameters,
                                          json=request_json)

        data = response.json(encoding='utf-8')
        if 'data' in data:
            return [DriveExtendedAction.from_api_response(item) for item in data['data']['actions']]

    def action_syncfolders(self,
                           root: str,
                           session_id: str,
                           version: str = '0',
                           diagnostics: bool = False,
                           push_token: str = None,
                           client_versions: typing.List[DriveObjectVersion] = None,
                           original_versions: typing.List[DriveObjectVersion] = None) -> typing.List[DriveAction]:
        request_parameters = {
            'root': root,
            'version': version,
            'apiVersion': self._api_version,
            'diagnostics': diagnostics,
            'pushToken': push_token
        }
        request_json = { }

        if client_versions and len(client_versions) > 0:
            request_json['clientVersions'] = [item.to_dict() for item in client_versions]

        if original_versions and len(original_versions) > 0:
            request_json['originalVersions'] = [item.to_dict() for item in original_versions]

        response = self.authenticated_put(_api_path_drive,
                                          _api_action_syncfolders,
                                          session_id,
                                          params=request_parameters,
                                          json=request_json)

        data = response.json(encoding='utf-8')
        if 'data' in data:
            return [DriveAction.from_api_response(item) for item in data['data']['actions']]

    def action_upload(self,
                      file: str,
                      root: str,
                      path: str,
                      new_name: str,
                      new_checksum: str,
                      session_id: str,
                      name: str = None,
                      checksum: str = None,
                      content_type: str = None,
                      offset: int = None,
                      total_length: int = None,
                      created: int = None,
                      modified: int = None,
                      diagnostics: bool = False,
                      push_token: str = None) -> typing.List[DriveAction]:
        request_parameters = {
            'root': root,
            'path': path,
            'newName': new_name,
            'newChecksum': new_checksum,
            'name': name,
            'checksum': checksum,
            'apiVersion': self._api_version,
            'contentType': content_type,
            'offset': offset,
            'totalLength': total_length,
            'created': created,
            'modified': modified,
            'device': self._device,
            'diagnostics': diagnostics,
            'pushToken': push_token
        }

        response = self.authenticated_post(_api_path_drive,
                                           _api_action_upload,
                                           session_id,
                                           data=open(file, 'rb'),
                                           params=request_parameters)

        data = response.json(encoding='utf-8')
        if 'data' in data:
            return [DriveAction.from_api_response(item) for item in data['data']['actions']]
