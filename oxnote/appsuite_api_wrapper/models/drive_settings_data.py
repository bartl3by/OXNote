#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import typing

from appsuite_api_wrapper.models.appsuite_id_model import AppsuiteIdModel, IdAttributeMap
from appsuite_api_wrapper.models.drive_quota import DriveQuota

logger = logging.getLogger(__name__)


class DriveSettingsDataAttributeMap(IdAttributeMap):
    quota = 'quota'
    quota_manage_link = 'quotaManageLink'
    help_link = 'helpLink'
    server_version = 'serverVersion'
    supported_api_version = 'supportedApiVersion'
    min_api_version = 'minApiVersion'
    localized_folder_names = 'localizedFolderNames'
    capabilities = 'capabilities'


class DriveSettingsData(AppsuiteIdModel):
    attribute_map_class = DriveSettingsDataAttributeMap
    attribute_types = {
        'quota': typing.List[DriveQuota],
        'quota_manage_link': str,
        'help_link': str,
        'server_version': str,
        'supported_api_version': str,
        'min_api_version': str,
        'localized_folder_names': typing.Dict[str, str],
        'capabilities': typing.List[str]
    }

    def __init__(self, quota=None, quota_manage_link=None, help_link=None, server_version=None,
                 supported_api_version=None, min_api_version=None, localized_folder_names=None, capabilities=None):
        self._quota = None
        self._quota_manage_link = None
        self._help_link = None
        self._server_version = None
        self._supported_api_version = None
        self._min_api_version = None
        self._localized_folder_names = None
        self._capabilities = None

        if quota is not None:
            self._quota = quota
        if quota_manage_link is not None:
            self._quota_manage_link = quota_manage_link
        if help_link is not None:
            self._help_link = help_link
        if server_version is not None:
            self._server_version = server_version
        if supported_api_version is not None:
            self._supported_api_version = supported_api_version
        if min_api_version is not None:
            self._min_api_version = min_api_version
        if localized_folder_names is not None:
            self._localized_folder_names = localized_folder_names
        if capabilities is not None:
            self._capabilities = capabilities

    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, quota):
        self._quota = quota

    @property
    def quota_manage_link(self):
        return self._quota_manage_link

    @quota_manage_link.setter
    def quota_manage_link(self, quota_manage_link):
        self._quota_manage_link = quota_manage_link

    @property
    def help_link(self):
        return self._help_link

    @help_link.setter
    def help_link(self, help_link):
        self._help_link = help_link

    @property
    def server_version(self):
        return self._server_version

    @server_version.setter
    def server_version(self, server_version):
        self._server_version = server_version

    @property
    def supported_api_version(self):
        return self._supported_api_version

    @supported_api_version.setter
    def supported_api_version(self, supported_api_version):
        self._supported_api_version = supported_api_version

    @property
    def min_api_version(self):
        return self._min_api_version

    @min_api_version.setter
    def min_api_version(self, min_api_version):
        self._min_api_version = min_api_version

    @property
    def localized_folder_names(self):
        return self._localized_folder_names

    @localized_folder_names.setter
    def localized_folder_names(self, localized_folder_names):
        self._localized_folder_names = localized_folder_names

    @property
    def capabilities(self):
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        self._capabilities = capabilities
