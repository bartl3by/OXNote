#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from typing import List

from appsuite_api_wrapper.models.appsuite_column_model import AppsuiteColumnModel, ColumnAttributeMap
from appsuite_api_wrapper.models.folder_extended_permission import FolderExtendedPermission
from appsuite_api_wrapper.models.folder_permission import FolderPermission

logger = logging.getLogger(__name__)


class FolderAttributeMap(ColumnAttributeMap):
    id = 1
    created_by = 2
    modified_by = 3
    creation_date = 4
    last_modified = 5
    last_modified_utc = 6
    folder_id = 20
    title = 300
    module = 301
    type = 302
    subfolders = 304
    own_rights = 305
    permissions = 306
    summary = 307
    standard_folder = 308
    total = 309
    new = 310
    unread = 311
    deleted = 312
    capabilities = 313
    subscribed = 314
    subscr_subflds = 315
    standard_folder_type = 316
    supported_capabilities = 317
    account_id = 318
    folder_name = 319
    com_openexchange_publish_publication_flag = 3010
    com_openexchange_subscribe_subscription_flag = 3020
    com_openexchange_folderstorage_display_name = 3030
    com_openexchange_share_extended_permissions = 3060


class Folder(AppsuiteColumnModel):
    attribute_map_class = FolderAttributeMap
    attribute_types = {
        'id': str,
        'created_by': str,
        'modified_by': str,
        'creation_date': str,
        'last_modified': str,
        'last_modified_utc': str,
        'folder_id': str,
        'title': str,
        'module': str,
        'type': int,
        'subfolders': bool,
        'own_rights': str,
        'permissions': List[FolderPermission],
        'summary': str,
        'standard_folder': bool,
        'total': int,
        'new': int,
        'unread': int,
        'deleted': int,
        'capabilities': int,
        'subscribed': bool,
        'subscr_subflds': bool,
        'standard_folder_type': int,
        'supported_capabilities': List[str],
        'account_id': str,
        'folder_name': str,
        'com_openexchange_publish_publication_flag': bool,
        'com_openexchange_subscribe_subscription_flag': bool,
        'com_openexchange_folderstorage_display_name': str,
        'com_openexchange_share_extended_permissions': List[FolderExtendedPermission]
    }

    def __init__(self, id=None, created_by=None, modified_by=None, creation_date=None, last_modified=None,
                 last_modified_utc=None, folder_id=None, title=None, module=None, type=None, subfolders=None,
                 own_rights=None, permissions=None, summary=None, standard_folder=None, total=None, new=None,
                 unread=None, deleted=None, capabilities=None, subscribed=None, subscr_subflds=None,
                 standard_folder_type=None, supported_capabilities=None, account_id=None, folder_name=None,
                 com_openexchange_publish_publication_flag=None, com_openexchange_subscribe_subscription_flag=None,
                 com_openexchange_folderstorage_display_name=None,
                 com_openexchange_share_extended_permissions=None):
        self._id = None
        self._created_by = None
        self._modified_by = None
        self._creation_date = None
        self._last_modified = None
        self._last_modified_utc = None
        self._folder_id = None
        self._title = None
        self._module = None
        self._type = None
        self._subfolders = None
        self._own_rights = None
        self._permissions = None
        self._summary = None
        self._standard_folder = None
        self._total = None
        self._new = None
        self._unread = None
        self._deleted = None
        self._capabilities = None
        self._subscribed = None
        self._subscr_subflds = None
        self._standard_folder_type = None
        self._supported_capabilities = None
        self._account_id = None
        self._folder_name = None
        self._com_openexchange_publish_publication_flag = None
        self._com_openexchange_subscribe_subscription_flag = None
        self._com_openexchange_folderstorage_display_name = None
        self._com_openexchange_share_extended_permissions = None

        if id is not None:
            self._id = id
        if created_by is not None:
            self._created_by = created_by
        if modified_by is not None:
            self._modified_by = modified_by
        if creation_date is not None:
            self._creation_date = creation_date
        if last_modified is not None:
            self._last_modified = last_modified
        if last_modified_utc is not None:
            self._last_modified_utc = last_modified_utc
        if folder_id is not None:
            self._folder_id = folder_id
        if title is not None:
            self._title = title
        if module is not None:
            self._module = module
        if type is not None:
            self._type = type
        if subfolders is not None:
            self._subfolders = subfolders
        if own_rights is not None:
            self._own_rights = own_rights
        if permissions is not None:
            self._permissions = permissions
        if summary is not None:
            self._summary = summary
        if standard_folder is not None:
            self._standard_folder = standard_folder
        if total is not None:
            self._total = total
        if new is not None:
            self._new = new
        if unread is not None:
            self._unread = unread
        if deleted is not None:
            self._deleted = deleted
        if capabilities is not None:
            self._capabilities = capabilities
        if subscribed is not None:
            self._subscribed = subscribed
        if subscr_subflds is not None:
            self._subscr_subflds = subscr_subflds
        if standard_folder_type is not None:
            self._standard_folder_type = standard_folder_type
        if supported_capabilities is not None:
            self._supported_capabilities = supported_capabilities
        if account_id is not None:
            self._account_id = account_id
        if folder_name is not None:
            self._folder_name = folder_name
        if com_openexchange_publish_publication_flag is not None:
            self._com_openexchange_publish_publication_flag = com_openexchange_publish_publication_flag
        if com_openexchange_subscribe_subscription_flag is not None:
            self._com_openexchange_subscribe_subscription_flag = com_openexchange_subscribe_subscription_flag
        if com_openexchange_folderstorage_display_name is not None:
            self._com_openexchange_folderstorage_display_name = com_openexchange_folderstorage_display_name
        if com_openexchange_share_extended_permissions is not None:
            self._com_openexchange_share_extended_permissions = com_openexchange_share_extended_permissions

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def created_by(self):
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        self._created_by = created_by

    @property
    def modified_by(self):
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        self._modified_by = modified_by

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        self._creation_date = creation_date

    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        self._last_modified = last_modified

    @property
    def last_modified_utc(self):
        return self._last_modified_utc

    @last_modified_utc.setter
    def last_modified_utc(self, last_modified_utc):
        self._last_modified_utc = last_modified_utc

    @property
    def folder_id(self):
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        self._folder_id = folder_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def module(self):
        return self._module

    @module.setter
    def module(self, module):
        self._module = module

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def subfolders(self):
        return self._subfolders

    @subfolders.setter
    def subfolders(self, subfolders):
        self._subfolders = subfolders

    @property
    def own_rights(self):
        return self._own_rights

    @own_rights.setter
    def own_rights(self, own_rights):
        self._own_rights = own_rights

    @property
    def permissions(self):
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        self._permissions = permissions

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, summary):
        self._summary = summary

    @property
    def standard_folder(self):
        return self._standard_folder

    @standard_folder.setter
    def standard_folder(self, standard_folder):
        self._standard_folder = standard_folder

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def new(self):
        return self._new

    @new.setter
    def new(self, new):
        self._new = new

    @property
    def unread(self):
        return self._unread

    @unread.setter
    def unread(self, unread):
        self._unread = unread

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted

    @property
    def capabilities(self):
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        self._capabilities = capabilities

    @property
    def subscribed(self):
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        self._subscribed = subscribed

    @property
    def subscr_subflds(self):
        return self._subscr_subflds

    @subscr_subflds.setter
    def subscr_subflds(self, subscr_subflds):
        self._subscr_subflds = subscr_subflds

    @property
    def standard_folder_type(self):
        return self._standard_folder_type

    @standard_folder_type.setter
    def standard_folder_type(self, standard_folder_type):
        self._standard_folder_type = standard_folder_type

    @property
    def supported_capabilities(self):
        return self._supported_capabilities

    @supported_capabilities.setter
    def supported_capabilities(self, supported_capabilities):
        self._supported_capabilities = supported_capabilities

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def folder_name(self):
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        self._folder_name = folder_name

    @property
    def com_openexchange_publish_publication_flag(self):
        return self._com_openexchange_publish_publication_flag

    @com_openexchange_publish_publication_flag.setter
    def com_openexchange_publish_publication_flag(self, com_openexchange_publish_publication_flag):
        self._com_openexchange_publish_publication_flag = com_openexchange_publish_publication_flag

    @property
    def com_openexchange_subscribe_subscription_flag(self):
        return self._com_openexchange_subscribe_subscription_flag

    @com_openexchange_subscribe_subscription_flag.setter
    def com_openexchange_subscribe_subscription_flag(self, com_openexchange_subscribe_subscription_flag):
        self._com_openexchange_subscribe_subscription_flag = com_openexchange_subscribe_subscription_flag

    @property
    def com_openexchange_folderstorage_display_name(self):
        return self._com_openexchange_folderstorage_display_name

    @com_openexchange_folderstorage_display_name.setter
    def com_openexchange_folderstorage_display_name(self, com_openexchange_folderstorage_display_name):
        self._com_openexchange_folderstorage_display_name = com_openexchange_folderstorage_display_name

    @property
    def com_openexchange_share_extended_permissions(self):
        return self._com_openexchange_share_extended_permissions

    @com_openexchange_share_extended_permissions.setter
    def com_openexchange_share_extended_permissions(self, com_openexchange_share_extended_permissions):
        self._com_openexchange_share_extended_permissions = com_openexchange_share_extended_permissions
