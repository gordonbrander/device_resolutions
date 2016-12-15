"""Guard and reader functions for dealing with device CSV"""
from device_resolutions.util import find_lowest, as_float

def DeviceRow((model, width_dp, height_dp, width_px, height_px, screen_in, is_touch)):
    """Guard/validation function for device rows"""
    return (
        str(model),
        as_float(width_dp),
        as_float(height_dp),
        as_float(width_px),
        as_float(height_px),
        as_float(screen_in),
        bool(is_touch)
    )


def model(row):
    return row[0]


def width_dp(row):
    return row[1]


def height_dp(row):
    return row[2]


def width_px(row):
    return row[3]


def height_px(row):
    return row[4]


def screen_in(row):
    return row[5]


def is_touch(row):
    return row[6]