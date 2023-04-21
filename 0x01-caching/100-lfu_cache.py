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
                # if key and item:

                values = list(self.key_dict.values())
                # min_value = min(list(self.key_dict.values()))
                min_value = min(values)

                # count = values.count(min_value)
                # for i in range(count):
                # for k in self.key_list:
                # a = 0
                # print("Check")
                # print(self.key_list)
                # print(self.key_dict)
                # print(min_value)
                # print("Check")
                for k in self.key_list:
                    for keye, value in self.key_dict.items():
                        if value == min_value and k == keye:
                            my_key = keye
                            print(keye)
                            break
                    try:
                        if my_key:
                            break
                    except UnboundLocalError:
                        pass

                """
                for keye, value in self.key_dict.items():
                    # print(keye, value, min_value)
                    # print(self.key_list)
                    # print(self.key_dict)
                    if value == min_value and keye == self.key_list[a]:
                        print(keye, value, value, self.key_list[a])
                        my_key = keye
                        print(a)
                        break
                    a += 1
                """

                try:
                    self.key_list.remove(my_key)
                except ValueError:
                    pass

                try:
                    # self.cache_data.pop(my_key)
                    self.key_dict.pop(my_key)
                except KeyError:
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
