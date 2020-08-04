# -*- coding: utf-8 -*-
"""
Youtube Related Video Fetcher
"""

__title__ = "youtube_related"
__author__ = "kijk2869"
__lisence__ = "MIT"
__version__ = "0.0.2"

from collections import namedtuple

from .client import async_get, get, preventDuplication
from .fetcher import async_fetch, fetch
from .parser import loadInitialData, parse

VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")

version_info = VersionInfo(major=0, minor=0, micro=2, releaselevel="final", serial=0)
