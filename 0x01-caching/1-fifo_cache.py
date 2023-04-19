#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A new cache class"""

    def __init__(self):
        """Instantiate BasicCache"""
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """Assign item to key"""
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            if key and item and key not in self.key_list:
                first_in = self.key_list.pop(0)
                self.cache_data.pop(first_in)
                print("DISCARD: {}".format(first_in))

        if key and item:
            self.cache_data[key] = item
            try:
                self.key_list.remove(key)
            except ValueError:
                pass
            self.key_list.append(key)

    def get(self, key):
        """Return value in key"""
        if key:
            return self.cache_data.get(key)
