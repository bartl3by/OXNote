#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import typing

from appsuite_api_wrapper.models.appsuite_model import AppsuiteAttributeMap, AppsuiteModel

logger = logging.getLogger(__name__)


class IdAttributeMap(AppsuiteAttributeMap):

    @classmethod
    def all_columns(cls) -> typing.List[str]:
        return list((cls.all_columns_map()).values())

    @classmethod
    def all_columns_map(cls) -> typing.Dict[str, str]:
        all_columns_map = dict()
        for attribute in [i for i in cls.__dict__.keys() if i[:1] != '_']:
            if isinstance((getattr(cls, attribute)), str):
                all_columns_map[attribute] = (getattr(cls, attribute))

        return all_columns_map

    @classmethod
    def attribute_name(cls, attribute_id: str) -> str:
        for attribute in [i for i in cls.__dict__.keys() if i[:1] != '_']:
            if getattr(cls, attribute) == attribute_id:
                return attribute

    @staticmethod
    def generate_columns_string(columns: typing.List[str]):
        column_string = ''
        for column in columns:
            column_string += column if len(column_string) <= 0 else ',' + column

        return column_string


class AppsuiteIdModel(AppsuiteModel):
    attribute_types = {}

    def __eq__(self, other):
        if not isinstance(other, AppsuiteIdModel):
            return False

        return self.__dict__ == other.__dict__

    @classmethod
    def from_api_response(cls, data: (typing.List, typing.Dict), columns: typing.List[int] = None):
        return cls._deserialize(cls, data, columns)

    @staticmethod
    def _deserialize_model(cls, data: typing.Dict, columns: typing.List[int] = None):
        kwargs = {}

        if isinstance(cls(), AppsuiteIdModel):
            for attr, attr_type in cls.attribute_types.items():
                if data and getattr(cls.attribute_map_class, attr, attr) in data and type(data) in (
                        list, dict):
                    value = data[getattr(cls.attribute_map_class, attr, attr)]
                    kwargs[attr] = AppsuiteIdModel._deserialize(attr_type, value)

            return cls(**kwargs)
