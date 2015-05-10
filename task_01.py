#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""


def xfibo(count):
    """Fibo sequence generation function.

    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        list: A generator of Fibonacci numbers.

    Examples:
        >>> xfibo(7)
        0
        1
        1
        2
        3
        5
        8
    """
    iteration = 0
    lastnum, curnum = 0, 1
    while iteration < count:
        yield lastnum
        lastnum, curnum = curnum, lastnum + curnum
        iteration += 1
