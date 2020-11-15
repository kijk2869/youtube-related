# -*- coding: utf-8 -*-
"""
Youtube Related Video Fetcher
"""

__title__ = "youtube_related"
__author__ = "kijk2869"
__lisence__ = "MIT"
__version__ = "1.0.0"

from collections import namedtuple

from .client import async_get, get, preventDuplication
from .error import *

VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")

version_info = VersionInfo(major=0, minor=0, micro=4, releaselevel="final", serial=0)
