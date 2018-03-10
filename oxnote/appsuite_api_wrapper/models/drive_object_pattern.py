#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from appsuite_api_wrapper.models.appsuite_id_model import IdAttributeMap, AppsuiteIdModel

logger = logging.getLogger(__name__)


class ObjectPermissionAttributeMap(IdAttributeMap):
    type = 'type'
    path = 'path'
    name = 'name'
    case_sensitive = 'caseSensitive'


class ObjectPermission(AppsuiteIdModel):
    attribute_map_class = ObjectPermissionAttributeMap
    attribute_types = {
        'type': str,
        'path': str,
        'name': str,
        'case_sensitive': bool
    }

    def __init__(self, type=None, path=None, name=None, case_sensitive=None):
        self._type = None
        self._path = None
        self._name = None
        self._case_sensitive = None

        if type is not None:
            self._type = type
        if path is not None:
            self._path = path
        if name is not None:
            self._name = name
        if case_sensitive is not None:
            self._case_sensitive = case_sensitive

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

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

    @property
    def case_sensitive(self):
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        self._case_sensitive = case_sensitive
