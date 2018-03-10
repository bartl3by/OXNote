#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from appsuite_api_wrapper.models.appsuite_id_model import AppsuiteIdModel, IdAttributeMap
from appsuite_api_wrapper.models.drive_object_version import DriveObjectVersion
from appsuite_api_wrapper.models.drive_sync_error_data import DriveSyncErrorData

logger = logging.getLogger(__name__)


class DriveActionAttributeMap(IdAttributeMap):
    action = 'action'
    version = 'version'
    new_version = 'newVersion'
    path = 'path'
    offset = 'offset'
    total_length = 'totalLength'
    content_type = 'contentType'
    created = 'created'
    modified = 'modified'
    error = 'error'
    quarantine = 'quarantine'
    reset = 'reset'
    stop = 'stop'
    acknowledge = 'acknowledge'
    thumbnail_link = 'thumbnailLink'
    preview_link = 'previewLink'
    direct_link = 'directLink'
    direct_link_fragments = 'directLinkFragments'


class DriveAction(AppsuiteIdModel):
    attribute_map_class = DriveActionAttributeMap
    attribute_types = {
        'action': str,
        'version': DriveObjectVersion,
        'new_version': DriveObjectVersion,
        'path': str,
        'offset': int,
        'total_length': int,
        'content_type': str,
        'created': int,
        'modified': int,
        'error': DriveSyncErrorData,
        'quarantine': bool,
        'reset': bool,
        'stop': bool,
        'acknowledge': bool,
        'thumbnail_link': str,
        'preview_link': str,
        'direct_link': str,
        'direct_link_fragments': str
    }

    def __init__(self, action=None, version=None, new_version=None, path=None, offset=None, total_length=None,
                 content_type=None, created=None, modified=None, error=None, quarantine=None, reset=None, stop=None,
                 acknowledge=None, thumbnail_link=None, preview_link=None, direct_link=None,
                 direct_link_fragments=None):
        self._action = None
        self._version = None
        self._new_version = None
        self._path = None
        self._offset = None
        self._total_length = None
        self._content_type = None
        self._created = None
        self._modified = None
        self._error = None
        self._quarantine = None
        self._reset = None
        self._stop = None
        self._acknowledge = None
        self._thumbnail_link = None
        self._preview_link = None
        self._direct_link = None
        self._direct_link_fragments = None

        if action is not None:
            self._action = action
        if version is not None:
            self._version = version
        if new_version is not None:
            self._new_version = new_version
        if path is not None:
            self._path = path
        if offset is not None:
            self._offset = offset
        if total_length is not None:
            self._total_length = total_length
        if content_type is not None:
            self._content_type = content_type
        if created is not None:
            self._created = created
        if modified is not None:
            self._modified = modified
        if error is not None:
            self._error = error
        if quarantine is not None:
            self._quarantine = quarantine
        if reset is not None:
            self._reset = reset
        if stop is not None:
            self._stop = stop
        if acknowledge is not None:
            self._acknowledge = acknowledge
        if thumbnail_link is not None:
            self._thumbnail_link = thumbnail_link
        if preview_link is not None:
            self._preview_link = preview_link
        if direct_link is not None:
            self._direct_link = direct_link
        if direct_link_fragments is not None:
            self._direct_link_fragments = direct_link_fragments

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def new_version(self):
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        self._new_version = new_version

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, offset):
        self._offset = offset

    @property
    def total_length(self):
        return self._total_length

    @total_length.setter
    def total_length(self, total_length):
        self._total_length = total_length

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        self._content_type = content_type

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, created):
        self._created = created

    @property
    def modified(self):
        return self._modified

    @modified.setter
    def modified(self, modified):
        self._modified = modified

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error):
        self._error = error

    @property
    def quarantine(self):
        return self._quarantine

    @quarantine.setter
    def quarantine(self, quarantine):
        self._quarantine = quarantine

    @property
    def reset(self):
        return self._reset

    @reset.setter
    def reset(self, reset):
        self._reset = reset

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, stop):
        self._stop = stop

    @property
    def acknowledge(self):
        return self._acknowledge

    @acknowledge.setter
    def acknowledge(self, acknowledge):
        self._acknowledge = acknowledge

    @property
    def thumbnail_link(self):
        return self._thumbnail_link

    @thumbnail_link.setter
    def thumbnail_link(self, thumbnail_link):
        self._thumbnail_link = thumbnail_link

    @property
    def preview_link(self):
        return self._preview_link

    @preview_link.setter
    def preview_link(self, preview_link):
        self._preview_link = preview_link

    @property
    def direct_link(self):
        return self._direct_link

    @direct_link.setter
    def direct_link(self, direct_link):
        self._direct_link = direct_link

    @property
    def direct_link_fragments(self):
        return self._direct_link_fragments

    @direct_link_fragments.setter
    def direct_link_fragments(self, direct_link_fragments):
        self._direct_link_fragments = direct_link_fragments
