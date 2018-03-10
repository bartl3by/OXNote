#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from typing import Tuple

from requests import Response, get, post, put

from appsuite_api_wrapper.exceptions import ApiException

logger = logging.getLogger(__name__)


class ApiClient(object):

    def _request(self, method,
                 scheme: str,
                 host: str,
                 api_uri: str,
                 module_path: str,
                 action: str,
                 **kwargs) -> Response:

        response = method('{}{}{}{}{}{}{}'.format(scheme, '://', host, api_uri, module_path, '?action=', action), **kwargs)

        status, message = self.verify_response(response)
        if status:
            return response
        else:
            response.close()
            raise ApiException(message)

    def get(self, *args, **kwargs) -> Response:
        return self._request(get, *args, **kwargs)

    def post(self, *args, **kwargs) -> Response:
        return self._request(post, *args, **kwargs)

    def put(self, *args, **kwargs) -> Response:
        return self._request(put, *args, **kwargs)

    def verify_response(self, response: Response) -> Tuple[bool, str(None)]:
        if not response.status_code == 200:
            return False, 'HTTP status: ' + str(response.status_code)
        if not response.status_code:
            return False, 'Empty response status code from server'
        if not response:
            return False, 'Empty response'

        if 'content-type' in response.headers and response.headers.get('content-type').startswith(
                'application/octet-stream'):
            return True, None

        response_content = response.content.decode('utf-8')
        if response.content.decode('utf-8').strip().startswith('{'):
            response_content = response.json(encoding='utf-8')

        if 'error' in response_content:
            logger.error('HTTP API error, code: ' + response_content.get('code') + response_content.get(
                    'error_id') + ' - ' + response_content.get('error_desc'))
            return False, response_content.get('error')

        return True, None
