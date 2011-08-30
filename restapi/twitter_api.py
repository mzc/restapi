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

BASE_URL     = 'https://api.twitter.com/1/'
STATUSES_URL = BASE_URL + 'statuses/'
SEARCH_URL   = 'http://search.twitter.com/search.json'

api_list = [
    # Timelines
    (
        # api             method url_format
        'home_timeline', 'GET', STATUSES_URL + 'home_timeline.json',
        # params
        {
            'count'                 : lambda x: params_range(x, 1, 200),
            'since_id'              : lambda x: params_isdigit(x)      ,
            'max_id'                : lambda x: params_isdigit(x)      ,
            'page'                  : lambda x: params_isdigit(x)      ,
            'trim_user'             : lambda x: params_isbool(x)       ,
            'include_rts'           : lambda x: params_isbool(x)       ,
            'include_entities'      : lambda x: params_isbool(x)       ,
            'exclude_replies'       : lambda x: params_isbool(x)       ,
            'contributor_details'   : lambda x: params_isbool(x)       ,
        },
        # required
        [],
    ),
    (
        'mentions', 'GET', STATUSES_URL + 'mentions.json',
        {
            'count'                 : lambda x: params_range(x, 1, 200),
            'since_id'              : lambda x: params_isdigit(x)      ,
            'max_id'                : lambda x: params_isdigit(x)      ,
            'page'                  : lambda x: params_isdigit(x)      ,
            'trim_user'             : lambda x: params_isbool(x)       ,
            'include_rts'           : lambda x: params_isbool(x)       ,
            'include_entities'      : lambda x: params_isbool(x)       ,
            'contributor_details'   : lambda x: params_isbool(x)       ,
        },
        [],
    ),
    (
        'public_timeline', 'GET', STATUSES_URL + 'public_timeline.json',
        {
            'trim_user'             : lambda x: params_isbool(x)       ,
            'include_entities'      : lambda x: params_isbool(x)       ,
        },
        [],
    ),
    (
        'retweeted_by_me', 'GET', STATUSES_URL + 'retweeted_by_me.json',
        {
            'count'                 : lambda x: params_range(x, 1, 100),
            'since_id'              : lambda x: params_isdigit(x)      ,
            'max_id'                : lambda x: params_isdigit(x)      ,
            'page'                  : lambda x: params_isdigit(x)      ,
            'trim_user'             : lambda x: params_isbool(x)       ,
            'include_entities'      : lambda x: params_isbool(x)       ,
        },
        [],
    ),
    (
        'retweeted_to_me', 'GET', STATUSES_URL + 'retweeted_to_me.json',
        {
            'count'                 : lambda x: params_range(x, 1, 100),
            'since_id'              : lambda x: params_isdigit(x)      ,
            'max_id'                : lambda x: params_isdigit(x)      ,
            'page'                  : lambda x: params_isdigit(x)      ,
            'trim_user'             : lambda x: params_isbool(x)       ,
            'include_entities'      : lambda x: params_isbool(x)       ,
        },
        [],
    ),
    (
        'retweeted_of_me', 'GET', STATUSES_URL + 'retweeted_of_me.json',
        {
            'count'                 : lambda x: params_range(x, 1, 100),
            'since_id'              : lambda x: params_isdigit(x)      ,
            'max_id'                : lambda x: params_isdigit(x)      ,
            'page'                  : lambda x: params_isdigit(x)      ,
            'trim_user'             : lambda x: params_isbool(x)       ,
            'include_entities'      : lambda x: params_isbool(x)       ,
        },
        [],
    ),
    (
        'user_timeline', 'GET', STATUSES_URL + 'user_timeline.json',
        {
            'user_id'               : lambda x: params_isdigit(x)      ,
            'screen_name'           : lambda x: params_isstring(x)     ,
            'since_id'              : lambda x: params_isdigit(x)      ,
            'count'                 : lambda x: params_range(x, 1, 200),
            'max_id'                : lambda x: params_isdigit(x)      ,
            'page'                  : lambda x: params_isdigit(x)      ,
            'trim_user'             : lambda x: params_isbool(x)       ,
            'include_rts'           : lambda x: params_isbool(x)       ,
            'include_entities'      : lambda x: params_isbool(x)       ,
            'exclude_replies'       : lambda x: params_isbool(x)       ,
            'contributor_details'   : lambda x: params_isbool(x)       ,
        },
        [],
    ),
    (
        'retweeted_to_user', 'GET', STATUSES_URL + 'retweeted_to_user.json',
        {
            'screen_name'           : lambda x: params_isstring(x)      ,
            'id'                    : lambda x: params_isdigit_string(x),
            'count'                 : lambda x: params_range(x, 1, 100) ,
            'since_id'              : lambda x: params_isdigit(x)       ,
            'max_id'                : lambda x: params_isdigit(x)       ,
            'page'                  : lambda x: params_isdigit(x)       ,
            'trim_user'             : lambda x: params_isbool(x)        ,
            'include_entities'      : lambda x: params_isbool(x)        ,
        },
        [],
    ),
    (
        'retweeted_by_user', 'GET', STATUSES_URL + 'retweeted_by_user.json',
        {
            'screen_name'           : lambda x: params_isstring(x)      ,
            'id'                    : lambda x: params_isdigit_string(x),
            'count'                 : lambda x: params_range(x, 1, 100) ,
            'since_id'              : lambda x: params_isdigit(x)       ,
            'max_id'                : lambda x: params_isdigit(x)       ,
            'page'                  : lambda x: params_isdigit(x)       ,
            'trim_user'             : lambda x: params_isbool(x)        ,
            'include_entities'      : lambda x: params_isbool(x)        ,
        },
        [],
    ),
    
    # Tweets
    (
        'retweeted_by', 'GET', STATUSES_URL + '%(id)s/retweeted_by.json',
        {
            'id'                    : lambda x: params_isdigit(x)      ,
            'count'                 : lambda x: params_range(x, 1, 100),
            'page'                  : lambda x: params_isdigit(x)      ,
        },
        ['id'],
    ),
    (
        'retweeted_by_ids', 'GET', STATUSES_URL + '%(id)s/retweeted_by/ids.json',
        {
            'id'                    : lambda x: params_isdigit(x)      ,
            'count'                 : lambda x: params_range(x, 1, 100),
            'page'                  : lambda x: params_isdigit(x)      ,
            'stringify_ids'         : lambda x: params_isbool(x)       ,
        },
        ['id'],
    ),
    (
        'retweets', 'GET', STATUSES_URL + 'retweets/%(id)s.json',
        {
            'id'                    : lambda x: params_isdigit(x)      ,
            'count'                 : lambda x: params_range(x, 1, 100),
            'trim_user'             : lambda x: params_isbool(x)       ,
            'include_entities'      : lambda x: params_isbool(x)       ,
        },
        ['id'],
    ),
    (
        'show', 'GET', STATUSES_URL + 'show/%(id)s.json',
        {
            'id'                    : lambda x: params_isdigit(x)      ,
            'trim_user'             : lambda x: params_isbool(x)       ,
            'include_entities'      : lambda x: params_isbool(x)       ,
        },
        ['id'],
    ),
    (
        'destroy', 'POST', STATUSES_URL + 'destroy/%(id)s.json',
        {
            'id'                    : lambda x: params_isdigit(x)      ,
            'include_entities'      : lambda x: params_isbool(x)       ,
            'trim_user'             : lambda x: params_isbool(x)       ,
        },
        ['id'],
    ),
    (
        'retweet', 'POST', STATUSES_URL + 'retweet/%(id)s.json',
        {
            'id'                    : lambda x: params_isdigit(x)      ,
            'include_entities'      : lambda x: params_isbool(x)       ,
            'trim_user'             : lambda x: params_isbool(x)       ,
        },
        ['id'],
    ),
    (
        'update', 'POST', STATUSES_URL + 'update.json',
        {
            'status'                : lambda x: params_istext(x)      ,
            'in_reply_to_status_id' : lambda x: params_isdigit(x)     ,
            'lat'                   : lambda x: params_islatitude(x)  ,
            'long'                  : lambda x: params_islongtitude(x),
            'place_id'              : lambda x: params_isdigit(x)     ,
            'display_coordinates'   : lambda x: params_isbool(x)      ,
            'trim_user'             : lambda x: params_isbool(x)      ,
            'include_entities'      : lambda x: params_isbool(x)      ,
            'wrap_links'            : lambda x: params_isbool(x)      ,
        },
        ['status'],
    ),
    (
        'update_with_media', 'POST', STATUSES_URL + 'update_with_media.json',
        {
            'status'                : lambda x: params_istext(x)      ,
#            'media'
            'possibly_sensitive'    : lambda x: params_isbool(x)      ,
            'in_reply_to_status_id' : lambda x: params_isstring(x)    ,
            'lat'                   : lambda x: params_islatitude(x)  ,
            'long'                  : lambda x: params_islongtitude(x),
            'place_id'              : lambda x: params_isdigit(x)     ,
            'display_coordinates'   : lambda x: params_isbool(x)      ,
        },
        ['status'],
    ),

    # Search
    (
        'search', 'GET', SEARCH_URL,
        {
            'q'                     : lambda x      : params_isstring(x)        ,
            'callback'              : lambda x      : params_isstring(x)        ,
            'geocode'               : lambda x, y, z: params_islocation(x, y, z),
            'lang'                  : lambda x      : params_isstring(x)        ,
            'locale'                : lambda x      : params_isstring(x)        ,
            'page'                  : lambda x      : params_isrange(x, 1, 1500),
            'result_type'           : lambda x      : params_istype(x)          ,
            'rpp'                   : lambda x      : params_isrange(x, 1, 100) ,
            'show_user'             : lambda x      : params_isbool(x)          ,
            'until'                 : lambda x      : params_isdata(x)          ,
            'since_id'              : lambda x      : params_isdigit(x)         ,
        },
        ['q'],
    ),
]

import re

def params_range(x, low, high):
    return x >= low and x <= high

def params_isdigit(x):
    return type(x) == type(1) or type(x) == type(1L)

def params_islatitude(x):
    return type(x) == type(1.1) and x >= -90.0 and x <= 90.0

def params_islongtitude(x):
    return type(x) == type(1.1) and x >= -180.0 and x <= 180.0

def params_isradius(x):
    unit = x[-2:]
    num  = x[:-2]
    return (unit == 'mi' or unix == 'km') and params_isdigit(num)

def params_isstring(x):
    return type(x) == type(' ')

def params_isdigit_string(x):
    return params_isdigit(x) or params_isstring(x)

def params_istext(x):
    return params_isstring(x) and len(x) <= 140

def params_isbool(x):
    return x == 'true' or x == 't' or x == 1 or x == 'false'

def params_istype(x):
    return x == 'mixed' or x == 'recent' or x == 'popular'

def params_isdata(x):
    [(y, m, d)] = re.findall('(....)-(..)-(..)', x)
    return params_range(y, 1970, 3000) and params_range(m, 1, 12) and params_range(d, 1, 31)

def params_islocation(x, y, z):
    return params_islatitude(x) and params_islongtitude(y) and params_israidus(z)
