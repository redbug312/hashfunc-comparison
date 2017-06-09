#! /usr/bin/python3
from math import floor, sqrt
from functools import reduce
from operator import mul
import matplotlib.pyplot as plot
import numpy

def nearest_sqrt(xx):
    x = floor(sqrt(xx))
    if x ** 2 >= xx:
        return (x, x)
    elif x ** 2 + x >= xx:
        return (x+1, x)
    else:
        return (x+1, x+1)

def show_tilechart(stat):
    mean = numpy.mean(stat)
    pattern = '□■'

    for tile_y in stat:
        for tile_yx in tile_y:
            print(pattern[int(tile_yx > mean)] if tile_yx else ' ', end='')
        print() # newline

def show_tilechart_gui(stat):
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
