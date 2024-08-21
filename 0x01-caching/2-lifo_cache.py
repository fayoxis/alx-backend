#!/usr/bin/env python3
"""
caching module that implements the Last-In First-Out (LIFO) policy.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A class that represents a cache with a LIFO removal mechanism.
    When the cache reaches its maximum capacity,
    """
    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key (str): The key for the item.
            item (obj): The item to be cached.

        If the cache is already full, the last item added
        will be discarded before adding the new item.
        """
        if key is None or item is None:
            return

        remove_item = False
        while len(self.cache_data) + (1 if remove_item else 0) > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(True)
            print("DISCARD:", last_key)
            remove_item = True

        if remove_item:
            self.cache_data[key] = item
        elif key not in self.cache_data:
            self.cache_data[key] = item

        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key (str): The key for the item.

        Returns:
            obj: The cached item, or None if the key is not found.
        """
        return self.cache_data.get(key, None)
