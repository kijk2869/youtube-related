# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup

version = ""
with open("youtube_related/__init__.py", encoding="UTF8") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

requirements = []
with open(f"{path}/requirements.txt", encoding="UTF8") as f:
    requirements = f.read().splitlines()

if not version:
    raise RuntimeError("version is not defined")

readme = ""
with open(f"{path}/README.rst", encoding="UTF8") as f:
    readme = f.read()

setup(
    name="youtube-related",
    author="kijk2869",
    url="https://github.com/kijk2869/youtube-related",
    project_urls={
        "Homepage": "https://youtube.com/",
        "Source": "https://github.com/kijk2869/youtube-related",
        "Tracker": "https://github.com/kijk2869/youtube-related/issues",
    },
    version=version,
    packages=["youtube_related"],
    license="MIT",
    description="Youtube Related Video Fetcher",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
