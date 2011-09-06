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

import urllib
import re

from error import RestAPIError

class Request(object):
    class _auto_dict(dict):
        def __getitem__(self, key):
            try:
                return dict.__getitem__(self, key)
            except KeyError:
                value = self[key] = type(self)()
            return value

    def __init__(self, api_list):
        # help to pass 'api' into lambda
        def helper(api):
            return lambda **args: self._make_request(api, **args)

        self._apis = self._auto_dict()
        for a in api_list:
            self._apis[a[0]]['method']     = a[1]
            self._apis[a[0]]['url_format'] = a[2]
            self._apis[a[0]]['params']     = a[3]
            self._apis[a[0]]['required']   = a[4]
            object.__setattr__(self, a[0], helper(a[0]))

    def _make_params(self, args, params, required, embeded):
        for key in required:
            if key and key not in args and key not in embeded:
                raise RestAPIError('Missing required param:\'%s\'' % key)
        
        for key in args:
            if key and key not in params:
                raise RestAPIError('Unexcepted params:\'%s\'' % key)
            
            if not params[key](args[key]):
                raise RestAPIError('Params:\'%s\' is out of range' % key)

        return urllib.urlencode(args)

    def _make_request(self, api, **args):
        url_format = self._apis[api]['url_format']
        method     = self._apis[api]['method']
        params     = self._apis[api]['params']
        required   = self._apis[api]['required']

        try:
            url_prefix = url_format % args
        except KeyError:
            raise RestAPIError('Missing required param:\'%s\'' % required)

        embeded    = re.findall('%\(([^\)]+)\)s', url_format)
        for p in embeded:
            del args[p]

        encoded    = self._make_params(args, params, required, embeded)

        if encoded:
            url = url_prefix + '?' + encoded
        else :
            url = url_prefix
        return url, method
