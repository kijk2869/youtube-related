youtube-related
=================

.. image:: https://img.shields.io/pypi/v/youtube-related.svg
    :target: https://pypi.org/project/youtube-related/
    :alt: PyPI
.. image:: https://img.shields.io/pypi/pyversions/youtube-related.svg
    :target: https://pypi.org/project/youtube-related/
    :alt: PyPI - Python Version
.. image:: https://img.shields.io/github/license/kijk2869/youtube-related.svg
    :target: https://github.com/kijk2869/youtube-related/
    :alt: GitHub
.. image:: https://img.shields.io/pypi/dm/youtube-related.svg
    :target: https://pypi.org/project/youtube-related/
    :alt: PyPI - Downloads

Youtube Related Video Fetcher

Installation
----------------

.. code:: sh

    python3 -m pip install youtube-related

Example
------------

Basic usage

.. code:: python3

    import youtube_related

    print(youtube_related.fetch('Some Youtube Video URL'))

YouTube's featured video may be repeated regularly, and deque was used to prevent this.

.. code:: python3

    from youtube_related import preventDuplication

    Avoider: preventDuplication = preventDuplication()

    print(Avoider.get('Some Youtube Video URL'))
