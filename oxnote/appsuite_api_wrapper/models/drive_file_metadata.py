#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from typing import List

from appsuite_api_wrapper.models.appsuite_id_model import AppsuiteIdModel, IdAttributeMap
from appsuite_api_wrapper.models.drive_file_version_metadata import DriveFileVersionMetadata
from appsuite_api_wrapper.models.object_extended_permission import ObjectExtendedPermission
from appsuite_api_wrapper.models.object_permission import ObjectPermission

logger = logging.getLogger(__name__)


class DriveFileMetadataAttributeMap(IdAttributeMap):
    name = 'name'
    checksum = 'checksum'
    path = 'path'
    created = 'created'
    modified = 'modified'
    created_by = 'created_by'
    modified_by = 'modified_by'
    content_type = 'content_type'
    preview = 'preview'
    thumbnail = 'thumbnail'
    object_permissions = 'object_permissions'
    extended_object_permissions = 'extended_object_permissions'
    shared = 'shared'
    shareable = 'shareable'
    locked = 'locked'
    jump = 'jump'
    number_of_versions = 'number_of_versions'
    version = 'version'
    version_comment = 'version_comment'
    versions = 'versions'


class DriveFileMetadata(AppsuiteIdModel):
    attribute_map_class = DriveFileMetadataAttributeMap
    attribute_types = {
        'name': str,
        'checksum': str,
        'path': str,
        'created': int,
        'modified': int,
        'created_by': int,
        'modified_by': int,
        'content_type': str,
        'preview': str,
        'thumbnail': str,
        'object_permissions': List[ObjectPermission],
        'extended_object_permissions': List[ObjectExtendedPermission],
        'shared': bool,
        'shareable': bool,
        'locked': bool,
        'jump': 'list[str]',
        'number_of_versions': int,
        'version': str,
        'version_comment': str,
        'versions': List[DriveFileVersionMetadata]
    }

    def __init__(self, name=None, checksum=None, path=None, created=None, modified=None, created_by=None,
                 modified_by=None, content_type=None, preview=None, thumbnail=None, object_permissions=None,
                 extended_object_permissions=None, shared=None, shareable=None, locked=None, jump=None,
                 number_of_versions=None, version=None, version_comment=None, versions=None):
        self._name = None
        self._checksum = None
        self._path = None
        self._created = None
        self._modified = None
        self._created_by = None
        self._modified_by = None
        self._content_type = None
        self._preview = None
        self._thumbnail = None
        self._object_permissions = None
        self._extended_object_permissions = None
        self._shared = None
        self._shareable = None
        self._locked = None
        self._jump = None
        self._number_of_versions = None
        self._version = None
        self._version_comment = None
        self._versions = None

        if name is not None:
            self.name = name
        if checksum is not None:
            self.checksum = checksum
        if path is not None:
            self.path = path
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if content_type is not None:
            self.content_type = content_type
        if preview is not None:
            self.preview = preview
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if object_permissions is not None:
            self.object_permissions = object_permissions
        if extended_object_permissions is not None:
            self.extended_object_permissions = extended_object_permissions
        if shared is not None:
            self.shared = shared
        if shareable is not None:
            self.shareable = shareable
        if locked is not None:
            self.locked = locked
        if jump is not None:
            self.jump = jump
        if number_of_versions is not None:
            self.number_of_versions = number_of_versions
        if version is not None:
            self.version = version
        if version_comment is not None:
            self.version_comment = version_comment
        if versions is not None:
            self.versions = versions

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        self._checksum = checksum

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, created):
        self._created = created

    @property
    def modified(self):
        return self._modified

    @modified.setter
    def modified(self, modified):
        self._modified = modified

    @property
    def created_by(self):
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        self._created_by = created_by

    @property
    def modified_by(self):
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        self._modified_by = modified_by

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        self._content_type = content_type

    @property
    def preview(self):
        return self._preview

    @preview.setter
    def preview(self, preview):
        self._preview = preview

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        self._thumbnail = thumbnail

    @property
    def object_permissions(self):
        return self._object_permissions

    @object_permissions.setter
    def object_permissions(self, object_permissions):
        self._object_permissions = object_permissions

    @property
    def extended_object_permissions(self):
        return self._extended_object_permissions

    @extended_object_permissions.setter
    def extended_object_permissions(self, extended_object_permissions):
        self._extended_object_permissions = extended_object_permissions

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
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, locked):
        self._locked = locked

    @property
    def jump(self):
        return self._jump

    @jump.setter
    def jump(self, jump):
        self._jump = jump

    @property
    def number_of_versions(self):
        return self._number_of_versions

    @number_of_versions.setter
    def number_of_versions(self, number_of_versions):
        self._number_of_versions = number_of_versions

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def version_comment(self):
        return self._version_comment

    @version_comment.setter
    def version_comment(self, version_comment):
        self._version_comment = version_comment

    @property
    def versions(self):
        return self._versions

    @versions.setter
    def versions(self, versions):
        self._versions = versions
