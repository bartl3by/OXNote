#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import logging
import typing

from dateutil.parser import parse

logger = logging.getLogger(__name__)


class AppsuiteAttributeMap(object):

    @classmethod
    def all_columns(cls): raise NotImplementedError

    @classmethod
    def all_columns_map(cls): raise NotImplementedError

    @classmethod
    def attribute_name(cls, attribute_id): raise NotImplementedError

    @staticmethod
    def generate_columns_string(columns): raise NotImplementedError


class AppsuiteModel(object):
    attribute_types = {}

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, AppsuiteModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def to_dict(self):
        result = {}

        for attr, _ in self.attribute_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, 'to_dict') else x, value))
            elif hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], 'to_dict') else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    @classmethod
    def from_api_response(cls, data: (typing.List, typing.Dict), columns: typing.List[int] = None):
        raise NotImplementedError

    @staticmethod
    def _deserialize(cls, data: (typing.List, typing.Dict), columns: typing.List[int] = None):
        if not data:
            return None

        if type(cls) == typing.GenericMeta:
            if cls.__extra__ == list:
                return [AppsuiteModel._deserialize(cls.__args__[0], sub_data) for sub_data in data]
            if cls.__extra__ == dict:
                return {k: AppsuiteModel._deserialize(cls.__args__[1], v) for k, v in data.items()}
        elif cls in (bool, bytes, float, int, str):
            return cls(data)
        elif cls == object:
            return data
        elif cls == datetime.date or cls == datetime.datetime:
            try:
                if cls == datetime.date:
                    return parse(data).date()
                elif cls == datetime.datetime:
                    return parse(data)
            except ValueError:
                logger.error('Failed to parse {} as date / datetime, using string value'.format(str(data)))
                return str(data)
        else:
            if not hasattr(cls, 'attribute_types') and not cls.attribute_types:
                return data

            return cls._deserialize_model(cls, data, columns)

    @staticmethod
    def _deserialize_model(cls, data: typing.Dict, columns: typing.List[int] = None): raise NotImplementedError
