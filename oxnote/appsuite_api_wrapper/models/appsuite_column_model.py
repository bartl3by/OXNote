#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import typing

from appsuite_api_wrapper.models.appsuite_model import AppsuiteAttributeMap, AppsuiteModel

logger = logging.getLogger(__name__)


class ColumnAttributeMap(AppsuiteAttributeMap):

    @classmethod
    def all_columns(cls) -> typing.List[int]:
        return list((cls.all_columns_map()).values())

    @classmethod
    def all_columns_map(cls) -> typing.Dict[str, int]:
        all_columns_map = dict()
        for attribute in [i for i in cls.__dict__.keys() if i[:1] != '_']:
            if isinstance((getattr(cls, attribute)), int):
                all_columns_map[attribute] = (getattr(cls, attribute))

        return all_columns_map

    @classmethod
    def attribute_name(cls, attribute_id: int) -> str:
        for attribute in [i for i in cls.__dict__.keys() if i[:1] != '_']:
            if getattr(cls, attribute) == attribute_id:
                return attribute

    @staticmethod
    def generate_columns_string(columns: typing.List[int]):
        column_string = ''
        for column in columns:
            column_string += str(column) if len(column_string) <= 0 else ',' + str(column)

        return column_string


class AppsuiteColumnModel(AppsuiteModel):
    attribute_map_class = AppsuiteAttributeMap
    attribute_types = {}

    def __eq__(self, other):
        if not isinstance(other, AppsuiteColumnModel):
            return False

        return self.__dict__ == other.__dict__

    @classmethod
    def from_api_response(cls, data: (typing.List, typing.Dict), columns: typing.List[int] = None):
        if isinstance(cls(), AppsuiteColumnModel) and (not columns or len(columns) <= 0):
            raise ValueError('AppsuiteColumnModel requires columns parameter for deserialization')

        return cls._deserialize(cls, data, columns)

    @staticmethod
    def _deserialize_model(cls, data: typing.Dict, columns: typing.List[int] = None):
        if isinstance(cls(), AppsuiteColumnModel) and (not columns or len(columns) <= 0):
            raise ValueError('AppsuiteColumnModel requires columns parameter for deserialization')

        kwargs = {}

        if isinstance(cls(), AppsuiteColumnModel):
            if not columns or len(columns) <= 0:
                raise ValueError('AppsuiteColumnModel requires columns parameter for deserialization')

            if data and type(data) in (list, dict):
                for position, value in enumerate(data):
                    if value:
                        attr = cls.attribute_map_class.attribute_name(columns[position])
                        kwargs[attr] = AppsuiteColumnModel._deserialize(cls.attribute_types[attr], value)

                return cls(**kwargs)
