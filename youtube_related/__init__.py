#-*- coding: utf-8 -*-
"""
Youtube Related Video Fetcher
"""

__title__ = 'youtube_related'
__author__ = 'kijk2869'
__lisence__ = 'MIT'
__version__ = '0.0.1'

from collections import namedtuple

from .client import get, async_get, preventDuplication
from .fetcher import fetch, async_fetch
from .parser import loadInitialData, parse

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel='final', serial=0)