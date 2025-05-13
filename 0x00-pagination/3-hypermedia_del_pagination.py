#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: row for i, row in enumerate(dataset)
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a deletion-resilient page of the dataset from starting index.

        Args:
            index (int): starting index
            page_size (int): number of items to return

        Returns:
            dict: with keys 'index', 'next_index', 'page_size', and 'data'
        """
        indexed_data = self.indexed_dataset()
        assert isinstance(index, int) and 0 <= index < len(self.dataset()), \
            "index must be a valid non-negative integer within range"

        data = []
        current_index = index

        while len(data) < page_size and current_index < len(self.dataset()):
            item = indexed_data.get(current_index)
            if item is not None:
                data.append(item)
            current_index += 1

        return {
            'index': index,
            'next_index': current_index,
            'page_size': len(data),
            'data': data
        }
