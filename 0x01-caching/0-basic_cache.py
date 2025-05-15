#!/usr/bin/python3
"""Basic caching module implementation class.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache implementaion class that inherits from BaseCaching

    Attributes:
        MAX_ITEMS: number of items in the cache
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Retrieve an item by key
        """
        return self.cache_data.get(key, None)
