"""
processing utilities
"""
import numpy as np


def smooth_curve(curve, length):
    """
    smooth a cure with a boxcar of length
    """
    boxcar = np.ones(length)/length
    s_curve = np.convolve(boxcar, curve, mode='same')
    return s_curve
