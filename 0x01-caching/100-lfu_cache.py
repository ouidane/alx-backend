#!/usr/bin/python3
"""LFU cache replacement implementation class.
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFU cache replacement implementation class

    Attributes:
        __stats (list): Stores cache keys in order of entry
        __rlock (RLock): Lock accessed resources to prevent race condition
    """
    def __init__(self):
        """ Instantiation method, sets instance attributes.
        """
        super().__init__()
        self.__stats = {}
        self.__rlock = RLock()

    def put(self, key, item):
        """ Replace an item in the cache.
        """
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """ Retrieve an item by key.
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """ Removes the least frequently used item from the cache.
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(keyOut)
                    self.__stats.pop(keyOut)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return keyOut
