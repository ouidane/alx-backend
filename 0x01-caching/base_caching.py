#!/usr/bin/python3
""" BaseCaching module.
"""

class BaseCaching():
    """ A base caching system
      - you can store items in the cache
      - you can retrieve items from the cache
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Instantiation
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Retrieve an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
