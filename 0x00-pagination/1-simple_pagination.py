#!/usr/bin/env python3
"""Pagination"""

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple:
    """Takes two integer arguments page and page_size
    and return tuple"""
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page > 0

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Returns list'''
        try:
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page > 0
        except AssertionError:
            raise
        page_list: List = []
        page_indexes: Tuple[int, int] = index_range(page, page_size)
        start, end = page_indexes
        page_list = self.dataset()[start:end]
        return (page_list)
