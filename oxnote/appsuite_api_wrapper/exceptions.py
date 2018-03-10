#!/usr/bin/python3
# -*- coding: utf-8 -*-


class ApiException(Exception):
    pass


class RequestParameterException(ApiException):
    pass


class SessionException(ApiException):
    pass


class NoActiveSessionException(SessionException):
    pass


class SessionLoginException(SessionException):
    pass


class SessionLogoutException(SessionException):
    pass


class MissingSessionTokenException(SessionException):
    pass


class FolderException(ApiException):
    pass


class DefaultFolderException(FolderException):
    pass


class OXNoteFolderException(FolderException):
    pass


class PermissionException(ApiException):
    pass


class DriveException(ApiException):
    pass
