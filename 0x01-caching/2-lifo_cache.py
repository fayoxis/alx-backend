#!/usr/bin/env python3
"""
caching module that implements the Last-In First-Out (LIFO) policy.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A class that represents a cache with a LIFO removal mechanism.
    When the cache reaches its maximum capacity.
    """
    def __init__(self):
        """
        Initialize the cache with an empty OrderedDict.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key associated with the item.
            item (object): The item to be cached.

        If the cache is full, new item needs tobe added, the most recently
        added item is discarded to make room for the new item.
        """
        if key is None or item is None:
            return
        while True:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    last_key, _ = self.cache_data.popitem(True)
                    print("DISCARD:", last_key)
                else:
                    break
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
            break

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item.

        Returns:
            cached item if the key exists in the cache, None otherwise.
        """
        return self.cache_data.get(key, None)
