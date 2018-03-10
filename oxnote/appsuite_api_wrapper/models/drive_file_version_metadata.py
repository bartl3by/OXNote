#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from appsuite_api_wrapper.models.appsuite_id_model import AppsuiteIdModel, IdAttributeMap

logger = logging.getLogger(__name__)


class DriveFileVersionMetadataAttributeMap(IdAttributeMap):
    name = 'name'
    file_size = 'file_size'
    created = 'created'
    modified = 'modified'
    created_by = 'created_by'
    modified_by = 'modified_by'
    version = 'version'
    version_comment = 'version_comment'


class DriveFileVersionMetadata(AppsuiteIdModel):
    attribute_map_class = DriveFileVersionMetadataAttributeMap
    attribute_types = {
        'name': str,
        'file_size': int,
        'created': int,
        'modified': int,
        'created_by': int,
        'modified_by': int,
        'version': str,
        'version_comment': str
    }

    def __init__(self, name=None, file_size=None, created=None, modified=None, created_by=None, modified_by=None,
                 version=None, version_comment=None):
        self._name = None
        self._file_size = None
        self._created = None
        self._modified = None
        self._created_by = None
        self._modified_by = None
        self._version = None
        self._version_comment = None

        if name is not None:
            self._name = name
        if file_size is not None:
            self._file_size = file_size
        if created is not None:
            self._created = created
        if modified is not None:
            self._modified = modified
        if created_by is not None:
            self._created_by = created_by
        if modified_by is not None:
            self._modified_by = modified_by
        if version is not None:
            self._version = version
        if version_comment is not None:
            self._version_comment = version_comment

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        self._file_size = file_size

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
