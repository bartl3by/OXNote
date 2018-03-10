#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from typing import Dict

from appsuite_api_wrapper.models.appsuite_id_model import AppsuiteIdModel, IdAttributeMap

logger = logging.getLogger(__name__)


class CapabilityAttributeMap(IdAttributeMap):
    id = 'id'
    attributes = 'attributes'


class Capability(AppsuiteIdModel):
    attribute_map_class = CapabilityAttributeMap
    attribute_types = {
        'id': str,
        'attributes': Dict[str, str]
    }

    def __init__(self, id=None, attributes=None):
        self._id = None
        self._attributes = None

        if id is not None:
            self._id = id
        if attributes is not None:
            self._attributes = attributes

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        self._attributes = attributes
