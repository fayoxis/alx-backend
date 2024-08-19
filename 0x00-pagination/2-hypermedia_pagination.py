#!/usr/bin/env python3
"""This script implements a pagination system for a dataset.
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end indices for a given page$page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to handle pagination of a baby names dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance with an empty dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file.
        """
        if self.__dataset is None:
            dataset = []
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                row = next(reader, None)  # Skip the header row
                while row:
                    dataset.append(row)
                    row = next(reader, None)
            self.__dataset = dataset

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a specific page of data from the dataset.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        page_data = []
        i = start
        while i < end and i < len(data):
            page_data.append(data[i])
            i += 1
        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieve hypermedia information for a specific page.
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
