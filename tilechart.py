#! /usr/bin/python3
""" It reads the transformed data outputed from hashfunc.py to show tilecharts
"""

from math import floor, sqrt
from functools import reduce
from operator import mul
import matplotlib.pyplot as plot
import numpy

def nearest_sqrt(xx):
    """ Find a near-square size for tilechart
    Args:
        area as `int`
    Returns:
        length and width as `(int, int)`
    """
    x = floor(sqrt(xx))
    if x ** 2 >= xx:
        return (x, x)
    elif x ** 2 + x >= xx:
        return (x+1, x)
    else:
        return (x+1, x+1)

def show_tilechart(stat):
    """ Show the tilechart in terminal
    Args:
        stat of chain lengths in hashtable as `[int]`
    """
    mean = numpy.mean(stat)
    pattern = '□■'

    for tile_y in stat:
        for tile_yx in tile_y:
            print(pattern[int(tile_yx > mean)] if tile_yx else ' ', end='')
        print() # newline

def show_tilechart_gui(stat):
    """ Show the barchart by pyplot
    Args:
        stat of chain lengths in hashtable as `[int]`
    """
    # cmap: https://matplotlib.org/examples/color/colormaps_reference.html
    _, ax = plot.subplots()
    ax.imshow(stat, cmap='Greys', vmin=0, vmax=numpy.amax(stat), interpolation='nearest')
    plot.show()


if __name__ == '__main__':
    import sys
    import json
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "g", [])
        options = dict(opts)
    except getopt.GetoptError:
        print('Invalid options')
        sys.exit(1)

    result = json.load(sys.stdin)
    freq = numpy.fromiter((len(bucket) for bucket in result), int)
    size = nearest_sqrt(len(freq))

    tiles = numpy.zeros(reduce(mul, size))
    tiles[:freq.shape[0]] = freq
    tiles = tiles.reshape(size)

    if '-g' in options:
        show_tilechart_gui(tiles)
    else:
        show_tilechart(tiles)
