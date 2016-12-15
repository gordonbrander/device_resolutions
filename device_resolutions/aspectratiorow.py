"""Guard and reader functions for working with aspect ratio CSV"""
from device_resolutions.util import as_float


def AspectRatioRow((width, height, title)):
    """Guard/validation function for aspect ratio rows"""
    return (as_float(width), as_float(height), str(title))