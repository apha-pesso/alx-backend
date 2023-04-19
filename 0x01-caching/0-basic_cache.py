#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A new cache class"""

    def __init__(self):
        """Instantiate BasicCache"""
        super().__init__()

    def put(self, key, item):
        """Assign item to key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Return value in key"""
        if key:
            return self.cache_data.get(key)
