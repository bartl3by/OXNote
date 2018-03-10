#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from typing import List

from appsuite_api_wrapper.exceptions import RequestParameterException
from appsuite_api_wrapper.models.capability import Capability
from appsuite_api_wrapper.session import HttpApiSession

logger = logging.getLogger(__name__)

_api_path_capabilities = 'capabilities'

_api_action_all = 'all'
_api_action_get = 'get'


class Capabilities(HttpApiSession):

    def action_all(self, session_id: str) -> List[Capability]:
        response = self.authenticated_get(_api_path_capabilities,
                                          _api_action_all,
                                          session_id)

        data = response.json(encoding='utf-8')
        if 'data' in data:
            return [Capability.from_api_response(capability) for capability in data['data']]

    def action_get(self, id: str, session_id: str) -> Capability:
        if not id or len(id.strip()) <= 0:
            raise RequestParameterException('Empty id')

        request_parameters = {
            'id': id
        }

        response = self.authenticated_get(_api_path_capabilities,
                                          _api_action_get,
                                          session_id,
                                          params=request_parameters)

        data = response.json(encoding='utf-8')
        if 'data' in data:
            return Capability.from_api_response(data['data'])
