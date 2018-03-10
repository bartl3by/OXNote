#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from typing import Dict

from requests import Response, get, post, put

from appsuite_api_wrapper.api_client import ApiClient
from appsuite_api_wrapper.exceptions import (ApiException,
                                             MissingSessionTokenException,
                                             SessionLoginException,
                                             SessionLogoutException)

logger = logging.getLogger(__name__)

_api_path_login = 'login'
_api_action_login = 'login'
_api_action_logout = 'logout'


def _verify_session_token(*outer_args, **outer_kwargs):
    def decorator(f):
        def decorated(self, *args, **kwargs):
            if 'session_id' in kwargs and not kwargs['session_id'] in self.sessions:
                raise MissingSessionTokenException()
            return f(self, *args, **kwargs)

        return decorated

    return decorator


class HttpApiSession(ApiClient):
    sessions = dict()

    def __exit__(self, *args, **kwargs):
        logger.info('Closing all sessions on class exit')
        self.logout()

    @_verify_session_token()
    def __authenticated_request(self,
                                method,
                                module_path: str,
                                action: str,
                                session_id: str,
                                **kwargs) -> Response:

        if 'params' in kwargs:
            kwargs['params']['session'] = self.sessions[session_id].session_id
        else:
            kwargs['params'] = { 'session': self.sessions[session_id].session_id }

        kwargs['headers'] = self.sessions[session_id].session_headers
        kwargs['cookies'] = self.sessions[session_id].session_cookies

        return super(HttpApiSession, self)._request(method,
                                                    self.sessions[session_id].scheme,
                                                    self.sessions[session_id].host,
                                                    self.sessions[session_id].api_uri,
                                                    module_path,
                                                    action,
                                                    **kwargs)

    def login(self, scheme: str, host: str, api_uri: str, username: str, password: str) -> str:
        """
        ..todo:: Implement long term session handling
        """
        logger.info('Initiating session for user {} on {}'.format(username, host))

        request_data = {
            'name': username,
            'password': password,
            'client': 'OXNote'
        }

        try:
            response = self.post(scheme,
                                 host,
                                 api_uri,
                                 _api_path_login,
                                 _api_action_login,
                                 data=request_data)
            response_content = response.json(encoding='utf-8')

            session = Session(scheme, host, api_uri, username, password, response_content.get('session'),
                              response.cookies, response.headers)
            response.close()

            self.sessions[session.session_id] = session

            return session.session_id
        except ApiException as e:
            raise SessionLoginException(e) from e

    @_verify_session_token()
    def logout(self, session_id: str = None, delete_reference_on_exception: bool = True):
        for current_session_id in [session_id] if session_id else list(self.sessions.keys()):
            request_parameters = { 'session': self.sessions[current_session_id].session_id }

            try:
                logger.info(
                        'Closing session {} for user {} on host {}'.format(self.sessions[current_session_id].session_id,
                                                                           self.sessions[current_session_id].username,
                                                                           self.sessions[current_session_id].host))

                response = self.get(self.sessions[current_session_id].scheme,
                                    self.sessions[current_session_id].host,
                                    self.sessions[current_session_id].api_uri,
                                    _api_path_login,
                                    _api_action_logout,
                                    params=request_parameters,
                                    headers=self.sessions[current_session_id].session_headers,
                                    cookies=self.sessions[current_session_id].session_cookies)
                response.close()
                del self.sessions[current_session_id]
            except ApiException as e:
                raise SessionLogoutException(e) from e
            finally:
                if delete_reference_on_exception and current_session_id in self.sessions:
                    del self.sessions[current_session_id]

    @_verify_session_token()
    def refresh_secret_cookie(self):
        """
        ..todo:: Implement cookie refresh
        """
        return

    def authenticated_get(self, *args, **kwargs) -> Response:
        return self.__authenticated_request(get, *args, **kwargs)

    def authenticated_post(self, *args, **kwargs) -> Response:
        return self.__authenticated_request(post, *args, **kwargs)

    def authenticated_put(self, *args, **kwargs) -> Response:
        return self.__authenticated_request(put, *args, **kwargs)


class Session(object):

    def __init__(self, scheme: str,
                 host: str,
                 api_uri: str,
                 username: str,
                 password: str,
                 session_id: str,
                 session_headers: Dict[str, str],
                 session_cookies: Dict[str, str]):
        self._scheme = scheme
        self._host = host
        self._api_uri = api_uri
        self._username = username
        self._password = password
        self._session_id = session_id
        self._session_headers = session_headers
        self._session_cookies = session_cookies

    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        self._scheme = scheme

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def api_uri(self):
        return self._api_uri

    @api_uri.setter
    def api_uri(self, api_uri):
        self._api_uri = api_uri

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        self._session_id = session_id

    @property
    def session_headers(self):
        return self._session_headers

    @session_headers.setter
    def session_headers(self, session_headers):
        self._session_headers = session_headers

    @property
    def session_cookies(self):
        return self._session_cookies

    @session_cookies.setter
    def session_cookies(self, session_cookies):
        self._session_cookies = session_cookies
