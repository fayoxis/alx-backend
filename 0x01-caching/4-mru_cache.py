#!/usr/bin/env python3
"""
This module implements a Most Recently Used (MRU) caching strategy.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class provides a caching mechanism that stores and retrieves
    items from a dictionary using the Most Recently Used removal strategy.
    When the cache limit is reached, least recently used item is discarded.
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
            item (obj): The item to be cached.

        If the key is already present in the cache, update its value.
        If the cache is full and a new item needs to be added, discard the
        least recently used item before adding the new one.
        """
        if key is None or item is None:
            return

        cache_full = False
        do
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    mru_key, _ = self.cache_data.popitem(False)
                    print("DISCARD:", mru_key)
                    cache_full = True
                else:
                    self.cache_data[key] = item
                    self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item
        while cache_full

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item.

        Returns:
            obj: The cached item if present, otherwise None.

        If the key is found in the cache, move to end of the OrderedDict
        to mark it as the most recently used item.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
