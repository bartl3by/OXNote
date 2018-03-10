#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from appsuite_api_wrapper.models.appsuite_id_model import IdAttributeMap, AppsuiteIdModel
from appsuite_api_wrapper.models.contact import Contact

logger = logging.getLogger(__name__)


class ObjectExtendedPermissionAttributeMap(IdAttributeMap):
    entity = 'entity'
    bits = 'bits'
    type = 'type'
    display_name = 'display_name'
    contact = 'contact'
    share_url = 'share_url'
    password = 'password'
    expiry_date = 'expiry_date'


class ObjectExtendedPermission(AppsuiteIdModel):
    attribute_map_class = ObjectExtendedPermissionAttributeMap
    attribute_types = {
        'entity': int,
        'bits': int,
        'type': str,
        'display_name': str,
        'contact': Contact,
        'share_url': str,
        'password': str,
        'expiry_date': int
    }

    def __init__(self, entity=None, bits=None, type=None, display_name=None, contact=None, share_url=None,
                 password=None, expiry_date=None):
        self._entity = None
        self._bits = None
        self._type = None
        self._display_name = None
        self._contact = None
        self._share_url = None
        self._password = None
        self._expiry_date = None

        if entity is not None:
            self._entity = entity
        if bits is not None:
            self._bits = bits
        if type is not None:
            self._type = type
        if display_name is not None:
            self._display_name = display_name
        if contact is not None:
            self._contact = contact
        if share_url is not None:
            self._share_url = share_url
        if password is not None:
            self._password = password
        if expiry_date is not None:
            self._expiry_date = expiry_date

    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, entity):
        self._entity = entity

    @property
    def bits(self):
        return self._bits

    @bits.setter
    def bits(self, bits):
        self._bits = bits

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def share_url(self):
        return self._share_url

    @share_url.setter
    def share_url(self, share_url):
        self._share_url = share_url

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        self._expiry_date = expiry_date
