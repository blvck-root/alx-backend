#!/usr/bin/env python3
"""
Function: index_range.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for a given page and page size.

    Args:
        page: The page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple containing the start and end indices.
  """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
