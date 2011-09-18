#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
