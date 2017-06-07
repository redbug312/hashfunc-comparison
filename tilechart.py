#! /usr/bin/python3
from math import floor, sqrt
import numpy

def nearest_sqrt(xx):
    x = floor(sqrt(xx))
    if x ** 2 >= xx:
        return (x, x)
    elif x ** 2 + x >= xx:
        return (x, x+1)
    else:
        return (x+1, x+1)

def show_tilechart(z):
    # cmap: https://matplotlib.org/examples/color/colormaps_reference.html
    _, ax = plot.subplots()
    ax.imshow(z, cmap='Greys', interpolation='nearest')
    plot.show()

if __name__ == '__main__':
    import sys
    import json
    import matplotlib.pyplot as plot
    from functools import reduce
    from operator import mul

    result = json.load(sys.stdin)
    collision = numpy.fromiter((len(bucket) for bucket in result), int)
    size = nearest_sqrt(len(collision))
    tiles = numpy.resize(collision, reduce(mul, size)) \
                 .reshape(size)

    show_tilechart(tiles)
