#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""

import task_01


def fibo(count):
    """Fibo list comprehensions function."""
    numbers = [num for num in task_01.xfibo(count)]
    return numbers
