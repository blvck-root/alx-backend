#!/usr/bin/env python3

'''Task 1: FIFO caching
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from
       `BaseCaching` and is a caching system.
    '''

    def __init__(self):
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data` the
           `item` value for the key `key`
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key, = self.cache_order.pop(0)
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        '''return the value in `self.cache_data` linked to `key`
        '''
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key, None)
