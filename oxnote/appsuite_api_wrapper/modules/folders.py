#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import typing

import simplejson as json

from appsuite_api_wrapper.exceptions import RequestParameterException
from appsuite_api_wrapper.models.folder import Folder, FolderAttributeMap
from appsuite_api_wrapper.session import HttpApiSession

logger = logging.getLogger(__name__)

_api_path_folders = 'folders'

_api_action_all_visible = 'allVisible'
_api_action_clear = 'clear'
_api_action_delete = 'delete'
_api_action_get = 'get'
_api_action_list = 'list'
_api_action_new = 'new'
_api_action_notify = 'notify'
_api_action_path = 'path'
_api_action_root = 'root'
_api_action_shares = 'shares'
_api_action_update = 'update'
_api_action_updates = 'updates'


class Folders(HttpApiSession):

    def action_all_visible(self,
                           content_type: str,
                           session_id: str,
                           tree: str = '0',
                           columns: typing.List[int] = FolderAttributeMap.all_columns()) -> typing.Dict[str, typing.List[Folder]]:
        request_parameters = {
            'tree': tree,
            'content_type': content_type,
            'columns': FolderAttributeMap.generate_columns_string(columns)
        }

        response = self.authenticated_get(_api_path_folders,
                                          _api_action_all_visible,
                                          session_id,
                                          params=request_parameters)

        result = dict()

        data = response.json(encoding='utf-8')
        if 'data' in data:
            result['private'] = [Folder.from_api_response(item, columns) for item in data['data']['private']] if 'private' in data['data'] else []
            result['public'] = [Folder.from_api_response(item, columns) for item in data['data']['public']] if 'public' in data['data'] else []
            result['shared'] = [Folder.from_api_response(item, columns) for item in data['data']['shared']] if 'shared' in data['data'] else []

        return result

    def action_clear(self,
                     folders: typing.List[Folder],
                     session_id: str,
                     tree: str = '0',
                     allowed_modules: str = None):
        if not folders or len(folders) <= 0:
            raise RequestParameterException('Empty folder list provided, no folders to clear')

        request_parameters = {
            'tree': tree,
            'allowed_modules': allowed_modules
        }

        folder_list = []
        for folder in folders:
            if folder.id and len(folder.id) > 0:
                folder_list.append(folder.id)

        if len(folder_list) <= 0:
            raise RequestParameterException('No folder model in folder list provided an id, no folders to clear')

        request_data = json.dumps(folder_list)

        self.authenticated_put(_api_path_folders,
                               _api_action_clear,
                               session_id,
                               params=request_parameters,
                               data=request_data)

    def action_delete(self,
                      folders: typing.List[Folder],
                      session_id: str,
                      tree: str = '0',
                      timestamp: int = None,
                      allowed_modules: str = None,
                      hard_delete: bool = False):
        if not folders or len(folders) <= 0:
            raise RequestParameterException('Empty folder list provided, no folders to delete')

        request_parameters = {
            'tree': tree,
            'timestamp': timestamp,
            'allowed_modules': allowed_modules,
            'hardDelete': hard_delete
        }

        folder_list = []
        for folder in folders:
            if folder.id and len(folder.id) > 0:
                folder_list.append(folder.id)

        if len(folder_list) <= 0:
            raise RequestParameterException('No folder model in folder list provided an id, no folders to delete')

        request_data = json.dumps(folder_list)

        self.authenticated_put(_api_path_folders,
                               _api_action_delete,
                               session_id,
                               params=request_parameters,
                               data=request_data)

    def action_list(self,
                    session_id: str,
                    parent: str = '0',
                    columns: typing.List[int] = FolderAttributeMap.all_columns(),
                    all: bool = False,
                    tree: str = '0',
                    allowed_modules: str = None,
                    error_on_duplicate_name: bool = False) -> typing.List[Folder]:
        request_parameters = {
            'parent': parent,
            'columns': FolderAttributeMap.generate_columns_string(columns),
            'all': 1 if all else 0,
            'tree': tree,
            'allowed_modules': allowed_modules,
            'error_on_duplicate_name': error_on_duplicate_name
        }

        response = self.authenticated_get(_api_path_folders,
                                          _api_action_list,
                                          session_id,
                                          params=request_parameters)

        data = response.json(encoding='utf-8')
        if 'data' in data:
            return [Folder.from_api_response(item, columns) for item in data['data']]

    def action_new(self,
                   folder: Folder,
                   folder_id: str,
                   session_id: str,
                   tree: str = '0',
                   allowed_modules: str = None) -> str:
        if not folder_id or len(folder_id.strip()) <= 0:
            raise RequestParameterException('Empty folder id')

        request_parameters = {
            'folder_id': folder_id,
            'tree': tree,
            'allowed_modules': allowed_modules
        }
        request_json = {
            'folder': folder.to_dict()
        }

        response = self.authenticated_put(_api_path_folders,
                                          _api_action_new,
                                          session_id,
                                          params=request_parameters,
                                          json=request_json)

        data = response.json(encoding='utf-8')

        if 'data' in data:
            return data['data']
