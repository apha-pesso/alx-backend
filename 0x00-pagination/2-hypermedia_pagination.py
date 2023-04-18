#!/usr/bin/env python3
"""Pagination"""

import csv
import math
from typing import Dict, List, Tuple


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        if page < 2:
            prev = None
        else:
            prev = page - 1

        hyper_dict = {}

        # index = index_range(page, page_size)

        data_ = self.get_page(page, page_size)

        # if ((page * page_size) > len(data_)):
            # next_ = None
        # else:
            # next_ = page + 1

        # if data_:
            # next_ = page + 1
        # else:
            # next_ = None

        total = len(self.dataset()) / page_size
        if page >= total:
            next_ = None
        else:
            next_ = page + 1
        # print(total)

        hyper_dict['page_size'] = len(data_)
        hyper_dict['page'] = page
        hyper_dict['data'] = data_
        hyper_dict['next_page'] = next_
        hyper_dict['prev_page'] = prev
        hyper_dict['total_pages'] = math.ceil(total)
        return hyper_dict
