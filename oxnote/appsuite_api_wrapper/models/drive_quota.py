#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from appsuite_api_wrapper.models.appsuite_id_model import IdAttributeMap, AppsuiteIdModel

logger = logging.getLogger(__name__)


class DriveQuotaAttributeMap(IdAttributeMap):
    type = 'type'
    limit = 'limit'
    use = 'use'


class DriveQuota(AppsuiteIdModel):
    attribute_map_class = DriveQuotaAttributeMap
    attribute_types = {
        'type': str,
        'limit': int,
        'use': int
    }

    def __init__(self, type=None, limit=None, use=None):
        self._type = None
        self._limit = None
        self._use = None

        if type is not None:
            self._type = type
        if limit is not None:
            self._limit = limit
        if use is not None:
            self._use = use

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        self._limit = limit

    @property
    def use(self):
        return self._use

    @use.setter
    def use(self, use):
        self._use = use
