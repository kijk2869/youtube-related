youtube-related
=================

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

    print(youtube_related.get('Some Youtube Video URL'))

YouTube's featured video may be repeated regularly, and deque was used to prevent this.

.. code:: python3

    from youtube_related import preventDuplication

    Avoider = preventDuplication()

    print(Avoider.get('Some Youtube Video URL'))
