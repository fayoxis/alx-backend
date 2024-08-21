#!/usr/bin/env python3
"""LRU Cache implementation using OrderedDict"""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache class for storing and retrieving items
    with a Least Recently Used removal mechanism when
    the cache limit is reached.
    """
    def __init__(self):
        """Initialize the LRU Cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add or update an item in the LRU Cache.
        If the cache is full, discard the least recently used item.
        """
        if key is None or item is None:
            return

        while True:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    lru_key, _ = self.cache_data.popitem(True)
                    print("DISCARD:", lru_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
                break
            else:
                self.cache_data[key] = item
                break

    def get(self, key):
        """Retrieve an item from the LRU Cache.
        Update the item as the most recently used.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
