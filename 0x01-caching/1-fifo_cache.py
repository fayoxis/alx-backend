#!/usr/bin/env python3
"""This module implements a First-In First-Out (FIFO) cache.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This class represents a FIFO cache.
    It stores and retrieves items from a dictionary,
    removing the oldest items when the cache limit is reached.
    """
    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.
        If the key or item is None, do nothing.
        If the cache size exceeds the limit, remove the oldest items.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        while len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieve an item from the cache by its key.
        If the key is not found, return None.
        """
        return self.cache_data.get(key, None)
