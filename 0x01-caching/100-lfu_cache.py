#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A new cache class"""

    def __init__(self):
        """Instantiate BasicCache"""
        super().__init__()
        self.key_list = []
        self.key_dict = {}

    def put(self, key, item):
        """Assign item to key"""
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            if key and item and key not in self.key_list:

                values = list(self.key_dict.values())
                # min_value = min(list(self.key_dict.values()))
                min_value = min(values)

                count = values.count(min_value)
                # for i in range(count):
                for key in self.key_list:
                    for keye, value in self.key_dict.items():
                        if value == min_value:
                            my_key = keye

                try:
                    self.key_list.remove(my_key)
                except ValueError:
                    pass
                try:
                    self.cache_data.pop(my_key)
                except KeyError:
                    pass
                print("DISCARD: {}".format(my_key))

        if key and item:
            self.cache_data[key] = item
            try:
                self.key_list.remove(key)
            except ValueError:
                pass

            try:
                self.key_dict[key] += 1
            except KeyError:
                self.key_dict[key] = 1

            self.key_list.append(key)

    def get(self, key):
        """Return value in key"""
        if key and self.cache_data.get(key):
            try:
                self.key_list.remove(key)
            except ValueError:
                pass

            self.key_dict[key] += 1

            self.key_list.append(key)
            return self.cache_data.get(key)
