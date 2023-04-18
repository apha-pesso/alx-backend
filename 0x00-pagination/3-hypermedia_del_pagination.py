#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns items requested when rows are removed"""
        assert index < 1000

        req_dict = {}
        data_ = self.indexed_dataset()
        # index = page * page_size
        page = index // page_size

        end_index = index + page_size

        next_index = end_index

        data_set = []

        for i in range(index, end_index):
            if i not in data_.keys():
                end_index += 1
            else:
                data_set.append(data_[i])

        req_dict["index"] = index
        req_dict["data"] = data_set
        req_dict["page_size"] = page_size
        req_dict["next_index"] = end_index
        return req_dict

        """
        end_index = index + page_size
        next_index = end_index
        page = index // page_size + 1
        data = []
        for i in range(index, end_index):
            if i in data_.keys():
                data.append(data_[i])
            else:
                next_index += 1
        req_dict["index"] = index
        req_dict["data"] = data
        req_dict["page_size"] = page_size
        req_dict["next_index"] = next_index
        return req_dict
        """
