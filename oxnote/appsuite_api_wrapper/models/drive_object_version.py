#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from appsuite_api_wrapper.models.appsuite_id_model import IdAttributeMap, AppsuiteIdModel

logger = logging.getLogger(__name__)


class DriveObjectVersionAttributeMap(IdAttributeMap):
    name = 'name'
    checksum = 'checksum'


class DriveObjectVersion(AppsuiteIdModel):
    attribute_map_class = DriveObjectVersionAttributeMap
    attribute_types = {
        'name': str,
        'path': str,
        'checksum': str
    }

    def __init__(self, name=None, path=None, checksum=None):
        self._name = None
        self._path = None
        self._checksum = None

        if name is not None:
            self._name = name
        if path is not None:
            self._path = path
        if checksum is not None:
            self._checksum = checksum

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        self._checksum = checksum
