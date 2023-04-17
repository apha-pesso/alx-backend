#!/usr/bin/env python3

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Takes two integer arguments page and page_size
    and return tuple"""
    try:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
    except AssertionError:
        raise

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
