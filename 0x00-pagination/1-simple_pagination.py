#!/usr/bin/env python3
"""A simple script to paginate a dataset of popular baby names.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start-end indices 4 a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """class to handle pagination of dataset of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize an instance of the Server class.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file.
        """
        if self.__dataset is None:
            self.__dataset = []
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                row = next(reader)  # Skip header row
                while True:
                    try:
                        row = next(reader)
                        self.__dataset.append(row)
                    except StopIteration:
                        break

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data from the dataset.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        while start >= len(data):
            return []
        return data[start:end]
