#!/usr/bin/env python3
"""Last-In First-Out (LIFO) Caching Module
This module implements a LIFO cache using an OrderedDict.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents a LIFO (Last-In First-Out) cache.
    This class inherits from BaseCaching, overrides put and get methods.
    """
    def __init__(self):
        """Initialize the cache.
        Creates an empty OrderedDict to store key-value pairs.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.
        If the cache size exceeds the maximum allowed, discard the least
        recently added item (LIFO) to make room for the new item.

        Args:
            key (str): The key associated with the item.
            item (obj): The item to be cached.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            while len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve an item from the cache.
        Args:
            key (str): The key associated with the item.

        Returns:
            obj: The cached item if found, None otherwise.
        """
        return self.cache_data.get(key, None)
