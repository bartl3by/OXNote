#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from appsuite_api_wrapper.models.appsuite_id_model import AppsuiteIdModel, IdAttributeMap

logger = logging.getLogger(__name__)


class DistributionListMemberAttributeMap(IdAttributeMap):
    id = 'id'
    folder_id = 'folder_id'
    display_name = 'display_name'
    mail = 'mail'
    mail_field = 'mail_field'


class DistributionListMember(AppsuiteIdModel):
    attribute_map_class = DistributionListMemberAttributeMap
    attribute_types = {
        'id': str,
        'folder_id': str,
        'display_name': str,
        'mail': str,
        'mail_field': float
    }

    def __init__(self, id=None, folder_id=None, display_name=None, mail=None, mail_field=None):
        self._id = None
        self._folder_id = None
        self._display_name = None
        self._mail = None
        self._mail_field = None
        self.discriminator = None

        if id is not None:
            self._id = id
        if folder_id is not None:
            self._folder_id = folder_id
        if display_name is not None:
            self._display_name = display_name
        if mail is not None:
            self._mail = mail
        if mail_field is not None:
            self._mail_field = mail_field

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def folder_id(self):
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        self._folder_id = folder_id

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def mail_field(self):
        return self._mail_field

    @mail_field.setter
    def mail_field(self, mail_field):
        self._mail_field = mail_field
