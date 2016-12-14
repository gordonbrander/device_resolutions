from math import sqrt
import csv

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

def calc_hypotenuse(a, b):
    """Calculate length of hypotenuse using Pythagorian theorem"""
    return sqrt(a**2 + b**2)

def calc_ppi(width_px, height_px, hypotenuse_in):
    """
    Given the diagnonal measurement of the screen in inches (`hypotenuse_in`),
    calculate the pixels-per-inch (ppi) offered by the screen.
    """
    hypotenuse_px = calc_hypotenuse(width_px, height_px)
    return hypotenuse_px / hypotenuse_in

# @TODO port to CSV
COMMON_ASPECT_RATIOS = (
  (3, 4, "3:4"),
  (1, 1, "1:1"),
  (5, 4, "5:4"),
  (4, 3, "4:3"),
  (1.43, 1, "IMAX 1.43:1"),
  (3, 2, "3:2"),
  (5, 3, "5:3"),
  (14, 9, "14:9"),
  (16, 10, "16:10"),
  (16, 9, "16:9"),
  (17, 9, "17:9"),
  (21, 9, "21:9"),
  (1.375, 1, "Academy Ratio 1.375:1"),
  (2.35, 1, "CinemaScope 2.35:1"),
  (2.59, 1, "Cinemara 2.59:1"),
  (2.75, 1, "Ultra Panavision 70 2.75:1"),
  (2.76, 1, "MGM 65 2.76:1"),
)

def find_aspect_ratio(x, y):
    """
    Given an aspect ratio, find an aspect ratio description using a list
    of common aspect ratios.
    """
    ratio = x / y
    for cx, cy, name in COMMON_ASPECT_RATIOS:
      if ratio == (cx/cy):
        return (ratio, cx, cy, name)
    return (ratio, ratio, 1, "")