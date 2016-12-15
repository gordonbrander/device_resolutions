from math import sqrt
import csv
from device_resolutions.util import find_lowest
from device_resolutions.devicerow import DeviceRow
from device_resolutions.aspectratiorow import AspectRatioRow


def as_orientation(x, y, is_portrait=False):
    """Given an x and y, return in orientation specified by `is_portrait`."""
    if is_portrait:
        return (y, x) if x > y else (x, y)
    else:
        return (x, y) if x > y else (y, x)


def as_portrait(x, y):
    """Given a dimensions, return that pair in portrait orientation"""
    return as_orientation(x, y, is_portrait=True)


def as_landscape(x, y):
    """Given a dimensions, return that pair in landscape orientation"""
    return as_orientation(x, y, is_portrait=False)


def is_portrait_primary(w, h):
    """Given a width and a height, deterimine if portrait is primary."""
    return h > w


def calc_hypotenuse(a, b):
    """Calculate length of hypotenuse using Pythagorian theorem"""
    return sqrt(a**2 + b**2)


def calc_screen_dimensions_in(width_px, height_px, ppi):
    """
    Calculate screen dimensions (width, height) in inches given dimensions
    in px and pixels-per-inch (ppi).
    """
    return (width_px / float(ppi), height_px / float(ppi))


def calc_screen_size_in(x_px, y_px, ppi):
    """
    Calculate diagonal screen size given dimensions in pixels and
    pixels-per-inch (ppi)
    """
    a, b = calc_screen_dimensions_in(x_px, y_px, ppi)
    return calc_hypotenuse(a, b)


def read_csv(f, Model):
    """
    Given a CSV file with a header, read rows through `Model` function.
    Returns generator function.
    """
    reader = csv.reader(f, dialect="excel")
    next(reader, None)  # skip the header row
    return (Model(row) for row in reader)


with open('./aspect_ratios.csv') as f:
    ASPECT_RATIOS = tuple(read_csv(f, AspectRatioRow))

with open('./device_resolutions.csv') as f:
    DEVICE_RESOLUTIONS = tuple(read_csv(f, DeviceRow))


def find_aspect_ratio(x, y):
    """
    Given an aspect ratio, find an aspect ratio description using a list
    of common aspect ratios.
    """
    ratio = x / y
    for cx, cy, name in ASPECT_RATIOS:
      if ratio == (cx/cy):
        return (ratio, cx, cy, name)
    return (ratio, ratio, 1, "")