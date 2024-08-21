#!/usr/bin/env python3
"""Last-In First-Out (LIFO) Caching Module
This module implements a LIFO cache using an OrderedDict.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class represents a cache with a Least-In-First-Out
    (LIFO) removal mechanism when the cache limit is reached.
    """
    def __init__(self):
        """Initialize the cache with an empty OrderedDict.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        If the key doesn't exist in the cache and adding the new
        item would exceed the cache limit, remove the least
        recently added items until there's enough space.
        Then, add the new item to the cache.

        If the key already exists, update its value and move it
        to the end of the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            while len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve an item from the cache by its key.

        Return the value of the item if the key exists,
        otherwise return None.
        """
        return self.cache_data.get(key, None)
