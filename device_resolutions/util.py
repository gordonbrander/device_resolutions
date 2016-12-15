"""Utility functions"""

nan = float('nan')


def as_float(x):
    try:
        return float(x)
    except ValueError:
        return nan


def find_with(f, iter, default=None):
    """Find the value in an iterator satisfying f(x)"""
    return next((x for x in iter if f(x)), default)


def lowest(a, b):
    return a if a < b else b


def find_lowest(iter):
    """Given a finite iterator of ints or floats, find the lowest"""
    return reduce(lowest, iter, float('inf'))