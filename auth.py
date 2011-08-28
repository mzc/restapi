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

class OAuth_Single(object):
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        consumer = oauth.Consumer(consumer_key, consumer_secret)
        token = oauth.Token(token_key, token_secret)
        self.client = oauth.Client(consumer, token)
        
    def request(self, url, method):
        return self.client.request(url, method)
