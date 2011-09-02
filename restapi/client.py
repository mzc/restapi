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

import twitter_api
from request import Request
try:
    import simplejson as json
except ImportError:
    import json

class _sub_func(object):
    def __init__(self, twitter, sub):
        self._twitter = twitter
        self._sub = sub

    def __getattr__(self, name):
        def helper(conn, **args):
            url, method = self._twitter.__dict__[self._sub + '_' + name](**args)
            response, content = conn.request(url, method)
            return json.loads(content)
        return helper

class Twitter(Request):
    def __init__(self):
        super(Twitter, self).__init__(twitter_api.api_list)
    
    def __getattr__(self, name):
        def helper():
            return _sub_func(self, name)
        return helper
