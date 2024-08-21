#!/usr/bin/env python3
"""
This module implements a Most Recently Used (MRU) caching system.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class manages a cache with Most Recently Used eviction policy.
    When the cache limit is reached, least recently used item is discarded.
    """
    def __init__(self):
        """
        Initialize the cache with an OrderedDict to track item usage order.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add or update an item in the cache.
        If the cache limit is reached, discard the least recently used item.
        """
        if key is None or item is None:
            return

        do_discard = False
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                do_discard = True

        while do_discard:
            mru_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", mru_key)
            if len(self.cache_data) + 1 <= BaseCaching.MAX_ITEMS:
                do_discard = False

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        Retrieve an item from the cache and update its usage order.
        Return None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
