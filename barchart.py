#! /usr/bin/python3
""" It reads the transformed data outputed from hashfunc.py to show barcharts
"""

import matplotlib.pyplot as plot
import numpy

def show_barchart(stat, length=20):
    """ Show the barchart in terminal
    Args:
        stat of chain lengths in hashtable as `[int]`
        maximum length of bars in barchart
    """
    if isinstance(stat, list):
        data = enumerate(stat)
    elif isinstance(stat, dict):
        data = stat

    y_max = max(max(stat), length)
    for x, y in data:
        y_len = int(length * y / y_max)
        print('{:>3}: {}'.format(x, '*' * y_len))
    print('\nmax: {}, min: {}, avg: {:.2f}' \
          .format(max(stat), min(stat), sum(stat) / len(stat)))

def show_barchart_gui(stat):
    """ Show the barchart by pyplot
    Args:
        stat of chain lengths in hashtable as `[int]`
    """
    if isinstance(stat, list):
        plot.bar(numpy.arange(len(stat)), stat)
    elif isinstance(stat, dict):
        data = sorted(stat.items(), key=lambda item: (-item[1], item[0]))
        plot.bar(numpy.arange(len(stat)), [d[1] for d in data])
        plot.tick_params(labelbottom='off')

    plot.tight_layout(pad=0.8)
    plot.show()
    return plot


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
    height = [len(bucket) for bucket in result]
    print("The standard deviation is {:.2f}".format(numpy.std(height)))

    if '-g' in options:
        show_barchart_gui(height)
    else:
        show_barchart(height)
