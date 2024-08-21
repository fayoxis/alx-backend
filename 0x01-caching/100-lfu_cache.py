#!/usr/bin/env python3
"""this is Least Frequently Used (LFU) Cache Module."""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents an object that stores & retrieves items dictionary
    using the Least Frequently Used caching mechanism. When the cache
    limit is reached, the least frequently used item is removed.
    """
    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorder the items in cache based on the most recently used key.
        Update the frequency count of the MRU key & reposition it in the keys_freq list.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        i = 0
        do_continue = True
        while do_continue:
            if i < len(self.keys_freq):
                key_freq = self.keys_freq[i]
                if key_freq[0] == mru_key:
                    mru_freq = key_freq[1] + 1
                    mru_pos = i
                    do_continue = False
                elif len(max_positions) == 0:
                    max_positions.append(i)
                elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                    max_positions.append(i)
            else:
                do_continue = False
            i += 1

        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """Add an item to the cache.
        If the cache is full and the new item needs to be added,
        discard the least frequently used item.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            i = 0
            do_continue = True
            while do_continue:
                if i < len(self.keys_freq):
                    key_freq = self.keys_freq[i]
                    if key_freq[1] == 0:
                        ins_index = i
                        do_continue = False
                else:
                    do_continue = False
                i += 1
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieve an item from the cache by key.
        Update the frequency count of the retrieved key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
