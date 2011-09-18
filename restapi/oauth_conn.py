# Copyright 2011 Max Z. Chao
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import oauth2 as oauth
import re

from error import RestAPIError

class OAuthConn(object):
    def __init__(self, consumer_key, consumer_secret, token_key=None, token_secret=None):
        self._consumer = oauth.Consumer(consumer_key, consumer_secret)
        if token_key and token_secret:
            self._token_key = token_key
            self._token_secret = token_secret
            token = oauth.Token(token_key, token_secret)
            self._client = oauth.Client(self._consumer, token)
        else:
            self._client = oauth.Client(self._consumer)

    def update(self, token_key, token_secret):
        token = oauth.Token(token_key, token_secret)
        self._token_key = token_key
        self._token_secret = token_secret
        self._client = oauth.Client(self._consumer, token)
        return self

    @property
    def token_key(self):
        return self._token_key

    @property
    def token_secret(self):
        return self._token_secret

    def request(self, url, method):
        return self._client.request(url, method)

class OAuthOOB(object):
    def __init__(self, request_token_url, authenticate_url, access_token_url):
        self._request_token_url = request_token_url
        self._authenticate_url = authenticate_url
        self._access_token_url = access_token_url

    def _parse_token(self, content):
        return re.findall('oauth_token=([^&]+)&oauth_token_secret=([^&]+)', content)[0]

    def get_temp_credentials(self, oauth_conn):
        resp, content = oauth_conn.request(self._request_token_url, method = 'GET')
        if resp.status != 200:
            raise RestAPIError('Failed to get Temp Credentials: ' + str(resp.status) + ' ' + resp.reason)
        self._temp_credentials_url = self._authenticate_url + '?' + content
        
        token_key, token_secret = self._parse_token(content)
        return oauth_conn.update(token_key, token_secret)

    @property
    def temp_credentials_url(self):
        return self._temp_credentials_url

    def get_credentials(self, oauth_conn, pin_code):
        access_token_pin_code_url = self._access_token_url + '?oauth_verifier=' + pin_code
        resp, content = oauth_conn.request(access_token_pin_code_url, method = 'GET')
        if resp.status != 200:
            raise RestAPIError('Failed to get Credentials: ' + str(resp.status) + ' ' + resp.reason)
        
        token_key, token_secret = self._parse_token(content)
        return oauth_conn.update(token_key, token_secret)
