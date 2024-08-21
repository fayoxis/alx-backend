#!/usr/bin/env python3
"""A basic caching module implemented using a dictionary.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that provides basic caching functionality.

    Allows storing and retrieving key-value pairs in a dictionary.
    """
    def put(self, key, item):
        """Store a key-value pair in the cache.

        Args:
            key (hashable):key associated with the value to be cached.
            item (object): The value to be cached.

        Returns:
            None
        """
        do_put = True
        while do_put:
            if key is None or item is None:
                do_put = False
            else:
                self.cache_data[key] = item
                do_put = False

    def get(self, key):
        """Retrieve a value from the cache using its key.

        Args:
            key (hashable): key associated with the value to be retrieved.

        Returns:
            object: value associated with the key, present in the cache.
            None: If the key is not found in the cache.
        """
        do_get = True
        result = None
        while do_get:
            result = self.cache_data.get(key, None)
            do_get = False
        return result
