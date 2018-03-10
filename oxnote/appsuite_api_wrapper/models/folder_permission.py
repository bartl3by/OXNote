#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from appsuite_api_wrapper.models.appsuite_id_model import IdAttributeMap, AppsuiteIdModel

logger = logging.getLogger(__name__)


class FolderPermissionAttributeMap(IdAttributeMap):
    bits = 'bits'
    rights = 'rights'
    entity = 'entity'
    group = 'group'
    type = 'type'
    password = 'password'
    email_address = 'email_address'
    display_name = 'display_name'
    contact_id = 'contact_id'
    contact_folder = 'contact_folder'
    expiry_date = 'expiry_date'


class FolderPermission(AppsuiteIdModel):
    attribute_map_class = FolderPermissionAttributeMap
    attribute_types = {
        'bits': int,
        'rights': str,
        'entity': int,
        'group': bool,
        'type': str,
        'password': str,
        'email_address': str,
        'display_name': str,
        'contact_id': str,
        'contact_folder': str,
        'expiry_date': int
    }

    def __init__(self, bits=None, rights=None, entity=None, group=None, type=None, password=None, email_address=None,
                 display_name=None, contact_id=None, contact_folder=None, expiry_date=None):
        self._bits = None
        self._rights = None
        self._entity = None
        self._group = None
        self._type = None
        self._password = None
        self._email_address = None
        self._display_name = None
        self._contact_id = None
        self._contact_folder = None
        self._expiry_date = None

        if bits is not None:
            self._bits = bits
        if rights is not None:
            self._rights = rights
        if entity is not None:
            self._entity = entity
        if group is not None:
            self._group = group
        if type is not None:
            self._type = type
        if password is not None:
            self._password = password
        if email_address is not None:
            self._email_address = email_address
        if display_name is not None:
            self._display_name = display_name
        if contact_id is not None:
            self._contact_id = contact_id
        if contact_folder is not None:
            self._contact_folder = contact_folder
        if expiry_date is not None:
            self._expiry_date = expiry_date

    @property
    def bits(self):
        return self._bits

    @bits.setter
    def bits(self, bits):
        self._bits = bits

    @property
    def rights(self):
        return self._rights

    @rights.setter
    def rights(self, rights):
        self._rights = rights

    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, entity):
        self._entity = entity

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        self._group = group

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        self._email_address = email_address

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def contact_folder(self):
        return self._contact_folder

    @contact_folder.setter
    def contact_folder(self, contact_folder):
        self._contact_folder = contact_folder

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        self._expiry_date = expiry_date
