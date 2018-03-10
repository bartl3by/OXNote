#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from typing import List

from appsuite_api_wrapper.models.appsuite_id_model import AppsuiteIdModel, IdAttributeMap
from appsuite_api_wrapper.models.drive_file_metadata import DriveFileMetadata
from appsuite_api_wrapper.models.folder_extended_permission import FolderExtendedPermission
from appsuite_api_wrapper.models.folder_permission import FolderPermission

logger = logging.getLogger(__name__)


class DriveDirectoryMetadataAttributeMap(IdAttributeMap):
    id = 'id'
    localized_name = 'localized_name'
    checksum = 'checksum'
    own_rights = 'own_rights'
    permissions = 'permissions'
    extended_permissions = 'extended_permissions'
    default_folder = 'default_folder'
    has_subfolders = 'has_subfolders'
    shared = 'shared'
    shareable = 'shareable'
    not_synchronizable = 'not_synchronizable'
    type = 'type'
    jump = 'jump'
    files = 'files'
    path = 'path'
    name = 'name'


class DriveDirectoryMetadata(AppsuiteIdModel):
    attribute_map_class = DriveDirectoryMetadataAttributeMap
    attribute_types = {
        'id': str,
        'localized_name': str,
        'checksum': str,
        'own_rights': int,
        'permissions': List[FolderPermission],
        'extended_permissions': List[FolderExtendedPermission],
        'default_folder': bool,
        'has_subfolders': bool,
        'shared': bool,
        'shareable': bool,
        'not_synchronizable': bool,
        'type': int,
        'jump': List[str],
        'files': List[DriveFileMetadata],
        'path': str,
        'name': str
    }

    def __init__(self, id=None, localized_name=None, checksum=None, own_rights=None, permissions=None,
                 extended_permissions=None, default_folder=None, has_subfolders=None, shared=None, shareable=None,
                 not_synchronizable=None, type=None, jump=None, files=None, path=None, name=None):
        self._id = None
        self._localized_name = None
        self._checksum = None
        self._own_rights = None
        self._permissions = None
        self._extended_permissions = None
        self._default_folder = None
        self._has_subfolders = None
        self._shared = None
        self._shareable = None
        self._not_synchronizable = None
        self._type = None
        self._jump = None
        self._files = None
        self._path = None
        self._name = None

        if id is not None:
            self._id = id
        if localized_name is not None:
            self._localized_name = localized_name
        if checksum is not None:
            self._checksum = checksum
        if own_rights is not None:
            self._own_rights = own_rights
        if permissions is not None:
            self._permissions = permissions
        if extended_permissions is not None:
            self._extended_permissions = extended_permissions
        if default_folder is not None:
            self._default_folder = default_folder
        if has_subfolders is not None:
            self._has_subfolders = has_subfolders
        if shared is not None:
            self._shared = shared
        if shareable is not None:
            self._shareable = shareable
        if not_synchronizable is not None:
            self._not_synchronizable = not_synchronizable
        if type is not None:
            self._type = type
        if jump is not None:
            self._jump = jump
        if files is not None:
            self._files = files
        if path is not None:
            self._path = path
        if name is not None:
            self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def localized_name(self):
        return self._localized_name

    @localized_name.setter
    def localized_name(self, localized_name):
        self._localized_name = localized_name

    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        self._checksum = checksum

    @property
    def own_rights(self):
        return self._own_rights

    @own_rights.setter
    def own_rights(self, own_rights):
        self._own_rights = own_rights

    @property
    def permissions(self):
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        self._permissions = permissions

    @property
    def extended_permissions(self):
        return self._extended_permissions

    @extended_permissions.setter
    def extended_permissions(self, extended_permissions):
        self._extended_permissions = extended_permissions

    @property
    def default_folder(self):
        return self._default_folder

    @default_folder.setter
    def default_folder(self, default_folder):
        self._default_folder = default_folder

    @property
    def has_subfolders(self):
        return self._has_subfolders

    @has_subfolders.setter
    def has_subfolders(self, has_subfolders):
        self._has_subfolders = has_subfolders

    @property
    def shared(self):
        return self._shared

    @shared.setter
    def shared(self, shared):
        self._shared = shared

    @property
    def shareable(self):
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        self._shareable = shareable

    @property
    def not_synchronizable(self):
        return self._not_synchronizable

    @not_synchronizable.setter
    def not_synchronizable(self, not_synchronizable):
        self._not_synchronizable = not_synchronizable

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def jump(self):
        return self._jump

    @jump.setter
    def jump(self, jump):
        self._jump = jump

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, files):
        self._files = files

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
