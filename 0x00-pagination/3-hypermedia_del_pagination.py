#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination with do-while loops
"""
import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a new Server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Retrieve the cached dataset using a do-while loop.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Create an indexed dataset using a do-while loop.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {}
            i = 0
            while i < len(dataset):
                self.__indexed_dataset[i] = dataset[i]
                i += 1
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve info about a page from a given index and with a
        specified size using a do-while loop.
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        page_data = []
        data_count = 0
        next_index = None
        start = index if index else 0
        i = start
        while i < len(data) and data_count < page_size:
            item = data[i]
            page_data.append(item)
            data_count += 1
            i += 1
        if data_count == page_size:
            next_index = i
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        return page_info
