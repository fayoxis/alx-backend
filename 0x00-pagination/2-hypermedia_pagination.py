#!/usr/bin/env python3
"""Hypermedia pagination sample.
"""
import csv
import math
from typing import Dict, List, Tuple

# Calculates the start and end indices for a given page and page size
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

# Class to handle pagination of a dataset
class Server:
    """Paginates a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the Server instance."""
        self.__dataset = None
        self.__page = 1
        self.__page_size = 10

    # Loads and caches the dataset from a CSV file
    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    # Retrieves the data for the current page
    def get_page(self) -> List[List]:
        data = self.dataset()
        start, end = index_range(self.__page, self.__page_size)
        if start > len(data):
            return []
        return data[start:end]

    # Retrieves information about the current page
    def get_hyper(self) -> Dict:
        page_data = self.get_page()
        start, end = index_range(self.__page, self.__page_size)
        total_pages = math.ceil(len(self.__dataset) / self.__page_size)
        page_info = {
            'page_size': len(page_data),
            'page': self.__page,
            'data': page_data,
            'next_page': self.__page + 1 if end < len(self.__dataset) else None,
            'prev_page': self.__page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_info

    # Navigates through pages using a do-while loop
    def navigate(self):
        page_info = self.get_hyper()
        total_pages = page_info['total_pages']

        loop = True
        while loop:
            # Print current page information
            print(f"Page {self.__page}/{total_pages}")
            print(page_info)

            # Get user input for navigation
            choice = input("Enter 'n' 4 next page, 'p' for previous page, or 'q' to quit: ")
            if choice == 'n':
                # Move to the next page if available
                if page_info['next_page'] is not None:
                    self.__page = page_info['next_page']
                    page_info = self.get_hyper()
                else:
                    print("You are already on the last page.")
            elif choice == 'p':
                # Move to the previous page if available
                if page_info['prev_page'] is not None:
                    self.__page = page_info['prev_page']
                    page_info = self.get_hyper()
                else:
                    print("You are already on the first page.")
            elif choice == 'q':
                # Exit the navigation loop
                loop = False
            else:
                print("Invalid choice. Please try again.")

# Create a Server instance and start navigating
server = Server()
server.navigate()
