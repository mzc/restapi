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

try:
    import simplejson as json
except ImportError:
    import json
import string

import twitter_api
from request import Request
from error import RestAPIError

class _sub_func(object):
    def __init__(self, service, service_name, sub):
        self._service = service
        self._service_name = service_name
        self._sub = sub

    def __getattr__(self, method_name):
        def helper(conn, **args):
            service_name_cap = string.capitalize(self._service_name)
            sub_name_cap = string.capitalize(self._sub)

            try:
                url, method = self._service.__dict__[self._sub + '_' + method_name](**args)
            except KeyError:
                raise RestAPIError('%s: Failed to find method:\'%s\' of \'%s\'' % (service_name_cap, method_name, sub_name_cap))
            except RestAPIError as err:
                raise RestAPIError(service_name_cap + ': ' + str(err) + ' in method:\'%s\' of \'%s\'' % (method_name, sub_name_cap))

            resp, content = conn.request(url, method)
            if resp.status != 200:
                raise RestAPIError(url + ': ' + str(resp.status) + ' ' + resp.reason)
            try:
                return json.loads(content)
            except Exception:
                raise RestAPIError(service_name_cap + ': Failed to get Json object in method:\'%s\' of \'%s\'' % (method_name, sub_name_cap))
        return helper

class Client(object):
    def __init__(self, service_name):
        self._service_name = service_name
        if self._service_name == 'twitter':
            self.service = Request(twitter_api.api_list)

    def __getattr__(self, sub):
        def helper():
            return _sub_func(self.service, self._service_name, sub)
        return helper
