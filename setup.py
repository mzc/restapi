#!/usr/bin/env python

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

import sys
import os
import codecs

from setuptools import setup, find_packages

import restapi

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name             = 'restapi'           ,
    version          = restapi.__version__ ,
    author           = restapi.__author__  ,
    author_email     = restapi.__contact__ ,
    description      = restapi.__doc__     ,
    license          = 'APACHE'            ,
    keywords         = 'twitter restapi'   ,
    url              = restapi.__homepage__,
    packages         = ['restapi']         ,
    long_description = read('README')      ,
)
