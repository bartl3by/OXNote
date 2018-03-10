#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import typing

from appsuite_api_wrapper.models.appsuite_id_model import IdAttributeMap, AppsuiteIdModel

logger = logging.getLogger(__name__)


class DriveSyncErrorDataAttributeMap(IdAttributeMap):
    error = 'error'
    error_params = 'error_params'
    error_id = 'error_id'
    error_desc = 'error_desc'
    code = 'code'
    categories = 'categories'
    category = 'category'


class DriveSyncErrorData(AppsuiteIdModel):
    attribute_map_class = DriveSyncErrorDataAttributeMap
    attribute_types = {
        'error': str,
        'error_params': typing.List[str],
        'error_id': str,
        'error_desc': str,
        'code': str,
        'categories': str,
        'category': int
    }

    def __init__(self, error=None, error_params=None, error_id=None, error_desc=None, code=None, categories=None,
                 category=None):
        self._error = None
        self._error_params = None
        self._error_id = None
        self._error_desc = None
        self._code = None
        self._categories = None
        self._category = None

        if error is not None:
            self._error = error
        if error_params is not None:
            self._error_params = error_params
        if error_id is not None:
            self._error_id = error_id
        if error_desc is not None:
            self._error_desc = error_desc
        if code is not None:
            self._code = code
        if categories is not None:
            self._categories = categories
        if category is not None:
            self._category = category

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error):
        self._error = error

    @property
    def error_params(self):
        return self._error_params

    @error_params.setter
    def error_params(self, error_params):
        self._error_params = error_params

    @property
    def error_id(self):
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        self._error_id = error_id

    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, error_desc):
        self._error_desc = error_desc

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, categories):
        self._categories = categories

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category
